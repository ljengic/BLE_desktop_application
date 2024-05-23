# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './package/measure/gui_measure.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Measure(object):
    def setupUi(self, Measure):
        Measure.setObjectName("Measure")
        Measure.resize(1021, 801)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Measure)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(Measure)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.bnt_new_patient = QtWidgets.QPushButton(self.page)
        self.bnt_new_patient.setMinimumSize(QtCore.QSize(200, 200))
        self.bnt_new_patient.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bnt_new_patient.setFont(font)
        self.bnt_new_patient.setObjectName("bnt_new_patient")
        self.horizontalLayout_17.addWidget(self.bnt_new_patient)
        self.btn_select_patient = QtWidgets.QPushButton(self.page)
        self.btn_select_patient.setMinimumSize(QtCore.QSize(200, 200))
        self.btn_select_patient.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_select_patient.setFont(font)
        self.btn_select_patient.setObjectName("btn_select_patient")
        self.horizontalLayout_17.addWidget(self.btn_select_patient)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.widget_3 = QtWidgets.QWidget(self.page_2)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(322, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_22.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.page_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame = QtWidgets.QFrame(self.widget_4)
        self.frame.setMinimumSize(QtCore.QSize(300, 300))
        self.frame.setMaximumSize(QtCore.QSize(300, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.input_age = QtWidgets.QLineEdit(self.frame_3)
        self.input_age.setObjectName("input_age")
        self.verticalLayout_3.addWidget(self.input_age)
        self.input_height = QtWidgets.QLineEdit(self.frame_3)
        self.input_height.setObjectName("input_height")
        self.verticalLayout_3.addWidget(self.input_height)
        self.input_weight = QtWidgets.QLineEdit(self.frame_3)
        self.input_weight.setObjectName("input_weight")
        self.verticalLayout_3.addWidget(self.input_weight)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.widget_6 = QtWidgets.QWidget(self.frame_2)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_female = QtWidgets.QRadioButton(self.frame_4)
        self.btn_female.setObjectName("btn_female")
        self.horizontalLayout_5.addWidget(self.btn_female)
        self.btn_male = QtWidgets.QRadioButton(self.frame_4)
        self.btn_male.setObjectName("btn_male")
        self.horizontalLayout_5.addWidget(self.btn_male)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.horizontalLayout_9.addWidget(self.frame)
        self.frame_14 = QtWidgets.QFrame(self.widget_4)
        self.frame_14.setMinimumSize(QtCore.QSize(500, 300))
        self.frame_14.setMaximumSize(QtCore.QSize(500, 300))
        self.frame_14.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_19 = QtWidgets.QLabel(self.frame_14)
        self.label_19.setMinimumSize(QtCore.QSize(0, 50))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_15.addWidget(self.label_19)
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_10 = QtWidgets.QFrame(self.frame_15)
        self.frame_10.setMinimumSize(QtCore.QSize(190, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(190, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_16 = QtWidgets.QLabel(self.frame_10)
        self.label_16.setMinimumSize(QtCore.QSize(0, 20))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_17 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_12.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_12.addWidget(self.label_18)
        self.horizontalLayout_7.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.input_chest_upper = QtWidgets.QLineEdit(self.frame_13)
        self.input_chest_upper.setObjectName("input_chest_upper")
        self.verticalLayout_13.addWidget(self.input_chest_upper)
        self.input_chest_lower = QtWidgets.QLineEdit(self.frame_13)
        self.input_chest_lower.setObjectName("input_chest_lower")
        self.verticalLayout_13.addWidget(self.input_chest_lower)
        self.horizontalLayout_7.addWidget(self.frame_13)
        self.widget_8 = QtWidgets.QWidget(self.frame_11)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_20 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_14.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_14.addWidget(self.label_21)
        self.horizontalLayout_7.addWidget(self.widget_8)
        self.verticalLayout_8.addWidget(self.frame_11)
        self.horizontalLayout_8.addWidget(self.frame_10)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.frame_6 = QtWidgets.QFrame(self.frame_15)
        self.frame_6.setMinimumSize(QtCore.QSize(190, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(190, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.input_leg_ankle = QtWidgets.QLineEdit(self.frame_9)
        self.input_leg_ankle.setObjectName("input_leg_ankle")
        self.verticalLayout_10.addWidget(self.input_leg_ankle)
        self.input_leg_calf = QtWidgets.QLineEdit(self.frame_9)
        self.input_leg_calf.setObjectName("input_leg_calf")
        self.verticalLayout_10.addWidget(self.input_leg_calf)
        self.input_leg_knee = QtWidgets.QLineEdit(self.frame_9)
        self.input_leg_knee.setObjectName("input_leg_knee")
        self.verticalLayout_10.addWidget(self.input_leg_knee)
        self.horizontalLayout_4.addWidget(self.frame_9)
        self.widget_7 = QtWidgets.QWidget(self.frame_7)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_11.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_11.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_11.addWidget(self.label_15)
        self.horizontalLayout_4.addWidget(self.widget_7)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.horizontalLayout_8.addWidget(self.frame_6)
        self.verticalLayout_15.addWidget(self.frame_15)
        self.horizontalLayout_9.addWidget(self.frame_14)
        spacerItem2 = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_22.addWidget(self.widget_4)
        self.widget_12 = QtWidgets.QWidget(self.page_2)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_18 = QtWidgets.QFrame(self.widget_12)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_18.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_18.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setLineWidth(1)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_25 = QtWidgets.QLabel(self.frame_19)
        self.label_25.setMinimumSize(QtCore.QSize(150, 0))
        self.label_25.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_14.addWidget(self.label_25)
        spacerItem3 = QtWidgets.QSpacerItem(56, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.btn_add_medication = QtWidgets.QPushButton(self.frame_19)
        self.btn_add_medication.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_add_medication.setMaximumSize(QtCore.QSize(100, 30))
        self.btn_add_medication.setObjectName("btn_add_medication")
        self.horizontalLayout_14.addWidget(self.btn_add_medication)
        self.verticalLayout_16.addWidget(self.frame_19)
        self.line = QtWidgets.QFrame(self.frame_18)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_16.addWidget(self.line)
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.widget_no_med = QtWidgets.QWidget(self.frame_20)
        self.widget_no_med.setObjectName("widget_no_med")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.widget_no_med)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_26 = QtWidgets.QLabel(self.widget_no_med)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_20.addWidget(self.label_26)
        self.verticalLayout_21.addWidget(self.widget_no_med)
        self.verticalLayout_16.addWidget(self.frame_20)
        self.horizontalLayout_15.addWidget(self.frame_18)
        spacerItem4 = QtWidgets.QSpacerItem(622, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem4)
        self.verticalLayout_22.addWidget(self.widget_12)
        spacerItem5 = QtWidgets.QSpacerItem(20, 67, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem5)
        self.widget_5 = QtWidgets.QWidget(self.page_2)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(637, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.btn_complete = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_complete.sizePolicy().hasHeightForWidth())
        self.btn_complete.setSizePolicy(sizePolicy)
        self.btn_complete.setMinimumSize(QtCore.QSize(150, 40))
        self.btn_complete.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_complete.setFont(font)
        self.btn_complete.setObjectName("btn_complete")
        self.horizontalLayout_2.addWidget(self.btn_complete)
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_22.addWidget(self.widget_5)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_top = QtWidgets.QWidget(self.page_3)
        self.widget_top.setMinimumSize(QtCore.QSize(0, 140))
        self.widget_top.setMaximumSize(QtCore.QSize(16777215, 140))
        self.widget_top.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_top.setObjectName("widget_top")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_top)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_16 = QtWidgets.QFrame(self.widget_top)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setSpacing(50)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.widget_11 = QtWidgets.QWidget(self.frame_16)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_22 = QtWidgets.QFrame(self.widget_11)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_28 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_19.addWidget(self.label_28)
        self.label_30 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_19.addWidget(self.label_30)
        self.horizontalLayout_11.addWidget(self.frame_22)
        self.widget_14 = QtWidgets.QWidget(self.widget_11)
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(10)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.display_sex = QtWidgets.QLabel(self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_sex.setFont(font)
        self.display_sex.setObjectName("display_sex")
        self.verticalLayout_26.addWidget(self.display_sex)
        self.display_age = QtWidgets.QLabel(self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_age.setFont(font)
        self.display_age.setObjectName("display_age")
        self.verticalLayout_26.addWidget(self.display_age)
        self.horizontalLayout_11.addWidget(self.widget_14)
        self.horizontalLayout_12.addWidget(self.widget_11)
        self.widget_10 = QtWidgets.QWidget(self.frame_16)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_17 = QtWidgets.QFrame(self.widget_10)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_22 = QtWidgets.QLabel(self.frame_17)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_17.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.frame_17)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_17.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.frame_17)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_17.addWidget(self.label_24)
        self.horizontalLayout.addWidget(self.frame_17)
        self.widget_9 = QtWidgets.QWidget(self.widget_10)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.display_height = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_height.setFont(font)
        self.display_height.setObjectName("display_height")
        self.verticalLayout_18.addWidget(self.display_height)
        self.display_weight = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_weight.setFont(font)
        self.display_weight.setObjectName("display_weight")
        self.verticalLayout_18.addWidget(self.display_weight)
        self.display_bmi = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_bmi.setFont(font)
        self.display_bmi.setObjectName("display_bmi")
        self.verticalLayout_18.addWidget(self.display_bmi)
        self.horizontalLayout.addWidget(self.widget_9)
        self.horizontalLayout_12.addWidget(self.widget_10)
        self.horizontalLayout_16.addWidget(self.frame_16)
        spacerItem8 = QtWidgets.QSpacerItem(379, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem8)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.widget_top)
        self.stackedWidget_2.setMinimumSize(QtCore.QSize(200, 0))
        self.stackedWidget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.page_4)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btn_start = QtWidgets.QPushButton(self.page_4)
        self.btn_start.setMinimumSize(QtCore.QSize(140, 40))
        self.btn_start.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_13.addWidget(self.btn_start)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.page_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_stop = QtWidgets.QPushButton(self.page_5)
        self.btn_stop.setMinimumSize(QtCore.QSize(140, 40))
        self.btn_stop.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_10.addWidget(self.btn_stop)
        self.stackedWidget_2.addWidget(self.page_5)
        self.horizontalLayout_16.addWidget(self.stackedWidget_2)
        self.verticalLayout.addWidget(self.widget_top)
        self.widget_2 = QtWidgets.QWidget(self.page_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_27 = QtWidgets.QLabel(self.widget_2)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_25.addWidget(self.label_27)
        self.verticalLayout.addWidget(self.widget_2)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_6.addWidget(self.stackedWidget)

        self.retranslateUi(Measure)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Measure)

    def retranslateUi(self, Measure):
        _translate = QtCore.QCoreApplication.translate
        Measure.setWindowTitle(_translate("Measure", "Form"))
        self.bnt_new_patient.setText(_translate("Measure", "Add new patient"))
        self.btn_select_patient.setText(_translate("Measure", "Select Patient \n"
"from database"))
        self.label_2.setText(_translate("Measure", "Please fill patient iformation:"))
        self.label.setText(_translate("Measure", "General information"))
        self.label_4.setText(_translate("Measure", "Age"))
        self.label_6.setText(_translate("Measure", "Height"))
        self.label_7.setText(_translate("Measure", "Weight"))
        self.label_8.setText(_translate("Measure", "years"))
        self.label_9.setText(_translate("Measure", "cm"))
        self.label_10.setText(_translate("Measure", "kg"))
        self.btn_female.setText(_translate("Measure", "Female"))
        self.btn_male.setText(_translate("Measure", "Male"))
        self.label_19.setText(_translate("Measure", "Circumfence"))
        self.label_16.setText(_translate("Measure", "Chest:"))
        self.label_17.setText(_translate("Measure", "Upper"))
        self.label_18.setText(_translate("Measure", "Lower"))
        self.label_20.setText(_translate("Measure", "cm"))
        self.label_21.setText(_translate("Measure", "cm"))
        self.label_3.setText(_translate("Measure", "Leg:"))
        self.label_5.setText(_translate("Measure", "Ankle"))
        self.label_11.setText(_translate("Measure", "Calf"))
        self.label_12.setText(_translate("Measure", "Knee"))
        self.label_13.setText(_translate("Measure", "cm"))
        self.label_14.setText(_translate("Measure", "cm"))
        self.label_15.setText(_translate("Measure", "cm"))
        self.label_25.setText(_translate("Measure", "Medications"))
        self.btn_add_medication.setText(_translate("Measure", "Add new"))
        self.label_26.setText(_translate("Measure", "No medications"))
        self.btn_complete.setText(_translate("Measure", "Complete"))
        self.label_28.setText(_translate("Measure", "Sex:"))
        self.label_30.setText(_translate("Measure", "Age:"))
        self.display_sex.setText(_translate("Measure", "male"))
        self.display_age.setText(_translate("Measure", "120 years"))
        self.label_22.setText(_translate("Measure", "Height:"))
        self.label_23.setText(_translate("Measure", "Weight:"))
        self.label_24.setText(_translate("Measure", "BMI:"))
        self.display_height.setText(_translate("Measure", "190 cm"))
        self.display_weight.setText(_translate("Measure", "70 kg"))
        self.display_bmi.setText(_translate("Measure", "20.2"))
        self.btn_start.setText(_translate("Measure", "Start"))
        self.btn_stop.setText(_translate("Measure", "Stop"))
        self.label_27.setText(_translate("Measure", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Measure = QtWidgets.QWidget()
    ui = Ui_Measure()
    ui.setupUi(Measure)
    Measure.show()
    sys.exit(app.exec_())
