from app.auto_gui.keyboard_controller import KeyboardController
from app.auto_gui.sap_main_window_navigator import SapMainWindowNavigator
from app.data_formatter.SAP_Objects.sap_data_row import SapDataRow
from typing import List
from pandas.io.clipboard import copy, paste
import time

class AutoEntryAgent:

    def __init__(self, main_kc: KeyboardController,
                 main_nav: SapMainWindowNavigator,
                 data_rows: List[SapDataRow]) -> None:
        self._main_kc = main_kc
        self._main_nav = main_nav
        self._data_rows = data_rows

    def execute(self, clear_data = False) -> None:
        if clear_data:
            self._clear_data()
        for row_index, row in enumerate(self._data_rows):
            # Paste row data
            copy(row.to_sap_str())
            time.sleep(.5)
            self._main_kc.press_paste(post_delay=.25)
            self._main_kc.press_enter(post_delay=.5)
            # Move through cells and input notes
            for day_index, entry in enumerate(row.date_entries):
                if entry is not None:
                    self._main_nav.move_to_day(day_index)
                    details_nav, details_kc = self._main_nav.open_cell_details()
                    copy(entry.note)
                    details_nav.move_to_short_text_field()
                    details_kc.press_paste(post_delay=.25)
                    details_nav.confirm_and_close()
            if row_index < len(self._data_rows) - 1:
                self._main_nav.move_next_row_start()
    
    def _clear_data(self) -> None:
        reset_nav, _ = self._main_nav.open_reset_entries()
        reset_nav.select_yes()
    
    def _test_cell_has_data(self) -> bool:
        self._main_kc.press_select_to_end(post_delay=.1)
        self._main_kc.press_copy(post_delay=.25)
        cell_content = paste()
        print('Clipboard contents: ' + cell_content)
        return cell_content is not None and len(cell_content) > 0 and any(char != ' ' for char in cell_content)

