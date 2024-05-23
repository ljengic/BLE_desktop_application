import sys
import time
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from package.patients.gui_select_patient import Ui_Patient_select

class Select_Patient(QtWidgets.QWidget, Ui_Patient_select):
    patient = pyqtSignal(str)
    
    def __init__(self, lock_app, unlock_app):
        super(Select_Patient, self).__init__()
        self.setupUi(self)

        self.lock_app = lock_app
        self.unlock_app = unlock_app

        self.btn_select.setEnabled(False)

        self.listWidget.itemClicked.connect(self.list_item_clicked)
        self.btn_cancle.clicked.connect(self.close_window)
        self.btn_select.clicked.connect(self.btn_select_clicked_handle)    

    def show_select_patient_window(self):
        self.refresh_patient_list()
        self.lock_app()
        self.show()

    def btn_select_clicked_handle(self):
        self.patient.emit(self.folder_path)
        self.close_window()

    def close_window(self):
        self.close()
        self.unlock_app()
        self = None

    def refresh_patient_list(self):
        self.listWidget.clear()
        for name in os.listdir("./data"):
            #print(os.getcwd() + "\data\\" +  name + "\\")
            if os.path.isdir(os.getcwd() + "\data\\" +  name + "\\"):
                print(name)
                self.item2add = QtWidgets.QListWidgetItem()
                self.item2add.setText(name)
                self.item2add.setData(QtCore.Qt.UserRole, name)
                self.listWidget.addItem(self.item2add)

    def list_item_clicked(self, itemC):
        self.folder_path = os.getcwd() + "\data\\" + itemC.data(QtCore.Qt.UserRole)
        self.btn_select.setEnabled(True)