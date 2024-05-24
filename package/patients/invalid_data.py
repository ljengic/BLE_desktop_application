import sys
import time
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from package.patients.gui_invalid_data import Ui_Invalid_data

class Invalid_Data(QtWidgets.QWidget, Ui_Invalid_data):
    
    def __init__(self, lock_app, unlock_app):
        super(Invalid_Data, self).__init__()
        self.setupUi(self)

        self.lock_app = lock_app
        self.unlock_app = unlock_app

        self.btn_ok.clicked.connect(self.close_window)

    def show_invalid_data_window(self, msg):
        self.lock_app()
        self.label_3.setText(msg)
        self.show()

    def close_window(self):
        self.close()
        self.unlock_app()
        self = None
