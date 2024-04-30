import os
import sys
import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from package.main_app.gui import Ui_MainWindow
from package.home.home import Home
from package.ble.ble import BLE
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
        self.measure = Measure(self.ble, self.play_fail_sound, self.lock, self.unlock)
        self.results = Results()

        self.measure.ble_not_connected_error.connect(self.btn_ble_on_click)

        self.stackedWidget.addWidget(self.home)
        self.stackedWidget.addWidget(self.ble)
        self.stackedWidget.addWidget(self.measure)
        self.stackedWidget.addWidget(self.results)

        self.btn_home_1.clicked.connect(self.btn_home_on_click)
        self.btn_home_2.clicked.connect(self.btn_home_on_click)

        self.btn_ble_1.clicked.connect(self.btn_ble_on_click)
        self.btn_ble_2.clicked.connect(self.btn_ble_on_click)

        self.btn_start_1.clicked.connect(self.btn_measure_on_click)
        self.btn_start_2.clicked.connect(self.btn_measure_on_click)

        self.btn_results_1.clicked.connect(self.btn_results_on_click)
        self.btn_results_2.clicked.connect(self.btn_results_on_click)

        self.label_screen_name.setText("Home screen")

        self.make_data_folder()

    def make_data_folder(self):
        self.path = os.getcwd() + "\data"
        if not os.path.isdir(self.path):
            print("Creating folder data.")
            os.makedirs(self.path)
        else:
            print("Folder already exists.")

    def btn_home_on_click(self):
        self.label_screen_name.setText("Home screen")
        self.stackedWidget.setCurrentIndex(0)

    def btn_ble_on_click(self):
        self.label_screen_name.setText("BLE connection")
        self.btn_ble_1.setChecked(True)
        self.stackedWidget.setCurrentIndex(1)

    def btn_measure_on_click(self):
        self.label_screen_name.setText("Measure")
        self.stackedWidget.setCurrentIndex(2)

    def btn_results_on_click(self):
        self.label_screen_name.setText("Results")
        self.stackedWidget.setCurrentIndex(3)

    def play_fail_sound(self):
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile("./sounds/wa_wa.wav"))
        self.sound.play()

    def lock(self):
        self.setEnabled(False)
    
    def unlock(self):
        self.setEnabled(True)

#run application
def run():
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(app_load_css("./style/my_style.qss"))
    window = MainWindow()
    window.show()
    return app.exec_()