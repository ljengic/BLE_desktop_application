from PyQt5.QtBluetooth import QBluetoothDeviceDiscoveryAgent
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class BLE_Scanner(QObject):  
    #scannerOutputMessage = pyqtSignal(str)

    def __init__(self):
        QObject.__init__(self)
        self.discoveryAgent = QBluetoothDeviceDiscoveryAgent()
        self.discoveryAgent.setLowEnergyDiscoveryTimeout(5000)
        self.discoveryAgent.finished.connect(self.get_devices)
        self.discoverd_devices_list = None

    def scan_devices(self):
        print("Scanning\n")
        #self.scannerOutputMessage.emit(">>Scanning\n")
        self.discoveryAgent.start()

    def get_devices(self):
        self.discoverd_devices_list = self.discoveryAgent.discoveredDevices()
        self.print_devices()

    def print_devices(self):
        for obj in self.discoverd_devices_list:
            print(obj.name())
