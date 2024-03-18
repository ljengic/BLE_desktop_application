import sys
import time
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
#run application

def run():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec_()