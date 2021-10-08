from app.gui.configure_columns_base import Ui_Dialog
from PyQt5 import QtWidgets


class ConfigureColumnsWindow(Ui_Dialog):

    def __init__(self) -> None:
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)


def launch_window():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ConfigureColumnsWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
