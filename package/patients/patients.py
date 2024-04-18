import sys
import time
from PyQt5 import QtWidgets, QtCore
from package.patients.gui_patients import Ui_Patients

class Patients(QtWidgets.QWidget, Ui_Patients):
    def __init__(self, parent=None):
        super(Patients, self).__init__(parent)
        self.setupUi(self)
