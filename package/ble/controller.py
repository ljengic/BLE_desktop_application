import sys
import time
from PyQt5.QtBluetooth import QLowEnergyController, QLowEnergyService, QBluetoothUuid, QLowEnergyCharacteristic
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class BLE_Controller(QObject):
    controllerConnected = pyqtSignal()
    servicesFound = pyqtSignal()
    serviceOpened = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    #connect to device
    def connectDevice(self, dev):
        self.ble_device = dev
        print("Connnecting to {0}".format(self.ble_device.name()))      #debug
        
        self.controller = QLowEnergyController.createCentral(self.ble_device)    
        
        self.controller.connected.connect(self.deviceConnected)
        self.controller.disconnected.connect(self.deviceDisconnected)
        self.controller.error.connect(self.errorReceived)
        self.controller.serviceDiscovered.connect(self.service_found_print)
        self.controller.discoveryFinished.connect(self.serviceScanDone)

        self.controller.setRemoteAddressType(QLowEnergyController.PublicAddress)
        self.controller.connectToDevice()

    #disconnect from device
    def disconnect(self):
        self.controller.disconnectFromDevice()

    #when device is connected start discovering services
    def deviceConnected(self):
        print("Device connected\n")
        time.sleep(0.1)
        self.controllerConnected.emit()
        self.controller.discoverServices()

    #print descovered service, used for debugging
    def service_found_print(self, servUid):
        self.serviceUid = servUid
        print("Found service {0}\n".format(self.serviceUid.toString()))

    def errorReceived(self, errMessage):
        print("error ")
        print("{0}\n".format(errMessage.toString()))
        self.controllerOutputMessage.emit(">>ERROR\n")

    #device disconnected callback
    def deviceDisconnected(self):
        print("device disconnected\n")

    #service scan done callback
    def serviceScanDone(self):
        print("Service scan done\n")
        self.servicesFound.emit()

    def readService(self, ble_service_UID):
        self.openedService = self.controller.createServiceObject(ble_service_UID)
        if self.openedService == None:
            print("ERR: Cannot open service\n")
        print(self.openedService.serviceName() + '\n')

        if (self.openedService.state() == QLowEnergyService.ServiceDiscovered):
            self.handleServiceOpened()
            
        elif (self.openedService.state() == QLowEnergyService.DiscoveryRequired):
            self.openedService.stateChanged.connect(self.handleServiceOpened)
            self.openedService.discoverDetails()
        else:
            print("Cannot discover service\n")

    def handleServiceOpened(self):
        if (self.openedService.state() == QLowEnergyService.ServiceDiscovered):
            self.serviceOpened.emit()