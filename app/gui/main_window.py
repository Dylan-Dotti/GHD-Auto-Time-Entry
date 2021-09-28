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
        self.run_button.clicked.connect(self.run_button_clicked)
        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle('Error!')
        self.error_dialog.setIcon(QMessageBox.Critical)
        self.error_dialog.setStandardButtons(QMessageBox.Ok)

    def select_data_button_clicked(self):
        file_name = self._open_file_selector()
        if file_name: # if valid file is selected
            self.selected_file_label.setText(file_name)
            self.username_selector.setEnabled(True)
            self.week_selector.setEnabled(True)

            name_and_month_reader = ZendeskDataReader(file_name)
            name_and_month_reader.load_wb()
            self.username_selector.clear()
            self.username_selector.addItems(name_and_month_reader.get_users())

            d_min, d_max = name_and_month_reader.get_dates()
            self.week_selector.clear()
            self.week_selector.addItems([i.strftime('%m/%d/%Y') +" - "+ j.strftime('%m/%d/%Y') for i,j in date_ranges(d_min.month)])

            self.run_button.setEnabled(True)

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
