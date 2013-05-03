# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpuchart.ui'
#
# Created: Fri May  3 11:07:02 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CpuChart(object):
    def setupUi(self, CpuChart):
        CpuChart.setObjectName("CpuChart")
        CpuChart.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(CpuChart)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(CpuChart)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cpuChart = Chart(self.groupBox)
        self.cpuChart.setObjectName("cpuChart")
        self.verticalLayout.addWidget(self.cpuChart)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(CpuChart)
        QtCore.QMetaObject.connectSlotsByName(CpuChart)

    def retranslateUi(self, CpuChart):
        CpuChart.setWindowTitle(QtGui.QApplication.translate("CpuChart", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CpuChart", "CPU", None, QtGui.QApplication.UnicodeUTF8))

from app.chart import Chart
