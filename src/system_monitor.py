#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       fct.py
#       
#       Copyright 2011 vminakov <vminakov@vminakov-desktop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
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
