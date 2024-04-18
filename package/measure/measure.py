import sys
import time
from PyQt5 import QtWidgets, QtCore
from package.measure.gui_measure import Ui_Measure

class Measure(QtWidgets.QWidget, Ui_Measure):
    def __init__(self, parent=None):
        super(Measure, self).__init__(parent)
        self.setupUi(self)
