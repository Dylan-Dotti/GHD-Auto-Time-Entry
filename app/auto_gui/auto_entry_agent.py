import time
from app.auto_gui.keyboard_controller import KeyboardController
from app.auto_gui.sap_main_window_navigator import SapMainWindowNavigator
from app.data_formatter.SAP_Objects.sap_data_row import SapDataRow
from app.interfaces.threadsafe_stoppable_w_subcomponents import ThreadSafeStoppableWithSubComponents
from app.option_preferences.column_layout.sap_column_layout import SapColumnLayout
from pandas.io.clipboard import copy, paste
from typing import List

class AutoEntryAgent(ThreadSafeStoppableWithSubComponents):

    def __init__(self, main_kc: KeyboardController,
                 main_nav: SapMainWindowNavigator,
                 data_rows: List[SapDataRow],
                 column_layout: SapColumnLayout) -> None:
        super().__init__()
        self._main_kc = main_kc
        self._main_nav = main_nav
        self._data_rows = data_rows
        self._column_layout = column_layout

    def execute(self, clear_data = False) -> None:
        self.clear_subcomponents()
        self.add_stoppable_subcomponent(self._main_kc)
        self.add_stoppable_subcomponent(self._main_nav)
        self._stop_requested = False
        # Clear data if requested, else move to first empty line
        if clear_data:
            self._main_nav.delete_all_entries()
        else:
            self._main_nav.move_first_empty_row()
        # Loop through rows
        for row_index, row in enumerate(self._data_rows):
            if self._stop_requested:
                self._on_stop_request_acknowledge()
            # Paste row data
            copy(row.to_sap_str_dynamic(self._column_layout))
            time.sleep(.05)
            self._main_kc.press_paste(post_delay=.2)
            self._main_kc.press_enter(post_delay=.5)
            # Move through cells and input notes
            verified_alignment = False
            for day_index in self._column_layout.get_day_index_list():
                entry = row.date_entries[day_index]
                if entry is not None:
                    # move to day in grid, verify alignment if needed
                    expected_data = None if verified_alignment else entry.time
                    if expected_data is not None:
                        verified_alignment = True
                    self._main_nav.move_to_day(day_index, expected_data=expected_data)
                    # open details window and paste note
                    details_nav, details_kc = self._main_nav.open_cell_details()
                    self.add_stoppable_subcomponent(details_nav)
                    copy(entry.note)
                    details_nav.move_to_short_text_field()
                    details_kc.press_paste(post_delay=.2)
                    details_nav.confirm_and_close()
                    self.remove_stoppable_subcomponent(details_nav)
            if row_index < len(self._data_rows) - 1:
                self._main_nav.move_next_row_start()
    
    def stop(self):
        print('Stopping AutoEntryAgent...')
        ThreadSafeStoppableWithSubComponents.stop(self)
    
    def _clear_data(self) -> None:
        reset_nav, _ = self._main_nav.open_reset_entries()
        reset_nav.select_yes()

