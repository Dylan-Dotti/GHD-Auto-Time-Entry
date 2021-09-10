from typing import Tuple
from PyQt5 import QtWidgets
from main_window_base import Ui_MainWindow
from app.app_main import AppMain

'''
    Extends Ui_MainWindow to provide custom functionality
    Ui_Main_Window overwrites any changes when rebuilt
'''
class MainWindowFunctional(Ui_MainWindow):
    _not_running_message = 'App is not running'
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.select_data_button.clicked.connect(self.select_data_button_clicked)
        self.username_input.textChanged.connect(self.username_changed)
        self.run_button.clicked.connect(self.run_button_clicked)
    
    def select_data_button_clicked(self):
        file_name = self.openFileNameDialog()
        if file_name:
            self.selected_file_label.setText(file_name)
            self.run_button.setEnabled(True)
    
    def username_changed(self):
        valid, reason = self._is_input_valid_w_reason()
        if valid:
            self.run_button.setEnabled(True)
            self._publish_status_message(
                MainWindowFunctional._not_running_message)
        else:
            self.run_button.setEnabled(False)
            self._publish_status_message(reason)

    def run_button_clicked(self):
        print('Running app')
        AppMain(self.selected_file_label.text(),
                self.username_input.text(),
                self.clear_data_checkbox.isChecked(),
                self.use_fn_checkbox.isChecked()).execute()

    def openFileNameDialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Zendesk Data", "","Excel Files (*.xlsx)")
        return fileName
    
    def _publish_status_message(self, message: str):
        self.status_label.setText(message)
        self.status_label.setEnabled(message != 'App is not running')
    
    def _is_input_valid_w_reason(self) -> Tuple[bool, str]:
        username = self.username_input.text()
        if len(username) == 0:
            return False, 'Username can\'t be empty'
        username_spaces = [c == ' ' for c in username]
        if all(username_spaces):
            return False, 'Username can\'t be all spaces'
        return True, None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowFunctional()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
