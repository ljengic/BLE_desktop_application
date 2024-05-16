# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './package/main_app/gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_screen = QtWidgets.QWidget(self.centralwidget)
        self.main_screen.setObjectName("main_screen")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_screen)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.status_bar = QtWidgets.QFrame(self.main_screen)
        self.status_bar.setFrameShape(QtWidgets.QFrame.Box)
        self.status_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status_bar.setLineWidth(1)
        self.status_bar.setObjectName("status_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.status_bar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_menu = QtWidgets.QPushButton(self.status_bar)
        self.btn_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-menu-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(25, 25))
        self.btn_menu.setCheckable(True)
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout.addWidget(self.btn_menu)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_screen_name = QtWidgets.QLabel(self.status_bar)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_screen_name.setFont(font)
        self.label_screen_name.setObjectName("label_screen_name")
        self.horizontalLayout.addWidget(self.label_screen_name)
        spacerItem1 = QtWidgets.QSpacerItem(609, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.status_bar)
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_screen)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.status_bar_2 = QtWidgets.QFrame(self.main_screen)
        self.status_bar_2.setFrameShape(QtWidgets.QFrame.Box)
        self.status_bar_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status_bar_2.setLineWidth(0)
        self.status_bar_2.setObjectName("status_bar_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.status_bar_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(609, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.status_bar_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/WhatsApp Image 2024-05-07 at 18.46.40 (1).jpeg"))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.status_bar_2)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/WhatsApp Image 2024-05-07 at 18.48.55.jpeg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_5.addWidget(self.status_bar_2)
        self.gridLayout.addWidget(self.main_screen, 0, 2, 1, 1)
        self.menu_full = QtWidgets.QFrame(self.centralwidget)
        self.menu_full.setMinimumSize(QtCore.QSize(250, 0))
        self.menu_full.setFrameShape(QtWidgets.QFrame.Box)
        self.menu_full.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_full.setLineWidth(1)
        self.menu_full.setObjectName("menu_full")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menu_full)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_home_2 = QtWidgets.QPushButton(self.menu_full)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_home_2.setFont(font)
        self.btn_home_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-home-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home_2.setIcon(icon1)
        self.btn_home_2.setIconSize(QtCore.QSize(50, 50))
        self.btn_home_2.setCheckable(True)
        self.btn_home_2.setAutoExclusive(True)
        self.btn_home_2.setObjectName("btn_home_2")
        self.verticalLayout_3.addWidget(self.btn_home_2)
        self.btn_ble_2 = QtWidgets.QPushButton(self.menu_full)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_ble_2.setFont(font)
        self.btn_ble_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-bluetooth-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ble_2.setIcon(icon2)
        self.btn_ble_2.setIconSize(QtCore.QSize(50, 50))
        self.btn_ble_2.setCheckable(True)
        self.btn_ble_2.setAutoExclusive(True)
        self.btn_ble_2.setObjectName("btn_ble_2")
        self.verticalLayout_3.addWidget(self.btn_ble_2)
        self.btn_start_2 = QtWidgets.QPushButton(self.menu_full)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_start_2.setFont(font)
        self.btn_start_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-start-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_start_2.setIcon(icon3)
        self.btn_start_2.setIconSize(QtCore.QSize(50, 50))
        self.btn_start_2.setCheckable(True)
        self.btn_start_2.setAutoExclusive(True)
        self.btn_start_2.setObjectName("btn_start_2")
        self.verticalLayout_3.addWidget(self.btn_start_2)
        self.btn_results_2 = QtWidgets.QPushButton(self.menu_full)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_results_2.setFont(font)
        self.btn_results_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-result-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_results_2.setIcon(icon4)
        self.btn_results_2.setIconSize(QtCore.QSize(50, 50))
        self.btn_results_2.setCheckable(True)
        self.btn_results_2.setAutoExclusive(True)
        self.btn_results_2.setObjectName("btn_results_2")
        self.verticalLayout_3.addWidget(self.btn_results_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 513, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.btn_exit_2 = QtWidgets.QPushButton(self.menu_full)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_exit_2.setFont(font)
        self.btn_exit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-close-120.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit_2.setIcon(icon5)
        self.btn_exit_2.setIconSize(QtCore.QSize(50, 50))
        self.btn_exit_2.setCheckable(True)
        self.btn_exit_2.setAutoExclusive(True)
        self.btn_exit_2.setObjectName("btn_exit_2")
        self.verticalLayout_4.addWidget(self.btn_exit_2)
        self.gridLayout.addWidget(self.menu_full, 0, 1, 1, 1)
        self.menu_icons_only = QtWidgets.QFrame(self.centralwidget)
        self.menu_icons_only.setFrameShape(QtWidgets.QFrame.Box)
        self.menu_icons_only.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_icons_only.setLineWidth(1)
        self.menu_icons_only.setObjectName("menu_icons_only")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_icons_only)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_home_1 = QtWidgets.QPushButton(self.menu_icons_only)
        self.btn_home_1.setText("")
        self.btn_home_1.setIcon(icon1)
        self.btn_home_1.setIconSize(QtCore.QSize(50, 50))
        self.btn_home_1.setCheckable(True)
        self.btn_home_1.setAutoExclusive(True)
        self.btn_home_1.setObjectName("btn_home_1")
        self.verticalLayout.addWidget(self.btn_home_1)
        self.btn_ble_1 = QtWidgets.QPushButton(self.menu_icons_only)
        self.btn_ble_1.setText("")
        self.btn_ble_1.setIcon(icon2)
        self.btn_ble_1.setIconSize(QtCore.QSize(50, 50))
        self.btn_ble_1.setCheckable(True)
        self.btn_ble_1.setAutoExclusive(True)
        self.btn_ble_1.setObjectName("btn_ble_1")
        self.verticalLayout.addWidget(self.btn_ble_1)
        self.btn_start_1 = QtWidgets.QPushButton(self.menu_icons_only)
        self.btn_start_1.setText("")
        self.btn_start_1.setIcon(icon3)
        self.btn_start_1.setIconSize(QtCore.QSize(50, 50))
        self.btn_start_1.setCheckable(True)
        self.btn_start_1.setAutoExclusive(True)
        self.btn_start_1.setObjectName("btn_start_1")
        self.verticalLayout.addWidget(self.btn_start_1)
        self.btn_results_1 = QtWidgets.QPushButton(self.menu_icons_only)
        self.btn_results_1.setText("")
        self.btn_results_1.setIcon(icon4)
        self.btn_results_1.setIconSize(QtCore.QSize(50, 50))
        self.btn_results_1.setCheckable(True)
        self.btn_results_1.setAutoExclusive(True)
        self.btn_results_1.setObjectName("btn_results_1")
        self.verticalLayout.addWidget(self.btn_results_1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 513, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.btn_exit_1 = QtWidgets.QPushButton(self.menu_icons_only)
        self.btn_exit_1.setText("")
        self.btn_exit_1.setIcon(icon5)
        self.btn_exit_1.setIconSize(QtCore.QSize(50, 50))
        self.btn_exit_1.setCheckable(True)
        self.btn_exit_1.setAutoExclusive(True)
        self.btn_exit_1.setObjectName("btn_exit_1")
        self.verticalLayout_2.addWidget(self.btn_exit_1)
        self.gridLayout.addWidget(self.menu_icons_only, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(-1)
        self.btn_menu.toggled['bool'].connect(self.menu_icons_only.setVisible) # type: ignore
        self.btn_menu.toggled['bool'].connect(self.menu_full.setHidden) # type: ignore
        self.btn_exit_1.clicked.connect(MainWindow.close) # type: ignore
        self.btn_exit_2.clicked.connect(MainWindow.close) # type: ignore
        self.btn_home_1.toggled['bool'].connect(self.btn_home_2.setChecked) # type: ignore
        self.btn_ble_1.toggled['bool'].connect(self.btn_ble_2.setChecked) # type: ignore
        self.btn_start_1.toggled['bool'].connect(self.btn_start_2.setChecked) # type: ignore
        self.btn_results_1.toggled['bool'].connect(self.btn_results_2.setChecked) # type: ignore
        self.btn_home_2.toggled['bool'].connect(self.btn_home_1.setChecked) # type: ignore
        self.btn_ble_2.toggled['bool'].connect(self.btn_ble_1.setChecked) # type: ignore
        self.btn_start_2.toggled['bool'].connect(self.btn_start_1.setChecked) # type: ignore
        self.btn_results_2.toggled['bool'].connect(self.btn_results_1.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_screen_name.setText(_translate("MainWindow", "Tu stavi naziv svakog prozora"))
        self.btn_home_2.setText(_translate("MainWindow", "Home"))
        self.btn_ble_2.setText(_translate("MainWindow", "BLE Connection"))
        self.btn_start_2.setText(_translate("MainWindow", "Start measurment"))
        self.btn_results_2.setText(_translate("MainWindow", "Results"))
        self.btn_exit_2.setText(_translate("MainWindow", "Exit"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
