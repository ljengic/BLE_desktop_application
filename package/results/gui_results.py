# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './package/results/gui_results.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Results(object):
    def setupUi(self, Results):
        Results.setObjectName("Results")
        Results.resize(969, 757)
        self.gridLayout = QtWidgets.QGridLayout(Results)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Results)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_13 = QtWidgets.QFrame(self.page_3)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.verticalLayout_12.addWidget(self.frame_13)
        self.line_3 = QtWidgets.QFrame(self.page_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_12.addWidget(self.line_3)
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setMinimumSize(QtCore.QSize(0, 50))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.frame_11 = QtWidgets.QFrame(self.page_3)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_select_patient = QtWidgets.QPushButton(self.frame_11)
        self.btn_select_patient.setMinimumSize(QtCore.QSize(200, 200))
        self.btn_select_patient.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btn_select_patient.setFont(font)
        self.btn_select_patient.setObjectName("btn_select_patient")
        self.gridLayout_2.addWidget(self.btn_select_patient, 0, 0, 1, 1)
        self.verticalLayout_12.addWidget(self.frame_11)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.widget_4 = QtWidgets.QWidget(self.page_4)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_back_main = QtWidgets.QPushButton(self.widget_4)
        self.btn_back_main.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_back_main.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_back_main.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-left-arrow-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back_main.setIcon(icon)
        self.btn_back_main.setObjectName("btn_back_main")
        self.horizontalLayout_7.addWidget(self.btn_back_main)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_14.addWidget(self.widget_4)
        self.frame_14 = QtWidgets.QFrame(self.page_4)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(35)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_name = QtWidgets.QLabel(self.frame_2)
        self.label_name.setMinimumSize(QtCore.QSize(0, 60))
        self.label_name.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.frame_29 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setMinimumSize(QtCore.QSize(330, 130))
        self.frame_29.setMaximumSize(QtCore.QSize(330, 130))
        self.frame_29.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_22 = QtWidgets.QLabel(self.frame_29)
        self.label_22.setMinimumSize(QtCore.QSize(0, 40))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_17.addWidget(self.label_22)
        self.frame_41 = QtWidgets.QFrame(self.frame_29)
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_32 = QtWidgets.QFrame(self.frame_41)
        self.frame_32.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_32.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_38 = QtWidgets.QFrame(self.frame_32)
        self.frame_38.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_38.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_38)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_23 = QtWidgets.QLabel(self.frame_38)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_19.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.frame_38)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_19.addWidget(self.label_24)
        self.horizontalLayout_11.addWidget(self.frame_38)
        self.widget_30 = QtWidgets.QWidget(self.frame_32)
        self.widget_30.setObjectName("widget_30")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.widget_30)
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_44.setSpacing(10)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.display_sex = QtWidgets.QLabel(self.widget_30)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_sex.setFont(font)
        self.display_sex.setText("")
        self.display_sex.setObjectName("display_sex")
        self.verticalLayout_44.addWidget(self.display_sex)
        self.display_age = QtWidgets.QLabel(self.widget_30)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_age.setFont(font)
        self.display_age.setObjectName("display_age")
        self.verticalLayout_44.addWidget(self.display_age)
        self.horizontalLayout_11.addWidget(self.widget_30)
        self.horizontalLayout_24.addWidget(self.frame_32)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem1)
        self.frame_39 = QtWidgets.QFrame(self.frame_41)
        self.frame_39.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_39.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_39)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_40 = QtWidgets.QFrame(self.frame_39)
        self.frame_40.setMinimumSize(QtCore.QSize(60, 0))
        self.frame_40.setMaximumSize(QtCore.QSize(60, 16777215))
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.frame_40)
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_45.setSpacing(10)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.label_8 = QtWidgets.QLabel(self.frame_40)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_45.addWidget(self.label_8)
        self.label_49 = QtWidgets.QLabel(self.frame_40)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.verticalLayout_45.addWidget(self.label_49)
        self.label_50 = QtWidgets.QLabel(self.frame_40)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.verticalLayout_45.addWidget(self.label_50)
        self.horizontalLayout_23.addWidget(self.frame_40)
        self.widget_31 = QtWidgets.QWidget(self.frame_39)
        self.widget_31.setObjectName("widget_31")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.widget_31)
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_46.setSpacing(10)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.display_height = QtWidgets.QLabel(self.widget_31)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_height.setFont(font)
        self.display_height.setObjectName("display_height")
        self.verticalLayout_46.addWidget(self.display_height)
        self.display_weight = QtWidgets.QLabel(self.widget_31)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_weight.setFont(font)
        self.display_weight.setObjectName("display_weight")
        self.verticalLayout_46.addWidget(self.display_weight)
        self.display_bmi = QtWidgets.QLabel(self.widget_31)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_bmi.setFont(font)
        self.display_bmi.setObjectName("display_bmi")
        self.verticalLayout_46.addWidget(self.display_bmi)
        self.horizontalLayout_23.addWidget(self.widget_31)
        self.horizontalLayout_24.addWidget(self.frame_39)
        self.verticalLayout_17.addWidget(self.frame_41)
        self.verticalLayout.addWidget(self.frame_29)
        self.frame_16 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMinimumSize(QtCore.QSize(330, 150))
        self.frame_16.setMaximumSize(QtCore.QSize(330, 150))
        self.frame_16.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_19 = QtWidgets.QLabel(self.frame_16)
        self.label_19.setMinimumSize(QtCore.QSize(0, 40))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_15.addWidget(self.label_19)
        self.frame_17 = QtWidgets.QFrame(self.frame_16)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_12 = QtWidgets.QFrame(self.frame_17)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.frame_12)
        self.label_16.setMinimumSize(QtCore.QSize(0, 20))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.frame_27 = QtWidgets.QFrame(self.frame_12)
        self.frame_27.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_27.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_28 = QtWidgets.QFrame(self.frame_27)
        self.frame_28.setMinimumSize(QtCore.QSize(60, 0))
        self.frame_28.setMaximumSize(QtCore.QSize(60, 16777215))
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_18.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.frame_28)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_18.addWidget(self.label_18)
        self.horizontalLayout_8.addWidget(self.frame_28)
        self.widget_28 = QtWidgets.QWidget(self.frame_27)
        self.widget_28.setObjectName("widget_28")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.widget_28)
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_42.setSpacing(10)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.display_chest_upper = QtWidgets.QLabel(self.widget_28)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_chest_upper.setFont(font)
        self.display_chest_upper.setObjectName("display_chest_upper")
        self.verticalLayout_42.addWidget(self.display_chest_upper)
        self.display_chest_lower = QtWidgets.QLabel(self.widget_28)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_chest_lower.setFont(font)
        self.display_chest_lower.setObjectName("display_chest_lower")
        self.verticalLayout_42.addWidget(self.display_chest_lower)
        self.horizontalLayout_8.addWidget(self.widget_28)
        self.verticalLayout_5.addWidget(self.frame_27)
        self.horizontalLayout_10.addWidget(self.frame_12)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.frame_8 = QtWidgets.QFrame(self.frame_17)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        self.label_6.setMinimumSize(QtCore.QSize(0, 20))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.frame_30 = QtWidgets.QFrame(self.frame_8)
        self.frame_30.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_30.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_31 = QtWidgets.QFrame(self.frame_30)
        self.frame_31.setMinimumSize(QtCore.QSize(60, 0))
        self.frame_31.setMaximumSize(QtCore.QSize(60, 16777215))
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(10)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_7 = QtWidgets.QLabel(self.frame_31)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_31.addWidget(self.label_7)
        self.label_11 = QtWidgets.QLabel(self.frame_31)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_31.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_31)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_31.addWidget(self.label_12)
        self.horizontalLayout_3.addWidget(self.frame_31)
        self.widget_29 = QtWidgets.QWidget(self.frame_30)
        self.widget_29.setObjectName("widget_29")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.widget_29)
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_43.setSpacing(10)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.display_leg_ankle = QtWidgets.QLabel(self.widget_29)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_leg_ankle.setFont(font)
        self.display_leg_ankle.setObjectName("display_leg_ankle")
        self.verticalLayout_43.addWidget(self.display_leg_ankle)
        self.display_leg_calf = QtWidgets.QLabel(self.widget_29)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_leg_calf.setFont(font)
        self.display_leg_calf.setObjectName("display_leg_calf")
        self.verticalLayout_43.addWidget(self.display_leg_calf)
        self.display_leg_knee = QtWidgets.QLabel(self.widget_29)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_leg_knee.setFont(font)
        self.display_leg_knee.setObjectName("display_leg_knee")
        self.verticalLayout_43.addWidget(self.display_leg_knee)
        self.horizontalLayout_3.addWidget(self.widget_29)
        self.verticalLayout_7.addWidget(self.frame_30)
        self.horizontalLayout_10.addWidget(self.frame_8)
        self.verticalLayout_15.addWidget(self.frame_17)
        self.verticalLayout.addWidget(self.frame_16)
        self.frame_20 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMinimumSize(QtCore.QSize(330, 0))
        self.frame_20.setMaximumSize(QtCore.QSize(330, 16777215))
        self.frame_20.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setLineWidth(1)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_21 = QtWidgets.QFrame(self.frame_20)
        self.frame_21.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_21.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_32 = QtWidgets.QLabel(self.frame_21)
        self.label_32.setMinimumSize(QtCore.QSize(150, 0))
        self.label_32.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_15.addWidget(self.label_32)
        self.verticalLayout_16.addWidget(self.frame_21)
        self.line_2 = QtWidgets.QFrame(self.frame_20)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_16.addWidget(self.line_2)
        self.frame_24 = QtWidgets.QFrame(self.frame_20)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.widget_no_med = QtWidgets.QWidget(self.frame_24)
        self.widget_no_med.setObjectName("widget_no_med")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.widget_no_med)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_33 = QtWidgets.QLabel(self.widget_no_med)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_24.addWidget(self.label_33)
        self.verticalLayout_23.addWidget(self.widget_no_med)
        self.verticalLayout_16.addWidget(self.frame_24)
        self.verticalLayout.addWidget(self.frame_20)
        self.verticalLayout_8.addWidget(self.frame_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.line_4 = QtWidgets.QFrame(self.frame_14)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setLineWidth(3)
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.frame = QtWidgets.QFrame(self.frame_14)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(350, 400))
        self.frame_3.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.verticalLayout_10.addWidget(self.frame_4)
        self.frame_15 = QtWidgets.QFrame(self.frame_3)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.listWidget = QtWidgets.QListWidget(self.frame_15)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_6.addWidget(self.listWidget)
        self.verticalLayout_10.addWidget(self.frame_15)
        self.verticalLayout_13.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.verticalLayout_11.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(134, 37, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btn_show = QtWidgets.QPushButton(self.frame_6)
        self.btn_show.setMinimumSize(QtCore.QSize(150, 40))
        self.btn_show.setObjectName("btn_show")
        self.horizontalLayout.addWidget(self.btn_show)
        self.verticalLayout_11.addWidget(self.frame_6)
        self.verticalLayout_13.addWidget(self.frame_5)
        self.horizontalLayout_2.addWidget(self.frame)
        spacerItem5 = QtWidgets.QSpacerItem(295, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_14.addWidget(self.frame_14)
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_9 = QtWidgets.QFrame(self.page_2)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_9.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_back = QtWidgets.QPushButton(self.frame_9)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_4.addWidget(self.btn_back)
        spacerItem6 = QtWidgets.QSpacerItem(732, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Results)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        _translate = QtCore.QCoreApplication.translate
        Results.setWindowTitle(_translate("Results", "Form"))
        self.label_3.setText(_translate("Results", "Previous results"))
        self.label_4.setText(_translate("Results", "Here you can see all previous measurments and analysis"))
        self.label_5.setText(_translate("Results", "To proceed click Select Patient button and choose patient"))
        self.btn_select_patient.setText(_translate("Results", "Select Patient"))
        self.btn_back_main.setText(_translate("Results", "Back"))
        self.label_name.setText(_translate("Results", "KOJI JE TO POKEMONNNN?"))
        self.label_22.setText(_translate("Results", "General info"))
        self.label_23.setText(_translate("Results", "Sex:"))
        self.label_24.setText(_translate("Results", "Age:"))
        self.display_age.setText(_translate("Results", "120 "))
        self.label_8.setText(_translate("Results", "Height:"))
        self.label_49.setText(_translate("Results", "Weight:"))
        self.label_50.setText(_translate("Results", "BMI:"))
        self.display_height.setText(_translate("Results", "190"))
        self.display_weight.setText(_translate("Results", "70"))
        self.display_bmi.setText(_translate("Results", "20.2"))
        self.label_19.setText(_translate("Results", "Circumfences"))
        self.label_16.setText(_translate("Results", "Chest:"))
        self.label_17.setText(_translate("Results", "Upper"))
        self.label_18.setText(_translate("Results", "Lower"))
        self.display_chest_upper.setText(_translate("Results", "20"))
        self.display_chest_lower.setText(_translate("Results", "20"))
        self.label_6.setText(_translate("Results", "Leg:"))
        self.label_7.setText(_translate("Results", "Ankle"))
        self.label_11.setText(_translate("Results", "Calf"))
        self.label_12.setText(_translate("Results", "Knee"))
        self.display_leg_ankle.setText(_translate("Results", "20"))
        self.display_leg_calf.setText(_translate("Results", "20"))
        self.display_leg_knee.setText(_translate("Results", "20"))
        self.label_32.setText(_translate("Results", "Medications"))
        self.label_33.setText(_translate("Results", "No medications"))
        self.label_9.setText(_translate("Results", "List of measurments found:"))
        self.label_2.setText(_translate("Results", "Neki izbornik sta se zeli\n"
"prikazat od rezultata"))
        self.btn_show.setText(_translate("Results", "Show results"))
        self.btn_back.setText(_translate("Results", "Back"))
        self.label.setText(_translate("Results", "TextLabel"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Results = QtWidgets.QWidget()
    ui = Ui_Results()
    ui.setupUi(Results)
    Results.show()
    sys.exit(app.exec_())
