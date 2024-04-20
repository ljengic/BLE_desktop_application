# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './package/ble/gui_ble.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BLE(object):
    def setupUi(self, BLE):
        BLE.setObjectName("BLE")
        BLE.resize(919, 704)
        self.verticalLayout = QtWidgets.QVBoxLayout(BLE)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(BLE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(150)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(BLE)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_scan = QtWidgets.QPushButton(self.frame_3)
        self.btn_scan.setObjectName("btn_scan")
        self.horizontalLayout_2.addWidget(self.btn_scan)
        spacerItem = QtWidgets.QSpacerItem(283, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.frame_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_connect = QtWidgets.QPushButton(self.widget_3)
        self.btn_connect.setObjectName("btn_connect")
        self.horizontalLayout_3.addWidget(self.btn_connect)
        spacerItem1 = QtWidgets.QSpacerItem(285, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.frame_2)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_4)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_3.addWidget(self.listWidget_2, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(BLE)
        QtCore.QMetaObject.connectSlotsByName(BLE)

    def retranslateUi(self, BLE):
        _translate = QtCore.QCoreApplication.translate
        BLE.setWindowTitle(_translate("BLE", "Form"))
        self.label.setText(_translate("BLE", "Neke gluposti"))
        self.btn_scan.setText(_translate("BLE", "Scan"))
        self.btn_connect.setText(_translate("BLE", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BLE = QtWidgets.QWidget()
    ui = Ui_BLE()
    ui.setupUi(BLE)
    BLE.show()
    sys.exit(app.exec_())