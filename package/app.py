import sys
import time
from PyQt5 import QtWidgets
from package.ble_api.scan import BLE_Scanner

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ble_scanner = BLE_Scanner()
        self.ble_scanner.scan_devices()

#run application

def run():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec_()