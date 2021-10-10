from app.gui.configure_columns_base import Ui_Dialog
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog


class ConfigureColumnsWindow(Ui_Dialog):

    def __init__(self) -> None:
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
    
    def show_as_dialog(self):
        dialog = QDialog()
        dialog.ui = self
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.show()
        dialog.exec_()
