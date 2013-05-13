# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logbrowser.ui'
#
# Created: Sat May 11 11:36:15 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
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
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtGui.QTextBrowser(LogBrowser)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(LogBrowser)
        QtCore.QMetaObject.connectSlotsByName(LogBrowser)

    def retranslateUi(self, LogBrowser):
        LogBrowser.setWindowTitle(QtGui.QApplication.translate("LogBrowser", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("LogBrowser", "Syslog - /var/log/syslog", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("LogBrowser", "Messages - /var/log/messages", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("LogBrowser", "Kernel - /var/log/kern.log", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("LogBrowser", "Auth - /var/log/auth.log", None, QtGui.QApplication.UnicodeUTF8))

