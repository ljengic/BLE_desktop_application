import sys
import time
from PyQt5 import QtWidgets, QtCore
from package.home.gui_home import Ui_Home

class Home(QtWidgets.QWidget, Ui_Home):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)

