import sys
import time
from PyQt5 import QtWidgets, QtCore
from package.medicine.gui_medicine import Ui_Medicine

class Medicine(QtWidgets.QWidget, Ui_Medicine):
    def __init__(self, parent, medicine_name, remove_func):
        super(Medicine, self).__init__(parent)
        self.setupUi(self)
        self.medicine_name = medicine_name
        self.label.setText(self.medicine_name)
        if(None == remove_func):
            self.btn_remove.hide()
        else:
            self.remove_func = remove_func
            self.btn_remove.clicked.connect(self.remove)

    def remove(self):
        self.remove_func(self,self.medicine_name)

