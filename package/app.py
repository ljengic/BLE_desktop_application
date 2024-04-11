import sys
import time
from PyQt5 import QtWidgets, QtCore
from package.gui.scanner import Ui_MainWindow
from package.ble_api.scan import BLE_Scanner
from package.ble_api.controller import BLE_Controller

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
        self.ble_controller = BLE_Controller()

        self.button_connect.setEnabled(False)
        self.button_scan.clicked.connect(self.button_scan_press_handle)
        self.button_connect.clicked.connect(self.button_connect_handler)
        self.ble_scanner.devices_scanned_message.connect(self.device_list_update)

        self.listWidget.itemClicked.connect(self.device_list_item_clicked)

    def button_scan_press_handle(self):
        self.listWidget.clear()
        self.button_scan.setEnabled(False)
        self.button_connect.setEnabled(False)
        #self.textBrowser.clear()
        self.ble_scanner.scan_devices()

    def device_list_update(self,device_list):
        self.listWidget.clear()
        for obj in device_list:
            self.item2add = QtWidgets.QListWidgetItem()
            self.item2add.setText(obj.name())
            self.item2add.setData(QtCore.Qt.UserRole, obj)
            self.listWidget.addItem(self.item2add)
        self.button_scan.setEnabled(True)

    def button_connect_handler(self):
        self.ble_controller.connectDevice(self.listWidget.currentItem().data(QtCore.Qt.UserRole))

    #Device clicked in list view
    def device_list_item_clicked(self, itemC):
        self.button_connect.setEnabled(True)
        self.deviceInfo = itemC.data(QtCore.Qt.UserRole)

#run application

def run():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(app_load_css("./package/gui/css.qss"))
    window = MainWindow()
    window.show()
    return app.exec_()