import os
import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui

def set_window_icon_and_title(window):
    window.setWindowIcon(QtGui.QIcon('./images/logo.jpeg'))
    window.setWindowTitle("Fluid Track")