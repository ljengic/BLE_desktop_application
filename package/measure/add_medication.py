import sys
import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from package.measure.gui_add_medication import Ui_Add_Medication

class Add_Medication(QtWidgets.QWidget, Ui_Add_Medication):
    medicine = pyqtSignal(str)
    
    def __init__(self, lock_app, unlock_app):
        super(Add_Medication, self).__init__()
        self.setupUi(self)

        self.lock_app = lock_app
        self.unlock_app = unlock_app

        self.btn_cancle.clicked.connect(self.close_window)
        self.btn_add.clicked.connect(self.btn_add_clicked_handle)    

    def show_add_medicine_window(self):
        self.input_medication.clear() 
        self.input_medication.setFocus(True)
        self.lock_app()
        self.show()

    def btn_add_clicked_handle(self):
        self.text = self.input_medication.text()
        if("" != self.text):   
            self.medicine.emit(self.text)
            self.close_window()

    def close_window(self):
        self.close()
        self.unlock_app()
        self = None