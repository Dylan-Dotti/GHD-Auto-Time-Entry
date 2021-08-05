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
    
    def open_cell_details(self) -> SapDetailsWindowNavigator:
        self._kc.press_f2(post_delay=0.5)
        details_wc = factory.get_sap_details_window_controller()
        details_kc = KeyboardController(details_wc)
        return SapDetailsWindowNavigator(details_kc)

    def move_next_col(self):
        self._kc.press_tab()
        self._current_col_index += 1
        if self._current_col_index == self._row_length():
            self._current_row_index += 1
            self._current_col_index = 0
    
    def move_prev_col(self):
        if (self._current_row_index == 0 and self._current_col_index == 0):
            return
        self._kc.press_reverse_tab()
        self._current_col_index -= 1
        if self._current_col_index == -1:
            self._current_row_index -= 1
            self._current_col_index = self._row_length() - 1
    
    def move_current_row_start(self):
        while self._current_col_index > 0:
            self.move_prev_col()
            time.sleep(0.1)

    def move_current_row_end(self):
        while self._current_col_index < self._row_length() - 1:
            self.move_next_col()
            time.sleep(0.1)
    
    def _row_length(self):
        return len(self._row_layout)
    
