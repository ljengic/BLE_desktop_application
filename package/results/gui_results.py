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
        Results.resize(580, 458)
        self.gridLayout = QtWidgets.QGridLayout(Results)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Results)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        _translate = QtCore.QCoreApplication.translate
        Results.setWindowTitle(_translate("Results", "Form"))
        self.label.setText(_translate("Results", "Results page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Results = QtWidgets.QWidget()
    ui = Ui_Results()
    ui.setupUi(Results)
    Results.show()
    sys.exit(app.exec_())
