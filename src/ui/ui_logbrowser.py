# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logbrowser.ui'
#
# Created: Fri May 10 15:25:34 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LogBrowser(object):
    def setupUi(self, LogBrowser):
        LogBrowser.setObjectName("LogBrowser")
        LogBrowser.resize(586, 440)
        self.verticalLayout = QtGui.QVBoxLayout(LogBrowser)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtGui.QComboBox(LogBrowser)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtGui.QTextBrowser(LogBrowser)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(LogBrowser)
        QtCore.QMetaObject.connectSlotsByName(LogBrowser)

    def retranslateUi(self, LogBrowser):
        LogBrowser.setWindowTitle(QtGui.QApplication.translate("LogBrowser", "Form", None, QtGui.QApplication.UnicodeUTF8))

