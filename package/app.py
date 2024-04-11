import sys
import time
from PyQt5 import QtWidgets
from package.gui.scanner import Ui_MainWindow
from package.ble_api.scan import BLE_Scanner

#function to load css file in application
def app_load_css(filename):
    with open(filename,'r') as my_css:
        content = my_css.read()
        my_css.close()
    return content
    
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ble_scanner = BLE_Scanner()
        self.ble_scanner.scan_devices()

#run application

def run():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(app_load_css("./package/gui/css.qss"))
    window = MainWindow()
    window.show()
    return app.exec_()