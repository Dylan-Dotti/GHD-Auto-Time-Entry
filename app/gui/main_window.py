from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from main_window_base import Ui_MainWindow
from app.app_main import AppMain
from app.data_formatter.utils import date_ranges
from datetime import date
from app.data_formatter.readers.zendesk.zendesk_data_reader import ZendeskDataReader

'''
    Extends Ui_MainWindow to provide custom functionality
    Ui_Main_Window overwrites any changes when rebuilt
'''
class MainWindowFunctional(Ui_MainWindow):
    _not_running_message = 'App is not running'
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.select_data_button.clicked.connect(self.select_data_button_clicked)
        self.username_selector.currentIndexChanged.connect(self.username_changed)
        self.run_button.clicked.connect(self.run_button_clicked)
        # self.week_selector.activated.connect(self.week_changed)
        self.reader = None

    def select_data_button_clicked(self):


        file_name = self._open_file_selector()

        if file_name: # if valid file is selected
            self.reset_file_selector()
            self.selected_file_label.setText(file_name)
            self.username_selector.setEnabled(True)
            self.week_selector.setEnabled(True)

            # set the username dropdown here..? 
            self.reader = ZendeskDataReader(file_name)
            self.reader.load_wb()

            self.set_username_selector()
            # self.set_week_selector(self.username_selector.currentText())

            self.run_button.setEnabled(True)

        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle('Error!')
        self.error_dialog.setIcon(QMessageBox.Critical)
        self.error_dialog.setStandardButtons(QMessageBox.Ok)

    def reset_file_selector(self):
        if self.reader:
            print("I RAN")
            self.reader = None
            self.username_selector.clear()
            self.week_selector.clear()

    def username_changed(self):
        # need this because this is triggered when the selector is cleared as well
        if self.reader:
            username = self.username_selector.currentText()
            self.week_selector.clear()
            self.set_week_selector(username)

        # valid, reason = self._is_input_valid_w_reason()
        # if valid:
        #     self.run_button.setEnabled(True)
        #     self._publish_status_message(
        #         MainWindowFunctional._not_running_message)
        # else:
        #     self.run_button.setEnabled(False)
        #     self._publish_status_message(reason)

    def set_week_selector(self, username):
        weeks = self.reader.get_weeks_with_data(username)
        self.week_selector.addItems([start.strftime('%m/%d/%Y') +" - "+ end.strftime('%m/%d/%Y') for start, end in sorted(list(weeks))])


    def set_username_selector(self):  
        self.username_selector.addItems(self.reader.get_users())

    def run_button_clicked(self):
        print('Running app')
        self._publish_status_message('App is running')
        try:
            AppMain(self.selected_file_label.text(),
                    self.username_selector.currentText(),
                    self.clear_data_checkbox.isChecked(),
                    self.use_fn_checkbox.isChecked(),
                    self.week_selector.currentText()).execute()
        except Exception as ex:
            print(ex)
            self._show_error_popup(str(ex))
        self._publish_status_message(MainWindowFunctional._not_running_message)

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
