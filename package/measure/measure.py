import sys
import time
from PyQt5 import QtWidgets, QtCore
from package.measure.gui_measure import Ui_Measure
from package.ble.ble import BLE

class Measure(QtWidgets.QWidget, Ui_Measure):

    def __init__(self,ble_instance):
        super(Measure, self).__init__()
        self.setupUi(self)

        self.ble = ble_instance

        self.btn_start.clicked.connect(self.btn_start_press_handle)
        self.btn_stop.clicked.connect(self.btn_stop_press_handle)

    def btn_start_press_handle(self):
        self.ble.ble_send(3)

    def btn_stop_press_handle(self):
        self.ble.ble_send(4)
