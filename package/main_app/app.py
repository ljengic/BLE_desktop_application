import sys
import time
from PyQt5 import QtWidgets, QtCore
from package.main_app.gui import Ui_MainWindow
from package.home.home import Home
from package.ble.ble import BLE
from package.patients.patients import Patients
from package.measure.measure import Measure
from package.results.results import Results

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

        self.menu_icons_only.setHidden(True)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_home_2.setChecked(True)

        self.home = Home()
        self.ble = BLE()
        self.patients = Patients()
        self.measure = Measure(self.ble)
        self.results = Results()

        self.stackedWidget.addWidget(self.home)
        self.stackedWidget.addWidget(self.ble)
        self.stackedWidget.addWidget(self.patients)
        self.stackedWidget.addWidget(self.measure)
        self.stackedWidget.addWidget(self.results)

        self.btn_home_1.clicked.connect(self.btn_home_on_click)
        self.btn_home_2.clicked.connect(self.btn_home_on_click)

        self.btn_ble_1.clicked.connect(self.btn_ble_on_click)
        self.btn_ble_2.clicked.connect(self.btn_ble_on_click)

        self.btn_patient_1.clicked.connect(self.btn_patients_on_click)
        self.btn_patient_2.clicked.connect(self.btn_patients_on_click)

        self.btn_start_1.clicked.connect(self.btn_measure_on_click)
        self.btn_start_2.clicked.connect(self.btn_measure_on_click)

        self.btn_results_1.clicked.connect(self.btn_results_on_click)
        self.btn_results_2.clicked.connect(self.btn_results_on_click)

        self.label_screen_name.setText("Home screen")

    def btn_home_on_click(self):
        self.label_screen_name.setText("Home screen")
        self.stackedWidget.setCurrentIndex(0)

    def btn_ble_on_click(self):
        self.label_screen_name.setText("BLE connection")
        self.stackedWidget.setCurrentIndex(1)

    def btn_patients_on_click(self):
        self.label_screen_name.setText("Patients")
        self.stackedWidget.setCurrentIndex(2)

    def btn_measure_on_click(self):
        self.label_screen_name.setText("Measure")
        self.stackedWidget.setCurrentIndex(3)

    def btn_results_on_click(self):
        self.label_screen_name.setText("Results")
        self.stackedWidget.setCurrentIndex(4)

#run application
def run():
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(app_load_css("./style/Adaptic.qss"))
    window = MainWindow()
    window.show()
    return app.exec_()