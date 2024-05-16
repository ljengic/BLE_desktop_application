import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QColor
from package.graphs.gui_check_box_widget import Ui_Check_box_widget

class Check_Box_Widget(QtWidgets.QWidget, Ui_Check_box_widget):
    def __init__(self, parent, text, color):
        super(Check_Box_Widget, self).__init__(parent)
        self.setupUi(self)
        self.text = text
        #self.checkBox.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px;}")
        self.checkBox.setText(self.text)
        self.checkBox.setChecked(True)

        palette = QtGui.QPalette()
        if(color == 'r'):
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        elif(color == 'b'):
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        elif(color == 'g'):
            brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        else:
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.line.setPalette(palette)

    def change_bakground_color(self, checked):
        if(True == checked):
            self.setStyleSheet('background-color: #FFFFFF;')
            self.line.show()
        else:
            self.setStyleSheet('background-color: #AAAAAA;')
            self.line.hide()

    