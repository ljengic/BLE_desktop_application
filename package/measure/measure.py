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
from package.medicine.add_medication import Add_Medication
from package.medicine.medicine import Medicine
from package.ble.ble import BLE
from package.patients.patient import Patient
from package.patients.select_patient import Select_Patient
from package.patients.invalid_data import Invalid_Data
from package.patients.patient import get_patient_from_csv
from package.graphs.graph_widget import Graph_Widget
from package.paths.patient_path import Patient_Path
from package.paths.measurment_path import Measurment_Path

from package.tools import write_to_file
from package.parser import decode_msg
from package.tools import get_max_from_csv


class Measure(QtWidgets.QWidget, Ui_Measure):

    def __init__(self, main_app):
        super(Measure, self).__init__()
        self.setupUi(self)

        self.graph = Graph_Widget(self.widget_2, True)
        self.verticalLayout_25.addWidget(self.graph)
        self.label_27.hide()
        #self.gridLayout_52 = QtWidgets.QGridLayout(self.page)
        #self.gridLayout_52.setObjectName("gridLayout_52")
        #self.gridLayout_52.addWidget(self.graph, 0, 0, 1, 1)

        self.main_app = main_app

        self.add_medication = Add_Medication(self.main_app)
        self.select_patient = Select_Patient(self.main_app)
        self.invalid_data = Invalid_Data(self.main_app)

        self.main_app.ble.ble_msg_received.connect(self.msg_received)
        #self.btn_start_new_measurment.clicked.connect(self.btn_start_new_measurment_handle)
        self.bnt_new_patient.clicked.connect(self.btn_new_patient_handle)
        self.btn_select_patient.clicked.connect(self.btn_select_patient_handle)
        self.btn_complete.clicked.connect(self.btn_complete_handle)
        self.btn_back_main.clicked.connect(self.btn_back_main_handle)

        self.btn_add_medication.clicked.connect(self.bt_add_medication_clicked_handle)
        self.add_medication.medicine.connect(self.medicine_added)
        self.select_patient.patient.connect(self.patient_selected)

        #self.medicine_1 = Medicine(self.frame_20, "Sljiva, domaca")
        #self.verticalLayout_20.addWidget(self.medicine_1)
        #self.medicine_2 = Medicine(self.frame_20, "Vilijamovka")
        #self.verticalLayout_20.addWidget(self.medicine_2)

        self.btn_start.clicked.connect(self.btn_start_press_handle)
        self.btn_stop.clicked.connect(self.btn_stop_press_handle)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)

        #this variable is true if patient is new, need for making new patient folder after valid data
        self.is_patient_new = False

    def btn_new_patient_handle(self):
        if(True == self.main_app.ble.is_device_connected()):
            self.clear_input_text_boxes()
            self.medicine_list = []
            self.medicine_widget_list = []
            self.label_input_patient.setText("Please fill new patient data") 
            self.stackedWidget.setCurrentIndex(1)
            self.is_patient_new = True

    def btn_select_patient_handle(self):
        if(True == self.main_app.ble.is_device_connected()):
            self.select_patient.show_select_patient_window()      

    def btn_complete_handle(self):
        # first check if data is valid !
        self.patient = self.get_patient_from_input_data()
        if(True == self.check_data()):
            self.measurment_path = Measurment_Path(self.patient_path.folder_path, None)
            self.patient.calculate_bmi()
            self.patient.print_patient_info()
            
            if(True == self.is_patient_new):
                self.patient_path = Patient_Path(None)

            self.patient.write_to_csv(self.patient_path.patient_file_path)
            self.patient.write_to_csv(self.measurment_path.patient_file_path)
            self.fill_patient_data()
            self.stackedWidget.setCurrentIndex(2)
            self.make_graph()

    def msg_received(self, msg):
        msg_list = msg.split(';') 
        write_to_file(self.measurment_path.raw_data_file, msg_list)
        print(msg)
        decode_msg(self.measurment_path,msg_list)

    def make_graph(self):
        self.graph.set_lines([["5 kHz",self.measurment_path.bioz_5_path,'b'],
        ["50 kHz",self.measurment_path.bioz_50_path,'g'],
        ["100 kHz",self.measurment_path.bioz_100_path,'r'],
        ["200 kHz",self.measurment_path.bioz_200_path,'k'],
        ])

    def btn_start_press_handle(self):
        self.widget_2.show()

        self.stackedWidget_2.setCurrentIndex(1)

        self.main_app.ble.ble_send(3)

        self.graph.start()

    def btn_stop_press_handle(self):
        self.main_app.ble.ble_send(4)

        self.graph.stop()

        self.stackedWidget_2.setCurrentIndex(0)

        get_max_from_csv(self.measurment_path.bioz_max_path)

        #self.widget_2.hide()
        #self.graph.delete_data()

        #self.verticalLayout.removeWidget(self.widget_2)
        #sip.delete(self.widget_2)
        #self.widget_2 = None

        #self.widget_2 = QtWidgets.QWidget(self.page_3)
        #self.widget_2.setObjectName("widget_2")
        #self.verticalLayout.addWidget(self.widget_2)
        

        self.stackedWidget.setCurrentIndex(0)

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
        patient.add_medications(self.medicine_list)

        return patient

    def fill_patient_data(self):
        self.display_age.setText(self.patient.age)
        self.display_height.setText(self.patient.height)
        self.display_weight.setText(self.patient.weight)
        self.display_sex.setText(self.patient.sex)
        self.display_bmi.setText(self.patient.bmi)

    def bt_add_medication_clicked_handle(self):
        self.add_medication.show_add_medicine_window()
        #self.setEnabled(False)

    def medicine_added(self, med):
        self.medicine_list.append(med)
        self.medicine_1 = Medicine(self.frame_20, med, self.medicine_remove)
        self.verticalLayout_21.addWidget(self.medicine_1)
        self.medicine_widget_list.append(self.medicine_1)
        self.widget_no_med.hide()
        print(self.medicine_list)

    def medicine_remove(self, med_widget, med):
        self.medicine_list.remove(med)
        #if list is empty put no medication label
        if([] == self.medicine_list):
            self.widget_no_med.show()
        print(self.medicine_list)
        self.verticalLayout_21.removeWidget(med_widget)
        med_widget.hide()
        del(med_widget)

    def patient_selected(self,patient_folder_path):
        self.label_input_patient.setText("Check patient info and edit them if changed") 
        self.patient_path = Patient_Path(patient_folder_path) 
        self.patient = get_patient_from_csv(self.patient_path.patient_file_path)
        self.medicine_list = []
        self.medicine_widget_list = []
        self.fill_patient_input_data(self.patient)
        self.stackedWidget.setCurrentIndex(1)

    #fill input data with patient data from database
    def fill_patient_input_data(self,patient):
        self.input_age.setText(patient.age)
        self.input_height.setText(patient.height)
        self.input_weight.setText(patient.weight)

        if ('M' == patient.sex):
            self.btn_male.setChecked(True)
            self.btn_female.setChecked(False)
        else:
            self.btn_male.setChecked(False)
            self.btn_female.setChecked(True)

        self.input_chest_lower.setText(patient.chest_lower)
        self.input_chest_upper.setText(patient.chest_upper)

        self.input_leg_ankle.setText(patient.leg_ankle)
        self.input_leg_calf.setText(patient.leg_calf) 
        self.input_leg_knee.setText(patient.leg_knee)

        for med in patient.medications:
            print(med)
            self.medicine_added(med)

    #check if input data is valid
    #if valid return True, otherwise return False
    def check_data(self):
        ret = True
        msg = self.patient.check_patient_data()
        if("Ok" != msg):
            self.invalid_data.show_invalid_data_window(msg)
            ret = False
        return ret

    def btn_back_main_handle(self):
        self.medicine_all_remove()
        self.stackedWidget.setCurrentIndex(0)
        #TO DO
        #ocisti podatke

    def medicine_all_remove(self):
        self.widget_no_med.show()

        for med_widget in  self.medicine_widget_list:
            self.verticalLayout_21.removeWidget(med_widget)
            med_widget.hide()
            del(med_widget)

    def clear_input_text_boxes(self):
        self.input_age.setText("")
        self.input_height.setText("")
        self.input_weight.setText("")

        self.btn_male.setChecked(False)
        self.btn_female.setChecked(False)

        self.input_chest_lower.setText("")
        self.input_chest_upper.setText("")

        self.input_leg_ankle.setText("")
        self.input_leg_calf.setText("") 
        self.input_leg_knee.setText("")        
