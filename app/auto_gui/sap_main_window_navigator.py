from app.interfaces.threadsafe_stoppable_w_subcomponents import ThreadSafeStoppableWithSubComponents
from app.interfaces.stoppable import Stoppable
from app.auto_gui.sap_confirmat_prompt_window_navigator import SapConfirmatPromptWindowNavigator
from typing import Tuple
from app.auto_gui.keyboard_controller import KeyboardController
from app.auto_gui.sap_details_window_navigator import SapDetailsWindowNavigator
from app.auto_gui.window_controller import WindowController
from pandas.io.clipboard import copy, paste
import app.auto_gui.window_names as win_names
import time


class SapMainWindowNavigator(ThreadSafeStoppableWithSubComponents):

    def __init__(self, sap_keyboard_controller: KeyboardController, rows_per_page: int) -> None:
        super().__init__()
        self._kc = sap_keyboard_controller
        self._current_row_index = 0
        self._current_col_index = 0
        self._rows_per_page = rows_per_page
        self._has_paged_down = False
        self._row_layout = [
            'activity_type', 'receiver_cc',
            'receiver_wbs', 'abs_type',
            'measure_unit', 'day1', 'from1',
            'to1', 'day2', 'from2', 'to2',
            'day3', 'from3', 'to3', 'day4',
            'from4', 'to4', 'day5', 'from5',
            'to5', 'day6', 'from6', 'to6',
            'day7', 'from7', 'to7'
        ]
        self._stop_requested = False
        self.add_stoppable_subcomponent(self._kc)
    
    def stop(self):
        print('Stopping SapMainWindowNavigator...')
        ThreadSafeStoppableWithSubComponents.stop(self)

    def open_cell_details(self) -> Tuple[SapDetailsWindowNavigator, KeyboardController]:
        self._kc.press_f2(post_delay=.5)
        details_wc = WindowController()
        if self._stop_requested:
            self._on_stop_request_acknowledge()
        self.add_stoppable_subcomponent(details_wc)
        details_wc.bind_to_window(win_names.DETAILS_WINDOW_NAMES)
        self.remove_stoppable_subcomponent(details_wc)
        details_kc = KeyboardController(details_wc, False)
        return SapDetailsWindowNavigator(details_kc), details_kc
    
    def open_reset_entries(self) -> Tuple[SapConfirmatPromptWindowNavigator, KeyboardController]:
        self._kc.press_f_key('f11', modifier_key='ctrl', post_delay=.5)
        confirm_wc = WindowController()
        if self._stop_requested:
            self._on_stop_request_acknowledge()
        self.add_stoppable_subcomponent(confirm_wc)
        confirm_wc.bind_to_window(win_names.CONFIRMAT_PROMPT_NAMES)
        self.remove_stoppable_subcomponent(confirm_wc)
        confirm_kc = KeyboardController(confirm_wc, False)
        return SapConfirmatPromptWindowNavigator(confirm_kc), confirm_kc

    def select_all_entries(self) -> None:
        self._kc.press_f_key('f7', modifier_key='shift', post_delay=1)
    
    def delete_all_entries(self) -> None:
        self.select_all_entries()
        if self._stop_requested:
            self._on_stop_request_acknowledge()
        self._kc.press_f_key('f2', modifier_key='shift', post_delay=1)

    def move_next_col(self):
        self._current_col_index += 1
        if self._current_col_index == self._row_length():
            self._current_row_index += 1
            self._current_col_index = 0
        self._kc.press_tab(post_delay=.05)

    def move_prev_col(self):
        if (self._current_row_index == 0 and self._current_col_index == 0):
            return
        self._current_col_index -= 1
        if self._current_col_index == -1:
            self._current_row_index -= 1
            self._current_col_index = self._row_length() - 1
        self._kc.press_reverse_tab(post_delay=.05)

    def move_current_row_start(self):
        while self._current_col_index > 0:
            if self._stop_requested:
                self._on_stop_request_acknowledge()
            self.move_prev_col()

    def move_current_row_end(self):
        while self._current_col_index < self._row_length() - 1:
            if self._stop_requested:
                self._on_stop_request_acknowledge()
            self.move_next_col()

    def move_next_row_start(self):
        self.move_current_row_end()
        if self._current_row_index > 0 and (self._current_row_index == self._rows_per_page - 1):
            self.move_next_row_alternate()
            if self._test_cell_has_data():
                self._rows_per_page = self._current_row_index + 1
                self.page_down()
        else:
            self.move_next_col()
    
    # Immediately moves to next row by pressing down
    def move_next_row_direct(self):
        if self._current_row_index >= self._rows_per_page - 1:
            return
        self._kc.press_down_arrow(post_delay=.1)
        self._current_row_index += 1
    
    # Immediately moves to previous row by pressing up
    def move_prev_row_direct(self):
        if self._current_row_index == 0:
            return
        self._kc.press_up_arrow(post_delay=.1)
        self._current_row_index -= 1
    
    def move_next_row_alternate(self):
        self.move_prev_row_direct()
        self.move_current_row_end()
        self.move_next_col()
        self.move_next_row_direct()
    
    def move_first_empty_row(self, reversed=False, empty_reversed=False) -> None:
        loop_condition = ((lambda: not self._test_cell_has_data()) if empty_reversed 
                          else (lambda: self._test_cell_has_data()))
        while loop_condition():
            if reversed:
                if self._current_row_index > 0:
                    self.move_prev_row_direct()
                else:
                    return
            else:
                if self._current_row_index < self._rows_per_page - 1:
                    self.move_next_row_direct()
                else:
                    self.page_down()

    def move_to_day(self, day_index, expected_data: str = None):
        if day_index < 0 or day_index > 6:
            raise ValueError('Invalid day index: ' + day_index)
        target_str = 'day' + str((day_index + 1))
        target_index = self._row_layout.index(target_str)
        start_index = self._current_col_index
        while self._current_col_index != target_index:
            if self._current_col_index < target_index:
                self.move_next_col()
            elif self._current_col_index > target_index:
                self.move_prev_col()
        # check for misalignment in case of SAP lag
        if expected_data is not None and not self._test_cell_has_data(expected_data):
            print('Misalignment detected. Attempting correction...')
            self._current_col_index = start_index
            while self._current_col_index != target_index:
                # move in direction of target
                if self._current_col_index < target_index:
                    self.move_next_col()
                elif self._current_col_index > target_index:
                    self.move_prev_col()
                # check if reached target
                if self._test_cell_has_data(expected_data):
                    print('Alignment corrected')
                    self._current_col_index = target_index
                    return
            # failed correction, throw error
            print()
            raise RuntimeError('Failed misalignment correction.')

    
    def page_down(self):
        self._kc.press_key('pgdn', post_delay=2)
        if not self._has_paged_down:
            self._has_paged_down = True
            self._rows_per_page += 1
        self._current_row_index = self._rows_per_page - 1
        while self._current_row_index > 0:
            self.move_prev_row_direct()
        self.move_first_empty_row(reversed=True, empty_reversed=True)
        self.move_next_row_direct()

    def _row_length(self) -> int:
        return len(self._row_layout)
    
    def _get_cell_data(self) -> str:
        copy('')
        time.sleep(.2)
        # pressing ctrl-a will cause the window to lose foreground status
        # shift-home and shift-end work though
        self._kc.press_key('home', post_delay=.1)
        self._kc.press_select_to_end(post_delay=.1)
        self._kc.press_copy(post_delay=.2)
        return paste()
    
    def _test_cell_has_data(self, test_data: str = None) -> bool:
        cell_content = self._get_cell_data()
        if test_data is None:
            return len(cell_content) > 0
        else:
            if cell_content == test_data:
                return True
            try:
                cell_content_f = float(cell_content)
                test_data_f = float(test_data)
                return abs(cell_content_f - test_data_f) <= 0.009
            except ValueError:
                return False
