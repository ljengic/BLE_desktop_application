# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './package/patients/gui_select_patient.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Patient_select(object):
    def setupUi(self, Patient_select):
        Patient_select.setObjectName("Patient_select")
        Patient_select.resize(249, 344)
        Patient_select.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(Patient_select)
        self.gridLayout.setContentsMargins(10, 0, 10, 10)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Patient_select)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancle = QtWidgets.QPushButton(self.widget)
        self.btn_cancle.setObjectName("btn_cancle")
        self.horizontalLayout.addWidget(self.btn_cancle)
        self.btn_select = QtWidgets.QPushButton(self.widget)
        self.btn_select.setDefault(True)
        self.btn_select.setObjectName("btn_select")
        self.horizontalLayout.addWidget(self.btn_select)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout.addWidget(self.frame_2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Patient_select)
        QtCore.QMetaObject.connectSlotsByName(Patient_select)

    def retranslateUi(self, Patient_select):
        _translate = QtCore.QCoreApplication.translate
        Patient_select.setWindowTitle(_translate("Patient_select", "Form"))
        self.label.setText(_translate("Patient_select", "Please select one of the\n"
"patient in database:"))
        self.btn_cancle.setText(_translate("Patient_select", "Cancle"))
        self.btn_select.setText(_translate("Patient_select", "Select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Patient_select = QtWidgets.QWidget()
    ui = Ui_Patient_select()
    ui.setupUi(Patient_select)
    Patient_select.show()
    sys.exit(app.exec_())
