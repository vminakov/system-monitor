# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'networkinfo.ui'
#
# Created: Fri May  3 13:29:24 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NetworkInfo(object):
    def setupUi(self, NetworkInfo):
        NetworkInfo.setObjectName("NetworkInfo")
        NetworkInfo.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(NetworkInfo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(NetworkInfo)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.labelBytesSentTotal = QtGui.QLabel(self.groupBox)
        self.labelBytesSentTotal.setObjectName("labelBytesSentTotal")
        self.gridLayout.addWidget(self.labelBytesSentTotal, 0, 1, 1, 1)
        self.labelBytesSentSpeed = QtGui.QLabel(self.groupBox)
        self.labelBytesSentSpeed.setObjectName("labelBytesSentSpeed")
        self.gridLayout.addWidget(self.labelBytesSentSpeed, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.labelBytesReceivedTotal = QtGui.QLabel(self.groupBox)
        self.labelBytesReceivedTotal.setObjectName("labelBytesReceivedTotal")
        self.gridLayout.addWidget(self.labelBytesReceivedTotal, 1, 1, 1, 1)
        self.labelBytesReceivedSpeed = QtGui.QLabel(self.groupBox)
        self.labelBytesReceivedSpeed.setObjectName("labelBytesReceivedSpeed")
        self.gridLayout.addWidget(self.labelBytesReceivedSpeed, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.labelPacketsSentTotal = QtGui.QLabel(self.groupBox)
        self.labelPacketsSentTotal.setObjectName("labelPacketsSentTotal")
        self.gridLayout.addWidget(self.labelPacketsSentTotal, 2, 1, 1, 1)
        self.labelPacketsSentSpeed = QtGui.QLabel(self.groupBox)
        self.labelPacketsSentSpeed.setObjectName("labelPacketsSentSpeed")
        self.gridLayout.addWidget(self.labelPacketsSentSpeed, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.labelPacketsReceivedTotal = QtGui.QLabel(self.groupBox)
        self.labelPacketsReceivedTotal.setObjectName("labelPacketsReceivedTotal")
        self.gridLayout.addWidget(self.labelPacketsReceivedTotal, 3, 1, 1, 1)
        self.labelPacketsReceivedSpeed = QtGui.QLabel(self.groupBox)
        self.labelPacketsReceivedSpeed.setObjectName("labelPacketsReceivedSpeed")
        self.gridLayout.addWidget(self.labelPacketsReceivedSpeed, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(NetworkInfo)
        QtCore.QMetaObject.connectSlotsByName(NetworkInfo)

    def retranslateUi(self, NetworkInfo):
        NetworkInfo.setWindowTitle(QtGui.QApplication.translate("NetworkInfo", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("NetworkInfo", "Iface name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NetworkInfo", "Bytes sent:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBytesSentTotal.setText(QtGui.QApplication.translate("NetworkInfo", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBytesSentSpeed.setText(QtGui.QApplication.translate("NetworkInfo", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NetworkInfo", "Bytes received:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBytesReceivedTotal.setText(QtGui.QApplication.translate("NetworkInfo", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBytesReceivedSpeed.setText(QtGui.QApplication.translate("NetworkInfo", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NetworkInfo", "Packets sent:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPacketsSentTotal.setText(QtGui.QApplication.translate("NetworkInfo", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPacketsSentSpeed.setText(QtGui.QApplication.translate("NetworkInfo", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NetworkInfo", "Packets received", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPacketsReceivedTotal.setText(QtGui.QApplication.translate("NetworkInfo", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPacketsReceivedSpeed.setText(QtGui.QApplication.translate("NetworkInfo", "0", None, QtGui.QApplication.UnicodeUTF8))

