# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'systemwindow.ui'
#
# Created: Fri May  3 15:56:39 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SystemWindow(object):
    def setupUi(self, SystemWindow):
        SystemWindow.setObjectName("SystemWindow")
        SystemWindow.resize(654, 474)
        self.horizontalLayout = QtGui.QHBoxLayout(SystemWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(SystemWindow)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/system-monitor.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.infoWidget = QtGui.QWidget(SystemWindow)
        self.infoWidget.setObjectName("infoWidget")
        self.horizontalLayout.addWidget(self.infoWidget)
        spacerItem1 = QtGui.QSpacerItem(481, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(SystemWindow)
        QtCore.QMetaObject.connectSlotsByName(SystemWindow)

    def retranslateUi(self, SystemWindow):
        SystemWindow.setWindowTitle(QtGui.QApplication.translate("SystemWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))

import application_rc
