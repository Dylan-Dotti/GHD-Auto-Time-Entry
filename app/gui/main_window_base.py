# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 369)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_data_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_data_button.sizePolicy().hasHeightForWidth())
        self.select_data_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.select_data_button.setFont(font)
        self.select_data_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.select_data_button.setStyleSheet("padding: 7px 12px;\n"
"margin: 5px;\n"
"margin-right: 0px;\n"
"")
        self.select_data_button.setObjectName("select_data_button")
        self.horizontalLayout.addWidget(self.select_data_button, 0, QtCore.Qt.AlignVCenter)
        self.selected_file_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_file_label.sizePolicy().hasHeightForWidth())
        self.selected_file_label.setSizePolicy(sizePolicy)
        self.selected_file_label.setStyleSheet("padding: 10px 10px 10px 0px;\n"
"")
        self.selected_file_label.setScaledContents(True)
        self.selected_file_label.setWordWrap(True)
        self.selected_file_label.setObjectName("selected_file_label")
        self.horizontalLayout.addWidget(self.selected_file_label, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("margin-left: 5px")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.username_selector = QtWidgets.QComboBox(self.groupBox)
        self.username_selector.setEnabled(False)
        self.username_selector.setMinimumSize(QtCore.QSize(150, 0))
        self.username_selector.setStyleSheet("padding: 5px\n"
"")
        self.username_selector.setObjectName("username_selector")
        self.horizontalLayout_3.addWidget(self.username_selector)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet("margin-left: 5px")
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.week_selector = QtWidgets.QComboBox(self.groupBox)
        self.week_selector.setEnabled(False)
        self.week_selector.setMinimumSize(QtCore.QSize(250, 0))
        self.week_selector.setStyleSheet("padding: 5px")
        self.week_selector.setObjectName("week_selector")
        self.horizontalLayout_7.addWidget(self.week_selector)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("padding-left: 5px")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft)
        self.rows_per_page_box = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rows_per_page_box.sizePolicy().hasHeightForWidth())
        self.rows_per_page_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rows_per_page_box.setFont(font)
        self.rows_per_page_box.setStyleSheet("padding: 2px 5px")
        self.rows_per_page_box.setProperty("value", 8)
        self.rows_per_page_box.setObjectName("rows_per_page_box")
        self.horizontalLayout_5.addWidget(self.rows_per_page_box, 0, QtCore.Qt.AlignLeft)
        self.configure_columns_button = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.configure_columns_button.setFont(font)
        self.configure_columns_button.setStyleSheet("padding: 6px 15px;\n"
"margin-left: 20px")
        self.configure_columns_button.setObjectName("configure_columns_button")
        self.horizontalLayout_5.addWidget(self.configure_columns_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clear_data_checkbox = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_data_checkbox.sizePolicy().hasHeightForWidth())
        self.clear_data_checkbox.setSizePolicy(sizePolicy)
        self.clear_data_checkbox.setStyleSheet("margin: 8px;\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 12px;\n"
"     height: 12px;\n"
" }")
        self.clear_data_checkbox.setTristate(False)
        self.clear_data_checkbox.setObjectName("clear_data_checkbox")
        self.horizontalLayout_2.addWidget(self.clear_data_checkbox, 0, QtCore.Qt.AlignVCenter)
        self.use_fn_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.use_fn_checkbox.setStyleSheet("margin: 8px;\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 12px;\n"
"     height: 12px;\n"
" }")
        self.use_fn_checkbox.setObjectName("use_fn_checkbox")
        self.horizontalLayout_2.addWidget(self.use_fn_checkbox, 0, QtCore.Qt.AlignVCenter)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setStyleSheet("margin-left: 2px")
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_4.addWidget(self.status_label)
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy)
        self.run_button.setMinimumSize(QtCore.QSize(150, 25))
        self.run_button.setStyleSheet("padding: 10px 50px")
        self.run_button.setObjectName("run_button")
        self.horizontalLayout_4.addWidget(self.run_button, 0, QtCore.Qt.AlignVCenter)
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setMinimumSize(QtCore.QSize(150, 25))
        self.stop_button.setStyleSheet("padding: 10px 50px")
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_4.addWidget(self.stop_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.select_data_button, self.clear_data_checkbox)
        MainWindow.setTabOrder(self.clear_data_checkbox, self.use_fn_checkbox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GHD Auto Time Entry"))
        self.groupBox.setTitle(_translate("MainWindow", "Configure"))
        self.select_data_button.setText(_translate("MainWindow", "Select Time Data"))
        self.selected_file_label.setText(_translate("MainWindow", "No file selected"))
        self.label.setText(_translate("MainWindow", "Select Name:"))
        self.label_2.setText(_translate("MainWindow", "Select Week:"))
        self.label_3.setText(_translate("MainWindow", "Rows per Page:"))
        self.configure_columns_button.setText(_translate("MainWindow", "Configure Columns"))
        self.clear_data_checkbox.setText(_translate("MainWindow", "Clear Existing Data"))
        self.use_fn_checkbox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Some computers need to press the \'Fn\' button in order to use the F keys (F1-F12)</p></body></html>"))
        self.use_fn_checkbox.setText(_translate("MainWindow", "Use Fn Button"))
        self.status_label.setText(_translate("MainWindow", "Not running"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
