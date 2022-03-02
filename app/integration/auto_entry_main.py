from app.interfaces.threadsafe_stoppable_w_subcomponents import ThreadSafeStoppableWithSubComponents
from app.interfaces.stop_requested_error import StopRequestedError
from typing import List
import app.auto_gui.window_names as win_names
import traceback
from app.auto_gui.keyboard_controller import KeyboardController
from app.auto_gui.sap_main_window_navigator import SapMainWindowNavigator
from app.auto_gui.auto_entry_agent import AutoEntryAgent
from app.auto_gui.window_controller import WindowController
from app.data_formatter.readers.zendesk.zendesk_data_reader import ZendeskDataReader
from app.data_formatter.formatters.data_formatter_factory import DataFormatterFactory
from datetime import date
from PyQt5.QtCore import QObject, pyqtSignal

from app.option_preferences.column_layout.sap_column_layout import SapColumnLayout


class AutoEntryMain(QObject, ThreadSafeStoppableWithSubComponents):
    started_signal = pyqtSignal()
    finished_signal = pyqtSignal()
    exception_signal = pyqtSignal(Exception)

    def __init__(self, zendesk_excel_path: str, user_name: str,
                 clear_existing_data: bool, use_fn_key: bool, selected_week: str,
                 num_sap_rows_per_page: int, column_layout: SapColumnLayout,
                 speed: float) -> None:
        super().__init__()
        self._zendesk_excel_path = zendesk_excel_path
        self._user_name = user_name
        self._num_sap_rows_per_page = num_sap_rows_per_page
        self._clear_existing_data = clear_existing_data
        self._use_fn_key = use_fn_key
        self.st, self.ed = selected_week.split(" - ")
        self._column_layout = column_layout
        self._speed = speed

    def run(self):
        self.started_signal.emit()
        try:
            # data formatting
            zendesk_reader = ZendeskDataReader(self._zendesk_excel_path)
            zendesk_reader.load_wb()
            zendesk_rows = zendesk_reader.read_all_rows()

            # get a formatter
            formatter_factory = DataFormatterFactory()
            data_formatter = formatter_factory.get_formatter('ZENDESK')
            # create pages for a provided month

            # ***Needs to be changed to use the month of the selected sheet**
            start_month = int(self.st.split('/')[0])
            end_month = int(self.ed.split('/')[0])
            try:
                pages = data_formatter.create_pages(start_month)
            except:
                pages = data_formatter.create_pages(end_month)

            # create a new formatter instance with the test data
            zdt_formatter = data_formatter(self._user_name, zendesk_rows, pages)
            # format zendesk data to SAP
            zdt_formatter.format()

            # get SAP pages
            # formatted_data = zdt_formatter.formatted_data()
            sap_rows = zdt_formatter.get_page(self.st, self.ed).data
            if len(sap_rows) == 0:
                raise Exception('No results were produced for the configured settings.')
            sap_rows = sorted(sap_rows)

            # auto entry
            self.clear_subcomponents()

            # main_wc = wc_factory.get_sap_main_window_controller()
            main_wc = WindowController()
            self.add_stoppable_subcomponent(main_wc)
            main_wc.bind_to_window(win_names.MAIN_WINDOW_NAMES)
            self.remove_stoppable_subcomponent(main_wc)

            main_kc = KeyboardController(main_wc, use_fn_key=self._use_fn_key)
            main_nav = SapMainWindowNavigator(main_kc, self._num_sap_rows_per_page,
                                              self._column_layout)
            entry_agent = AutoEntryAgent(main_kc, main_nav, sap_rows, self._column_layout)
            self.add_stoppable_subcomponent(entry_agent)

            main_wc.set_window_foreground()
            entry_agent.execute(self._clear_existing_data)
        
        except StopRequestedError:
            self._stop_requested = False
            print('AutoEntryMain stopped')

        except Exception as ex:
            print(traceback.format_exc())
            self.exception_signal.emit(ex)

        print('AutoEntryMain finished')
        self.finished_signal.emit()
    
    def stop(self):
        print('Stopping AutoEntryMain...')
        ThreadSafeStoppableWithSubComponents.stop(self)