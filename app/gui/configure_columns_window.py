from typing import Callable
from app.gui.configure_columns_base import Ui_Dialog
from app.option_preferences.column_layout.sap_column import SapColumn
from app.option_preferences.column_layout.sap_column_layout import SapColumnLayout
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QListWidgetItem


class ConfigureColumnsWindow(Ui_Dialog):

    def __init__(self, column_layout: SapColumnLayout = None,
                 on_layout_changed: Callable[[SapColumnLayout], None] = None) -> None:
        super().__init__()
        self._column_layout = column_layout
        self._item_index_tuples = []
        self._on_layout_changed = on_layout_changed

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.buttonBox.accepted.connect(self._save_column_layout)
        self.set_column_layout(self._column_layout if self._column_layout else 
                               SapColumnLayout.from_default_layout())
    
    def show_as_dialog(self):
        dialog = QDialog()
        dialog.ui = self
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.show()
        dialog.exec_()
    
    def get_column_layout(self) -> SapColumnLayout:
        return self._column_layout
    
    def set_column_layout(self, clayout: SapColumnLayout) -> None:
        self._column_layout = clayout
        self.configure_columns_list.clear()
        self._item_index_tuples.clear()
        for col in clayout.get_current_layout():
            item = QListWidgetItem()
            item.setText(col.column_name)
            item.setCheckState(2 if col.visible else 0)
            self.configure_columns_list.addItem(item)
            self._item_index_tuples.append((item, self.configure_columns_list.count() - 1))
    
    def _save_column_layout(self):
        print('Saving column layout preferences...')
        new_columns = []
        current_columns = self._column_layout.get_current_layout()
        for i in range(self.configure_columns_list.count()):
            list_item = self.configure_columns_list.item(i)
            item_index = self._item_index_tuples.index(
                next(filter(lambda x: x[0] == list_item, self._item_index_tuples)))
            current_col = current_columns[item_index]
            current_col.visible = list_item.checkState() != 0
            new_columns.append(current_col)
        self._column_layout = SapColumnLayout(new_columns)
        if self._on_layout_changed:
            self._on_layout_changed(self._column_layout)

