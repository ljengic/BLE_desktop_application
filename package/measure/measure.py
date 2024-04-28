import os
import sys
import time
import csv
import pathlib
import glob
import sip
from datetime import date
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from package.measure.gui_measure import Ui_Measure
from package.ble.ble import BLE
from package.patients.patient import Patient
from package.graphs.graph import Graph
from package.tools.paths import Paths

class Measure(QtWidgets.QWidget, Ui_Measure):

    ble_not_connected_error = pyqtSignal()

    def __init__(self,ble_instance, fail_sound):
        super(Measure, self).__init__()
        self.setupUi(self)

        self.ble = ble_instance
        self.graph = Graph(self.widget_2, True)
        self.play_fail_sound = fail_sound

        self.btn_start.clicked.connect(self.btn_start_press_handle)
        self.btn_stop.clicked.connect(self.btn_stop_press_handle)
        self.ble.ble_msg_received.connect(self.msg_received)
        self.btn_start_new_measurment.clicked.connect(self.btn_start_new_measurment_handle)
        self.btn_complete.clicked.connect(self.btn_complete_handle)

        self.widget_2.hide()

        self.stackedWidget.setCurrentIndex(0)

    def btn_start_new_measurment_handle(self):
        #clear text 
        #self.clear_input_text_boxs()

        self.make_measurment_folder()
        self.paths = Paths(self.folder_path)

        #check BLE connection
        if(True == self.ble.is_device_connected()):
            #switch to page for patient data input
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.play_fail_sound()
            self.show_ble_popup()
            print("BLE not connected, you cannot measure, sorryy, byee.")

    def btn_complete_handle(self):
        # first check if data is valid !
        self.patient = self.get_patient_from_input_data()
        self.patient.print_patient_info()
        self.patient.write_to_csv(self.paths.patient_file_path)
        self.stackedWidget.setCurrentIndex(2)

    def msg_received(self, msg):
        msg_list = msg.split(';') 
        self.csv_write_raw_data(msg_list)
        self.decode_msg(msg_list)

    def csv_write_raw_data(self, data):
        #change this later, there is no need for opening the file every time
        with open(self.paths.raw_data_file, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow(data)
            file.close()

    def decode_msg(self,msg):
        print(msg)
        if('0' == msg[1]):
            self.csv_write_bioz_data(msg)
        elif('1' == msg[1]):
            self.csv_write_temperature_data(msg)    
        else:
            print("ERROR: cannot decode received data")            

    def csv_write_temperature_data(self,msg):
        print("Received data from temperature sensor.")
        with open( self.paths.temp_data_file, 'a', newline='') as file:
            self.writer = csv.writer(file)
            self.writer.writerow([msg[0],msg[2]])
            file.close()

    def csv_write_bioz_data(self,msg):
        print("Received data from bioz sensor.")

    def btn_start_press_handle(self):
        self.graph.start(self.paths.temp_data_file)
        self.widget_2.show()
        self.ble.ble_send(3)

    def btn_stop_press_handle(self):
        self.ble.ble_send(4)
        
        #self.graph.__del__()

        self.widget_2.hide()
        self.graph.delete_data()

        #self.verticalLayout.removeWidget(self.widget_2)
        #sip.delete(self.widget_2)
        #self.widget_2 = None

        #self.widget_2 = QtWidgets.QWidget(self.page_3)
        #self.widget_2.setObjectName("widget_2")
        #self.verticalLayout.addWidget(self.widget_2)
        
        self.stackedWidget.setCurrentIndex(0)

    #make folder for this measurment
    def make_measurment_folder(self):
        today = date.today()
        name_prefix = "Measurment_" + today.strftime("%m-%d-%Y") + '_#'

        today_dirs = glob.glob('data/'+name_prefix+'*')
        today_measurments = len(today_dirs)
        name = name_prefix + str(today_measurments + 1)

        self.folder_path = os.getcwd() + "\data\\" + name
        os.makedirs(self.folder_path)


    def get_patient_from_input_data(self):

        sex = "None"

        if((self.btn_male.isChecked() == True) and (self.btn_female.isChecked() == False)):
            sex = "M"
        elif((self.btn_male.isChecked() == False) and (self.btn_female.isChecked() == True)):
            sex = "F"
        else:
            #izbaci neki error
            print("ERROR while getting sex info")

        patient = Patient(self.input_age.text(),sex, self.input_height.text(),self.input_weight.text())

        patient.add_leg_circumfences(self.input_leg_ankle.text(), self.input_leg_calf.text(), self.input_leg_knee.text())

        patient.add_chest_circumfences(self.input_chest_upper.text(), self.input_chest_lower.text())

        return patient

    def show_ble_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("BLE not connected!")
        msg.setInformativeText("You can't measure if your device is not connected.")
        #msg.setIcon(QMessageBox.Critical)
        msg.addButton("Connect device", QMessageBox.AcceptRole)

        msg.buttonClicked.connect(self.popup_button_clicked)

        msg.exec_()

    def popup_button_clicked(self, i):
        if("Connect device" == i.text()):
            #go to ble connection screen
            self.ble_not_connected_error.emit()
            print("Switching to BLE screen")
        else:
            print("Uknown popup button")
