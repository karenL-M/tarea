# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\complex.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-20, 0, 481, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 461, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 461, 271))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.verticalLayoutWidget_2)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_4)
        self.dateEdit.setGeometry(QtCore.QRect(10, 10, 431, 22))
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName("dateEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 40, 431, 211))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 121, 111))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 30, 84, 65))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_start = QtWidgets.QRadioButton(self.widget)
        self.radioButton_start.setChecked(True)
        self.radioButton_start.setObjectName("radioButton_start")
        self.verticalLayout_3.addWidget(self.radioButton_start)
        self.radioButton_stop = QtWidgets.QRadioButton(self.widget)
        self.radioButton_stop.setObjectName("radioButton_stop")
        self.verticalLayout_3.addWidget(self.radioButton_stop)
        self.radioButton_reset = QtWidgets.QRadioButton(self.widget)
        self.radioButton_reset.setObjectName("radioButton_reset")
        self.verticalLayout_3.addWidget(self.radioButton_reset)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 10, 241, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.dial = QtWidgets.QDial(self.groupBox_2)
        self.dial.setGeometry(QtCore.QRect(10, 30, 91, 101))
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setGeometry(QtCore.QRect(130, 40, 101, 71))
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(40, 250, 421, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.fontComboBox = QtWidgets.QFontComboBox(self.tab_2)
        self.fontComboBox.setGeometry(QtCore.QRect(40, 150, 181, 16))
        self.fontComboBox.setObjectName("fontComboBox")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(40, 170, 181, 61))
        self.label.setText("")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        self.dial.valueChanged['int'].connect(self.lcdNumber.display)
        self.fontComboBox.activated['QString'].connect(self.label.setText)
        self.radioButton_reset.clicked.connect(self.reset_progressbar)
        self.fontComboBox.activated['QString'].connect(self.label.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Header 1"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "New Column"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tree"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Calendar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Widgets1"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.radioButton_start.setText(_translate("MainWindow", "Start"))
        self.radioButton_stop.setText(_translate("MainWindow", "Stop"))
        self.radioButton_reset.setStatusTip(_translate("MainWindow", "This is Option 2"))
        self.radioButton_reset.setText(_translate("MainWindow", "Reset"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Widgets 2"))


    def reset_progressbar(self):
        self.progressBar.reset
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())