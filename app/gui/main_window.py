import traceback
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox, QDialog
from pathlib import Path
from app.integration.auto_entry_main import AutoEntryMain
from app.data_formatter.readers.zendesk.zendesk_data_reader import ZendeskDataReader
from app.gui.main_window_base import Ui_MainWindow
from app.gui.configure_columns_window import ConfigureColumnsWindow
from app.option_preferences.option_prefs import OptionPrefs

'''
    Extends Ui_MainWindow to provide custom functionality
    Ui_Main_Window overwrites any changes when rebuilt
'''


class MainWindowFunctional(Ui_MainWindow):
    _not_running_message = 'Not running'

    def __init__(self, option_prefs: OptionPrefs = None) -> None:
        super().__init__()
        self._option_prefs = option_prefs
        self.auto_entry_thread = None
        self.auto_entry_worker = None
        self.reader = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        # set window icon
        icon_path = str(Path(__file__).parent / "red_clock_z0x_2.ico")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        # initialize error window
        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle('Error!')
        self.error_dialog.setIcon(QMessageBox.Critical)
        self.error_dialog.setStandardButtons(QMessageBox.Ok)

        # initialize configure columns dialog
        self._configure_cols_dialog = ConfigureColumnsWindow(
            self._option_prefs.column_layout if self._option_prefs else None)

        # setup GUI prefs where possible
        if self._option_prefs is not None:
            if self._option_prefs.num_sap_rows is not None:
                self.rows_per_page_box.setValue(
                    self._option_prefs.num_sap_rows)
            if self._option_prefs.use_fn_button is not None:
                self.use_fn_checkbox.setChecked(
                    self._option_prefs.use_fn_button)

        # connect events
        self.select_data_button.clicked.connect(
            self.select_data_button_clicked)
        self.username_selector.currentIndexChanged.connect(
            self.username_changed)
        self.configure_columns_button.clicked.connect(
            self.configure_columns_clicked)
        self.run_button.clicked.connect(self.run_button_clicked)
        self.stop_button.clicked.connect(self.stop_button_clicked)

    def select_data_button_clicked(self):
        try:
            file_path = self._open_file_selector()
            # if valid file name selected
            if file_path:
                self._option_prefs.data_directory = str(Path(file_path).parent)
                self.reset_file_selector()
                self.selected_file_label.setText(file_path)
                self.reader = ZendeskDataReader(file_path)
                self.reader.load_wb()
                self.set_username_selector()
                self.username_selector.setEnabled(True)
                self.week_selector.setEnabled(True)
                self.run_button.setEnabled(True)
        except Exception as ex:
            print(traceback.format_exc())
            self._show_error_popup(str(ex))

    def reset_file_selector(self):
        if self.reader:
            self.reader = None
            self.username_selector.clear()
            self.week_selector.clear()

    def set_username_selector(self):
        self.username_selector.addItems(self.reader.get_users())
        if self._option_prefs.name:
            self.username_selector.setCurrentIndex(
                self.reader.get_users().index(self._option_prefs.name))

    def username_changed(self):
        # need this because this is triggered when the selector is cleared as well
        if self.reader:
            username = self.username_selector.currentText()
            self.week_selector.clear()
            self.set_week_selector(username)

    def set_week_selector(self, username):
        weeks = self.reader.get_weeks_with_data(username)
        self.week_selector.addItems([start.strftime(
            '%m/%d/%Y') + " - " + end.strftime('%m/%d/%Y') for start, end in sorted(list(weeks))])

    def configure_columns_clicked(self):
        self._configure_cols_dialog.show_as_dialog()

    def run_button_clicked(self):
        print('Running Auto Entry...')
        self._set_configure_controls_enabled(False)
        self.run_button.setEnabled(False)

        # if a user is running the app w/ a name, they probably want that name to be the default
        self._option_prefs.name = self.username_selector.currentText()
        self._option_prefs.num_sap_rows = self.rows_per_page_box.value()
        self._option_prefs.use_fn_button = self.use_fn_checkbox.isChecked()

        self.auto_entry_thread = QThread()
        self.auto_entry_worker = AutoEntryMain(
            self.selected_file_label.text(),
            self.username_selector.currentText(),
            self.clear_data_checkbox.isChecked(),
            self.use_fn_checkbox.isChecked(),
            self.week_selector.currentText(),
            self.rows_per_page_box.value())

        self.auto_entry_worker.moveToThread(self.auto_entry_thread)
        self.auto_entry_thread.started.connect(self.auto_entry_worker.run)
        self.auto_entry_thread.finished.connect(
            self.auto_entry_thread.deleteLater)
        self.auto_entry_worker.started_signal.connect(
            self._on_auto_entry_started)
        self.auto_entry_worker.finished_signal.connect(
            self.auto_entry_thread.quit)
        self.auto_entry_worker.finished_signal.connect(
            self.auto_entry_worker.deleteLater)
        self.auto_entry_worker.finished_signal.connect(
            self._on_auto_entry_finished)
        self.auto_entry_worker.exception_signal.connect(
            self._on_auto_entry_exception)
        self.auto_entry_thread.start()

        self.stop_button.setEnabled(True)

    def stop_button_clicked(self):
        self.stop_button.setEnabled(False)
        self._publish_status_message('Stopping...')
        self.auto_entry_worker.stop()

    def _on_auto_entry_started(self):
        self._publish_status_message('Running')

    def _on_auto_entry_finished(self):
        self._publish_status_message(MainWindowFunctional._not_running_message)
        self._set_configure_controls_enabled(True)
        self.stop_button.setEnabled(False)
        self.run_button.setEnabled(True)
        print('Auto Entry finished')

    def _on_auto_entry_exception(self, ex: Exception):
        self._show_error_popup(str(ex))

    def _open_file_selector(self):
        base_dir = str(("" if not self._option_prefs or
                        not self._option_prefs.data_directory else
                        self._option_prefs.data_directory))
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Zendesk Data", base_dir, "Excel Files (*.xlsx)")
        return str(fileName)

    def _show_error_popup(self, msg: str):
        self.error_dialog.setText(msg)
        self.error_dialog.exec()

    def _publish_status_message(self, message: str):
        self.status_label.setText(message)
        self.status_label.setEnabled(
            message != MainWindowFunctional._not_running_message)

    def _set_configure_controls_enabled(self, enabled: bool):
        self.select_data_button.setEnabled(enabled)
        self.username_selector.setEnabled(enabled)
        self.week_selector.setEnabled(enabled)
        self.rows_per_page_box.setEnabled(enabled)
        self.clear_data_checkbox.setEnabled(enabled)
        self.use_fn_checkbox.setEnabled(enabled)


def launch_window(option_prefs: OptionPrefs = None):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowFunctional(option_prefs=option_prefs)
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()


if __name__ == "__main__":
    launch_window()
