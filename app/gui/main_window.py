from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from main_window_base import Ui_MainWindow
from app.auto_entry_main import AutoEntryMain
from app.data_formatter.utils import date_ranges
from datetime import date
from app.data_formatter.readers.zendesk.zendesk_data_reader import ZendeskDataReader

'''
    Extends Ui_MainWindow to provide custom functionality
    Ui_Main_Window overwrites any changes when rebuilt
'''
class MainWindowFunctional(Ui_MainWindow):
    _not_running_message = 'App is not running'

    _stop_signal = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.auto_entry_thread = None
        self.auto_entry_worker = None
        self.reader = None
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.select_data_button.clicked.connect(self.select_data_button_clicked)
        self.username_selector.currentIndexChanged.connect(self.username_changed)
        self.run_button.clicked.connect(self.run_button_clicked)
        self.stop_button.clicked.connect(self.stop_button_clicked)

    def select_data_button_clicked(self):
        file_name = self._open_file_selector()
        
        # if valid file name selected
        if file_name:
            
            self.reset_file_selector()
            self.selected_file_label.setText(file_name)

            self.username_selector.setEnabled(True)
            self.week_selector.setEnabled(True)

            self.reader = ZendeskDataReader(file_name)
            self.reader.load_wb()

            self.set_username_selector()

            self.run_button.setEnabled(True)

        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle('Error!')
        self.error_dialog.setIcon(QMessageBox.Critical)
        self.error_dialog.setStandardButtons(QMessageBox.Ok)

    def reset_file_selector(self):
        if self.reader:
            self.reader = None
            self.username_selector.clear()
            self.week_selector.clear()

    def set_username_selector(self):  
        self.username_selector.addItems(self.reader.get_users())

    def username_changed(self):
        # need this because this is triggered when the selector is cleared as well
        if self.reader:
            username = self.username_selector.currentText()
            self.week_selector.clear()
            self.set_week_selector(username)

    def set_week_selector(self, username):
        weeks = self.reader.get_weeks_with_data(username)
        self.week_selector.addItems([start.strftime('%m/%d/%Y') +" - "+ end.strftime('%m/%d/%Y') for start, end in sorted(list(weeks))])

    def run_button_clicked(self):
        print('Running Auto Entry...')
        self.run_button.setEnabled(False)

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
        self.auto_entry_thread.finished.connect(self.auto_entry_thread.deleteLater)
        self.auto_entry_worker.started_signal.connect(self._on_auto_entry_started)
        self.auto_entry_worker.finished_signal.connect(self.auto_entry_thread.quit)
        self.auto_entry_worker.finished_signal.connect(self.auto_entry_worker.deleteLater)
        self.auto_entry_worker.finished_signal.connect(self._on_auto_entry_finished)
        self.auto_entry_worker.exception_signal.connect(self._on_auto_entry_exception)
        self.auto_entry_thread.start()

        self.stop_button.setEnabled(True)
    
    def stop_button_clicked(self):
        self.auto_entry_worker.stop()
    
    def _on_auto_entry_started(self):
        self._publish_status_message('App is running')
    
    def _on_auto_entry_finished(self):
        self._publish_status_message(MainWindowFunctional._not_running_message)
        self.stop_button.setEnabled(False)
        self.run_button.setEnabled(True)
        print('Auto Entry finished')
    
    def _on_auto_entry_exception(self, ex: Exception):
        print(ex)
        self._show_error_popup(str(ex))

    def _open_file_selector(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Zendesk Data", "","Excel Files (*.xlsx)")
        return fileName

    def _show_error_popup(self, msg: str):
        self.error_dialog.setText(msg)
        self.error_dialog.exec()

    def _publish_status_message(self, message: str):
        self.status_label.setText(message)
        self.status_label.setEnabled(
            message != MainWindowFunctional._not_running_message)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowFunctional()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
