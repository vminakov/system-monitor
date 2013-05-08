#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       mainwindow.py
#       
#       Copyright 2012 Vladimir Minakov <vminakov@friendmts.co.uk>
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

#import os, base64, subprocess, json, time

from PySide import QtGui, QtCore
from ui.ui_mainwindow import Ui_MainWindow
from app.systemwindow import SystemWindow
from app.processmonitor import ProcessMonitor
from app.memorymonitor import MemoryMonitor
from app.cpumonitor import CpuMonitor
from app.networkmonitor import NetworkMonitor

class MainWindow(QtGui.QMainWindow):

	def __init__(self, parent = None):

		QtGui.QMainWindow.__init__(self, parent)
		
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# setup menu actions
		self.ui.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit)
		self.ui.actionAbout.triggered.connect(self.about)
		self.ui.actionAboutQt.triggered.connect(self.aboutQt)

		# initialize tabs
		self._systemWindowWidget = SystemWindow()
		self._processMonitorWidget = ProcessMonitor()
		self._memoryMonitorWidget = MemoryMonitor()
		self._cpuMonitorWidget = CpuMonitor()
		self._networkMonitorWidget = NetworkMonitor()

		self.ui.tabWidget.addTab(self._systemWindowWidget, "System")
		self.ui.tabWidget.addTab(self._processMonitorWidget, "Processes")
		self.ui.tabWidget.addTab(self._memoryMonitorWidget, "Memory")
		self.ui.tabWidget.addTab(self._cpuMonitorWidget, "CPU(s)")
		self.ui.tabWidget.addTab(self._networkMonitorWidget, "Network")

	def about(self):
		QtGui.QMessageBox.about(self, "About System Monitor", 
			"A sample Qt/PySide application, which uses self-updating models")

	def aboutQt(self):
		QtGui.QMessageBox.aboutQt(self)
