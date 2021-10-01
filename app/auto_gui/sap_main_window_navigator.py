from app.interfaces.stoppable import Stoppable
from app.auto_gui.sap_confirmat_prompt_window_navigator import SapConfirmatPromptWindowNavigator
from typing import Tuple
from app.auto_gui.keyboard_controller import KeyboardController
from app.auto_gui.sap_details_window_navigator import SapDetailsWindowNavigator
from pandas.io.clipboard import copy, paste
import app.auto_gui.window_controller_factory as factory
import time


class SapMainWindowNavigator(Stoppable):

    def __init__(self, sap_keyboard_controller: KeyboardController, rows_per_page: int=None) -> None:
        self._kc = sap_keyboard_controller
        self._current_row_index = 0
        self._current_col_index = 0
        self._rows_per_page = rows_per_page
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

    def open_cell_details(self) -> Tuple[SapDetailsWindowNavigator, KeyboardController]:
        self._kc.press_f2(post_delay=.5)
        details_wc = factory.get_sap_details_window_controller()
        details_kc = KeyboardController(details_wc, False)
        return SapDetailsWindowNavigator(details_kc), details_kc
    
    def open_reset_entries(self) -> Tuple[SapConfirmatPromptWindowNavigator, KeyboardController]:
        self._kc.press_f_key('f11', modifier_key='ctrl', post_delay=.5)
        confirm_wc = factory.get_sap_confirmat_prot_window_controller()
        confirm_kc = KeyboardController(confirm_wc, False)
        return SapConfirmatPromptWindowNavigator(confirm_kc), confirm_kc

    def select_all_entries(self) -> None:
        self._kc.press_f_key('f7', modifier_key='shift', post_delay=1)
    
    def delete_all_entries(self) -> None:
        self.select_all_entries()
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
            self.move_prev_col()

    def move_current_row_end(self):
        while self._current_col_index < self._row_length() - 1:
            self.move_next_col()

    def move_next_row_start(self):
        self.move_current_row_end()
        if self._current_row_index > 0 and (self._rows_per_page is None or self._current_row_index == self._rows_per_page - 1):
            self.move_next_row_alternate()
            if self._test_cell_has_data():
                self._rows_per_page = self._current_row_index + 1
                print('rows per page: ' + str(self._rows_per_page))
                self.page_down()
        else:
            self.move_next_col()
    
    # Immediately moves to next row by pressing down
    def move_next_row_direct(self):
        self._kc.press_down_arrow()
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
    
    def move_first_empty_row(self) -> None:
        while self._test_cell_has_data():
            self.move_next_row_direct()

    def move_to_day(self, day_index):
        if day_index < 0 or day_index > 6:
            raise ValueError('Invalid day index: ' + day_index)
        target_str = 'day' + str((day_index + 1))
        target_index = self._row_layout.index(target_str)
        while self._current_col_index != target_index:
            if self._current_col_index < target_index:
                self.move_next_col()
            elif self._current_col_index > target_index:
                self.move_prev_col()
    
    def page_down(self):
        self._kc.press_key('pgdn', post_delay=1)
        self._current_row_index = self._rows_per_page - 1
        while self._current_row_index > 1:
            self.move_prev_row_direct()

    def _row_length(self):
        return len(self._row_layout)
    
    def _test_cell_has_data(self):
        copy('')
        time.sleep(.25)
        # pressing ctrl-a will cause the window to lose foreground status
        # shift-home and shift-end work though
        self._kc.press_key('home', post_delay=.1)
        self._kc.press_select_to_end(post_delay=.1)
        self._kc.press_copy(post_delay=.25)
        cell_content = paste()
        return cell_content is not None and len(cell_content) > 0 and any(char != ' ' for char in cell_content)
