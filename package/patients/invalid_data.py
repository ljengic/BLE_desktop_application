import sys
import time
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from package.patients.gui_invalid_data import Ui_Invalid_data
from package.tools import set_window_icon_and_title

class Invalid_Data(QtWidgets.QWidget, Ui_Invalid_data):
    
    def __init__(self, main_app):
        super(Invalid_Data, self).__init__()
        self.setupUi(self)

        self.setFixedSize(260, 180)
        set_window_icon_and_title(self)
        self.main_app = main_app

        self.btn_ok.clicked.connect(self.close_window)

    def show_invalid_data_window(self, msg):
        self.main_app.lock()
        self.label_3.setText(msg)
        self.show()

    def close_window(self):
        self.close()
        self = None

    def closeEvent(self, event):
        self.main_app.unlock()
        event.accept()
