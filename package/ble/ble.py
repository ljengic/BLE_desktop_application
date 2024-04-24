import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtBluetooth import QBluetoothUuid, QLowEnergyService, QLowEnergyCharacteristic
from package.ble.gui_ble import Ui_BLE
from package.ble.scan import BLE_Scanner
from package.ble.controller import BLE_Controller

class BLE(QtWidgets.QWidget, Ui_BLE):

    ble_msg_received = pyqtSignal(str)

    def __init__(self, parent=None):
        super(BLE, self).__init__(parent)
        self.setupUi(self)

        #make instances of scaner and controller classes
        self.ble_scanner = BLE_Scanner()
        self.ble_controller = BLE_Controller()

        self.btn_connect.setEnabled(False)
        self.btn_scan.clicked.connect(self.btn_scan_press_handle)
        self.btn_connect.clicked.connect(self.btn_connect_handler)
        self.ble_scanner.devices_scanned_message.connect(self.device_list_update)
        self.ble_controller.servicesFound.connect(self.handleServicesFound)
        self.ble_controller.serviceOpened.connect(self.handleOpenedService)
        self.btn_disconnect.clicked.connect(self.btn_disconnect_handle)

        self.listWidget.itemClicked.connect(self.device_list_item_clicked)

        self.ble_controller.controllerConnected.connect(self.handleDeviceConnected)
        self.ble_controller.controllerDisconnected.connect(self.handleDeviceDisconnected)

        self.stackedWidget.setCurrentIndex(0)
        self.frame_7.hide()

    def btn_scan_press_handle(self):
        self.listWidget.clear()
        self.btn_scan.setEnabled(False)
        self.frame_7.hide()
        self.ble_scanner.scan_devices()

    def device_list_update(self,device_list):
        self.listWidget.clear()
        for obj in device_list:
            self.item2add = QtWidgets.QListWidgetItem()
            self.item2add.setText(obj.name())
            self.item2add.setData(QtCore.Qt.UserRole, obj)
            self.listWidget.addItem(self.item2add)
        self.btn_scan.setEnabled(True)

    def btn_connect_handler(self):
        self.ble_controller.connectDevice(self.listWidget.currentItem().data(QtCore.Qt.UserRole))

    def btn_disconnect_handle(self):
        self.ble_controller.disconnect()
        self.handleDeviceDisconnected()

    #Device clicked in list view
    def device_list_item_clicked(self, itemC):
        self.btn_connect.setEnabled(True)
        self.frame_7.show()
        self.ble_set_info_data(itemC.data(QtCore.Qt.UserRole))

    #Adds discovered BLE services to list view
    def handleServicesFound(self):
        #go through all discoverd services and try to find the one that is used in project
        for servicesUids in self.ble_controller.controller.services():
            self.ble_service_uuid = QBluetoothUuid(servicesUids)
            if (self.ble_service_uuid == QBluetoothUuid("{00001523-f7b8-48e9-8fe5-8e202813f0d9}")):
                #we found our service!
                self.ble_controller.readService(self.ble_service_uuid)

    def handleOpenedService(self):
        print("Service opend!!!")
        #time.sleep(0.2)
        #print found characteristics, for debugging
        for obj in self.ble_controller.openedService.characteristics():
            self.ble_char_uuid = obj.uuid()
            if (self.ble_char_uuid == QBluetoothUuid("{00001524-f7b8-48e9-8fe5-8e202813f0d9}")):
                #we found our service!
                self.read_char = obj
                self.suscribe_to_char(self.read_char)

            elif (self.ble_char_uuid == QBluetoothUuid("{00001525-f7b8-48e9-8fe5-8e202813f0d9}")):
                #we found our service!
                self.write_char = obj

            else:
                print("Something went really really wrong, we dont know that characteristic :(\n")

    #Called when succesfully connected to device
    def handleDeviceConnected(self):
        self.label_conn_status.setText("Connected")
        self.label_ble_info.setText("Wohooo, you can start measuring :)")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/ble_on.png"))
        self.stackedWidget.setCurrentIndex(1)
        self.frame.hide()
        print("Successfully connected!\n")
        #self.ble_serviceAgent.scan_services(self.ble_controller.ble_device.address())

    def handleDeviceDisconnected(self):
        self.label_conn_status.setText("Disconnected")
        self.label_ble_info.setText("Please scan availabe BLE devices and \nchoose device to connect")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/ble_off.png"))
        self.stackedWidget.setCurrentIndex(0)
        self.frame_7.hide()
        self.listWidget.clear()
        self.frame.show()

    def suscribe_to_char(self, characterictis):
        self.karakteristika = characterictis

        self.type = QBluetoothUuid(QBluetoothUuid.ClientCharacteristicConfiguration)
        self.descript = self.karakteristika.descriptor(self.type)

        self.array = QByteArray(b'\x01\x00')        #turn on NOTIFY for characteristic

        self.ble_controller.openedService.characteristicChanged.connect(self.updateVal)
        self.ble_controller.openedService.writeDescriptor(self.descript, self.array)    #turn on NOTIFY

    def updateVal(self, Charac, newVal):
        self.val = QByteArray()
        self.val = newVal
        self.ble_string_msg = self.val.data().decode()
        self.ble_msg_received.emit(self.ble_string_msg)

    def ble_send(self, val):
        q_b = QByteArray()
        q_b.setNum(val,10)
        print("Sending command to micreocontroller ",val)
        self.ble_controller.openedService.writeCharacteristic(self.write_char,q_b,QLowEnergyService.WriteWithoutResponse)

    def ble_set_info_data(self, device):
        self.label_inf_name.setText(device.name())
        #self.label_inf_type.setText(device.coreConfigurations())
        self.label_inf_rssi.setText(str(device.rssi()))
        self.label_inf_address.setText(device.address().toString())


