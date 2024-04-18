import sys
import time
from PyQt5 import QtWidgets, QtCore
from package.ble.gui_ble import Ui_BLE

class BLE(QtWidgets.QWidget, Ui_BLE):
    def __init__(self, parent=None):
        super(BLE, self).__init__(parent)
        self.setupUi(self)