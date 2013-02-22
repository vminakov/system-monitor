# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memorymonitor.ui'
#
# Created: Mon Feb 18 11:58:30 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MemoryMonitor(object):
    def setupUi(self, MemoryMonitor):
        MemoryMonitor.setObjectName("MemoryMonitor")
        MemoryMonitor.resize(400, 279)
        self.label = QtGui.QLabel(MemoryMonitor)
        self.label.setGeometry(QtCore.QRect(160, 90, 161, 51))
        self.label.setObjectName("label")

        self.retranslateUi(MemoryMonitor)
        QtCore.QMetaObject.connectSlotsByName(MemoryMonitor)

    def retranslateUi(self, MemoryMonitor):
        MemoryMonitor.setWindowTitle(QtGui.QApplication.translate("MemoryMonitor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MemoryMonitor", "Memory Monitor", None, QtGui.QApplication.UnicodeUTF8))

