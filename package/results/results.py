import sys
import time
import os
from PyQt5 import QtWidgets, QtCore
from package.results.gui_results import Ui_Results
from package.graphs.graph_widget import Graph_Widget
from package.tools.paths import Paths
from package.patients.patient import get_patient_from_csv

class Results(QtWidgets.QWidget, Ui_Results):
    def __init__(self, parent=None):
        super(Results, self).__init__(parent)
        self.setupUi(self)
        
        self.graph = Graph_Widget(self.widget, False)
        self.verticalLayout_4.addWidget(self.graph)
        self.label.hide()

        self.stackedWidget.setCurrentIndex(0)

        self.btn_show.setEnabled(False)
        self.listWidget.itemClicked.connect(self.list_item_clicked)
        self.btn_show.clicked.connect(self.btn_show_clicked_handle)
        self.btn_refresh.clicked.connect(self.btn_refresh_clicked_handle)
        self.btn_back.clicked.connect(self.btn_back_clicked_handle)

        self.frame_5.hide()
        self.refresh_measurment_list()

    def btn_refresh_clicked_handle(self):
        self.refresh_measurment_list()

    def btn_show_clicked_handle(self):
        self.make_graph()
        self.stackedWidget.setCurrentIndex(1)

    def btn_back_clicked_handle(self):
        self.graph.stop()
        self.stackedWidget.setCurrentIndex(0)

    def list_item_clicked(self, itemC):
        #self.set_info_data(itemC.data(QtCore.Qt.UserRole))
        self.folder_path = os.getcwd() + "\data\\" + itemC.data(QtCore.Qt.UserRole)
        self.paths = Paths(self.folder_path)
        self.patient = get_patient_from_csv(self.paths.patient_file_path)
        self.fill_patient_data()
        self.btn_show.setEnabled(True)
        self.frame_5.show()

    def refresh_measurment_list(self):
        self.listWidget.clear()
        for root, dirs, files in os.walk("./data", topdown=False):
            for name in dirs:
                self.item2add = QtWidgets.QListWidgetItem()
                self.item2add.setText(name)
                self.item2add.setData(QtCore.Qt.UserRole, name)
                self.listWidget.addItem(self.item2add)

    def make_graph(self):
        self.graph.set_lines([["5 kHz",self.paths.bioz_data_file_5,'b'],
        ["50 kHz",self.paths.bioz_data_file_50,'g'],
        ["100 kHz",self.paths.bioz_data_file_100,'r'],
        ["200 kHz",self.paths.bioz_data_file_200,'k'],
        ])
        self.graph.start()

    def fill_patient_data(self):
        self.display_age.setText(self.patient.age)
        self.display_height.setText(self.patient.height)
        self.display_weight.setText(self.patient.weight)
        self.display_sex.setText(self.patient.sex)
        self.display_bmi.setText(self.patient.bmi)




