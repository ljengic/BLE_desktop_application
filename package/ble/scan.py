from PyQt5.QtBluetooth import QBluetoothDeviceDiscoveryAgent
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class BLE_Scanner(QObject):  
    devices_scanned_message = pyqtSignal(list)
    discoverd_devices_list = None

    def __init__(self):
        QObject.__init__(self)
        self.discoveryAgent = QBluetoothDeviceDiscoveryAgent()
        self.discoveryAgent.setLowEnergyDiscoveryTimeout(5000)
        self.discoveryAgent.finished.connect(self.get_devices)

    def scan_devices(self):
        print("Scanning\n")
        self.discoveryAgent.start()

    def get_devices(self):
        self.discoverd_devices_list = self.discoveryAgent.discoveredDevices()
        self.print_devices()
        self.devices_scanned_message.emit(self.discoverd_devices_list)

    def print_devices(self):
        for obj in self.discoverd_devices_list:
            print(obj.name())

