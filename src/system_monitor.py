#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       system_monitor.py
#       
#		The starting point for desktop monitor application.
#		Creates the application and runs it

__IN_QT__ = True

import sys

from PySide import QtGui, QtCore
from app.mainwindow import MainWindow

def main():
	QtCore.QCoreApplication.setApplicationName("system_monitor")
	QtCore.QCoreApplication.setOrganizationName("UH")
	QtCore.QCoreApplication.setOrganizationDomain("uh.ac.uk")
	
	app = QtGui.QApplication(sys.argv)
	sm_app = MainWindow()
	sm_app.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
