# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'processmonitor.ui'
#
# Created: Mon Feb 18 14:36:06 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProcessMonitor(object):
    def setupUi(self, ProcessMonitor):
        ProcessMonitor.setObjectName("ProcessMonitor")
        ProcessMonitor.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(ProcessMonitor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtGui.QTableView(ProcessMonitor)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(ProcessMonitor)
        QtCore.QMetaObject.connectSlotsByName(ProcessMonitor)

    def retranslateUi(self, ProcessMonitor):
        ProcessMonitor.setWindowTitle(QtGui.QApplication.translate("ProcessMonitor", "Form", None, QtGui.QApplication.UnicodeUTF8))

