import sys
import time
import os
from PyQt5 import QtWidgets, QtCore
from package.results.gui_results import Ui_Results
from package.graphs.graph import Graph
from package.tools.paths import Paths

class Results(QtWidgets.QWidget, Ui_Results):
    def __init__(self, parent=None):
        super(Results, self).__init__(parent)
        self.setupUi(self)
        
        self.graph = Graph(self.widget, False)

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
        self.graph.start(self.paths.temp_data_file)
        self.stackedWidget.setCurrentIndex(1)

    def btn_back_clicked_handle(self):
        self.graph.delete_data()
        self.stackedWidget.setCurrentIndex(0)

    def list_item_clicked(self, itemC):
        #self.set_info_data(itemC.data(QtCore.Qt.UserRole))
        self.frame_5.show()
        self.folder_path = os.getcwd() + "\data\\" + itemC.data(QtCore.Qt.UserRole)
        self.paths = Paths(self.folder_path)
        self.btn_show.setEnabled(True)

    def refresh_measurment_list(self):
        self.listWidget.clear()
        for root, dirs, files in os.walk("./data", topdown=False):
            for name in dirs:
                self.item2add = QtWidgets.QListWidgetItem()
                self.item2add.setText(name)
                self.item2add.setData(QtCore.Qt.UserRole, name)
                self.listWidget.addItem(self.item2add)


