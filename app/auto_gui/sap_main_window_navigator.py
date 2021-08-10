from typing import Tuple
from app.auto_gui.keyboard_controller import KeyboardController
from app.auto_gui.sap_details_window_navigator import SapDetailsWindowNavigator
import app.auto_gui.window_controller_factory as factory
import time


class SapMainWindowNavigator:

    def __init__(self, sap_keyboard_controller: KeyboardController) -> None:
        self._kc = sap_keyboard_controller
        self._current_row_index = 0
        self._current_col_index = 0
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
        self._kc.press_f2(post_delay=0.5)
        details_wc = factory.get_sap_details_window_controller()
        details_kc = KeyboardController(details_wc)
        return SapDetailsWindowNavigator(details_kc), details_kc

    def move_next_col(self):
        self._kc.press_tab()
        self._current_col_index += 1
        if self._current_col_index == self._row_length():
            self._current_row_index += 1
            self._current_col_index = 0
        time.sleep(0.1)

    def move_prev_col(self):
        if (self._current_row_index == 0 and self._current_col_index == 0):
            return
        self._kc.press_reverse_tab()
        self._current_col_index -= 1
        if self._current_col_index == -1:
            self._current_row_index -= 1
            self._current_col_index = self._row_length() - 1
        time.sleep(0.1)

    def move_current_row_start(self):
        while self._current_col_index > 0:
            self.move_prev_col()

    def move_current_row_end(self):
        while self._current_col_index < self._row_length() - 1:
            self.move_next_col()

    def move_next_row_start(self):
        self.move_current_row_end()
        self.move_next_col()

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

    def _row_length(self):
        return len(self._row_layout)
