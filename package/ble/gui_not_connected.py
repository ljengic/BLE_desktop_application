# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './package/ble/gui_not_connected.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BLE_not_connected(object):
    def setupUi(self, BLE_not_connected):
        BLE_not_connected.setObjectName("BLE_not_connected")
        BLE_not_connected.resize(253, 197)
        self.gridLayout = QtWidgets.QGridLayout(BLE_not_connected)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(BLE_not_connected)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(40, 40))
        self.label_4.setMaximumSize(QtCore.QSize(40, 40))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/icons/icons8-error-100.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(143, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_connect = QtWidgets.QPushButton(self.widget)
        self.btn_connect.setDefault(True)
        self.btn_connect.setObjectName("btn_connect")
        self.horizontalLayout.addWidget(self.btn_connect)
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(BLE_not_connected)
        QtCore.QMetaObject.connectSlotsByName(BLE_not_connected)

    def retranslateUi(self, BLE_not_connected):
        _translate = QtCore.QCoreApplication.translate
        BLE_not_connected.setWindowTitle(_translate("BLE_not_connected", "Form"))
        self.label.setText(_translate("BLE_not_connected", "Device not connected!"))
        self.label_2.setText(_translate("BLE_not_connected", "Details:"))
        self.label_3.setText(_translate("BLE_not_connected", "You cannot measure until BLE device\n"
" is connected"))
        self.btn_connect.setText(_translate("BLE_not_connected", "Connect"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BLE_not_connected = QtWidgets.QWidget()
    ui = Ui_BLE_not_connected()
    ui.setupUi(BLE_not_connected)
    BLE_not_connected.show()
    sys.exit(app.exec_())
