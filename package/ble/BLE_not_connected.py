import sys
import time
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from package.ble.gui_not_connected import Ui_BLE_not_connected
from package.tools import set_window_icon_and_title

class BLE_Not_Connected(QtWidgets.QWidget, Ui_BLE_not_connected):
    
    def __init__(self, main_app):
        super(BLE_Not_Connected, self).__init__()
        self.setupUi(self)

        self.setFixedSize(250, 200)
        set_window_icon_and_title(self)
        self.main_app = main_app

        self.btn_connect.clicked.connect(self.btn_connect_handler)

    def show_BLE_not_connected_window(self):
        self.main_app.lock()
        self.show()

    def btn_connect_handler(self):
        self.main_app.btn_ble_on_click()
        self.close()
        self = None

    def closeEvent(self, event):
        self.main_app.unlock()
        event.accept()
