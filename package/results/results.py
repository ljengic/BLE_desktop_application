import sys
import time
from PyQt5 import QtWidgets, QtCore
from package.results.gui_results import Ui_Results

class Results(QtWidgets.QWidget, Ui_Results):
    def __init__(self, parent=None):
        super(Results, self).__init__(parent)
        self.setupUi(self)

