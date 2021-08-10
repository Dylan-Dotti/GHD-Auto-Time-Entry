import pyperclip as clip
from app.auto_gui.keyboard_controller import KeyboardController
from app.auto_gui.sap_main_window_navigator import SapMainWindowNavigator
from typing import List
from app.data_formatter.sap_data_row import SapDataRow


class AutoEntryAgent:

    def __init__(self, main_kc: KeyboardController,
                 main_nav: SapMainWindowNavigator,
                 data_rows: List[SapDataRow]) -> None:
        self._main_kc = main_kc
        self._main_nav = main_nav
        self._data_rows = data_rows

    def execute(self):
        # layout_str = 'TEST	 	 	 	TEST	 	 	 		 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST	 	 	 TEST'
        # Convert rows to a string
        page_data_str = ''
        # Paste string data into the window
        # clip.copy(page_data_str)
        # clip.paste()
        # Move through cells and input notes
        for row_index, row in enumerate(self._data_rows):
            for day_index, entry in enumerate(row.date_entries):
                self._main_nav.move_to_day(day_index)
                details_nav = self._main_nav.open_cell_details()
                details_nav.move_to_short_text_field()
                clip.copy(entry.note)
                clip.paste()
                details_nav.confirm_and_close()
            if row_index < len(self._data_rows) - 1:
                self._main_nav.move_next_row_start()
        pass
