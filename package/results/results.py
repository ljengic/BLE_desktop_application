import sys
import time
import os
from PyQt5 import QtWidgets, QtCore
from package.results.gui_results import Ui_Results
from package.graphs.graph_widget import Graph_Widget
from package.patients.select_patient import Select_Patient
from package.patients.patient import get_patient_from_csv
from package.graphs.graph_widget import Graph_Widget
from package.paths.patient_path import Patient_Path
from package.paths.measurment_path import Measurment_Path
from package.medicine.medicine import Medicine

class Results(QtWidgets.QWidget, Ui_Results):
    def __init__(self, main_app):
        super(Results, self).__init__()
        self.setupUi(self)
        
        self.main_app = main_app

        self.graph = Graph_Widget(self.widget, False)
        self.verticalLayout_4.addWidget(self.graph)
        self.label.hide()

        self.stackedWidget.setCurrentIndex(0)

        self.select_patient = Select_Patient(self.main_app)
        self.select_patient.patient.connect(self.patient_selected)
        self.btn_select_patient.clicked.connect(self.btn_select_patient_handle)
        self.btn_back_main.clicked.connect(self.btn_back_main_handle)

        #self.btn_show.setEnabled(False)
        #self.listWidget.itemClicked.connect(self.list_item_clicked)
        #self.btn_show.clicked.connect(self.btn_show_clicked_handle)
        #self.btn_back.clicked.connect(self.btn_back_clicked_handle)

        #self.frame_5.hide()
        #self.refresh_measurment_list()

    def btn_select_patient_handle(self):
         self.select_patient.show_select_patient_window()    

    def btn_back_main_handle(self):
        self.medicine_all_remove()
        self.stackedWidget.setCurrentIndex(0)

    def patient_selected(self,patient_folder_path):
        self.patient_path = Patient_Path(patient_folder_path) 
        self.patient = get_patient_from_csv(self.patient_path.patient_file_path)
        #else - corrupted data for selected patient error
        if("Ok" == self.patient.check_patient_data()):
            self.patient.calculate_bmi()
            self.medicine_list = []
            self.medicine_widget_list = []
            self.fill_patient_data()
            self.refresh_measurment_list()
            self.stackedWidget.setCurrentIndex(1)

    def fill_patient_data(self):
        self.label_name.setText(self.patient_path.name)

        self.display_age.setText(self.patient.age + " years")
        self.display_height.setText(self.patient.height + " cm")
        self.display_weight.setText(self.patient.weight + " kg")
        if("M" == self.patient.sex):
            sex = "male"
        else:
            sex = "female"
        self.display_sex.setText(sex)
        self.display_bmi.setText(self.patient.bmi)

        self.display_chest_upper.setText(self.patient.chest_upper + " cm")
        self.display_chest_lower.setText(self.patient.chest_lower + " cm")
        
        self.display_leg_ankle.setText(self.patient.leg_ankle + " cm")
        self.display_leg_calf.setText(self.patient.leg_calf + " cm")
        self.display_leg_knee.setText(self.patient.leg_knee + " cm")

        for med in self.patient.medications:
            print(med)
            self.medicine_added(med)

    def refresh_measurment_list(self):
        self.listWidget.clear()
        #print(self.patient_path.folder_path + "\\")
        for name in os.listdir(self.patient_path.folder_path + "\\"):
            #print(self.patient_path.folder_path + "\\" +  name + "\\")
            if os.path.isdir(self.patient_path.folder_path + "\\" +  name + "\\"):
                print(name)
                self.item2add = QtWidgets.QListWidgetItem()
                self.item2add.setText(name)
                self.item2add.setData(QtCore.Qt.UserRole, name)
                self.listWidget.addItem(self.item2add)

    def medicine_added(self, med):
        self.medicine_list.append(med)
        self.medicine_1 = Medicine(self.frame_24, med, None)
        self.verticalLayout_23.addWidget(self.medicine_1)
        self.widget_no_med.hide()
        self.medicine_widget_list.append(self.medicine_1)
        print(self.medicine_list)

    def medicine_all_remove(self):
        self.widget_no_med.show()

        for med_widget in  self.medicine_widget_list:
            self.verticalLayout_23.removeWidget(med_widget)
            med_widget.hide()
            del(med_widget)

############################## OLD ##############################################

    def btn_show_clicked_handle(self):
        self.make_graph()
        self.stackedWidget.setCurrentIndex(1)

    def btn_back_clicked_handle(self):
        self.graph.stop()
        self.stackedWidget.setCurrentIndex(0)

    def list_item_clicked(self, itemC):
        #self.set_info_data(itemC.data(QtCore.Qt.UserRole))
        self.folder_path = os.getcwd() + "\data\\" + itemC.data(QtCore.Qt.UserRole)
        #self.paths = Paths(self.folder_path)
        self.patient = get_patient_from_csv(self.paths.patient_file_path)
        self.fill_patient_data()
        self.btn_show.setEnabled(True)
        self.frame_5.show()

    def make_graph(self):
        self.graph.set_lines([["5 kHz",self.paths.bioz_data_file_5,'b'],
        ["50 kHz",self.paths.bioz_data_file_50,'g'],
        ["100 kHz",self.paths.bioz_data_file_100,'r'],
        ["200 kHz",self.paths.bioz_data_file_200,'k'],
        ])
        self.graph.start()

