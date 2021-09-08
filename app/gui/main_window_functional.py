from PyQt5 import QtWidgets
from main_window_base import Ui_MainWindow
from app.app_main import AppMain

'''
    Extends Ui_MainWindow to provide custom functionality
    Ui_Main_Window overwrites any changes when rebuilt
'''
class MainWindowFunctional(Ui_MainWindow):
    
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.select_data_button.clicked.connect(self.select_data_button_clicked)
        self.run_button.clicked.connect(self.run_button_clicked)
    
    def select_data_button_clicked(self):
        file_name = self.openFileNameDialog()
        if file_name:
            self.selected_file_label.setText(file_name)
            self.run_button.setEnabled(True)

    def run_button_clicked(self):
        print('Running app')
        AppMain(self.selected_file_label.text(),
                'Dylan Dotti', False, True).execute()

    
    def openFileNameDialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Zendesk Data", "","Excel Files (*.xlsx)")
        return fileName


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowFunctional()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
