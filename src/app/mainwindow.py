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

from PySide import QtGui
from ui.ui_mainwindow import Ui_MainWindow
from app.processmonitor import ProcessMonitor
from app.memorymonitor import MemoryMonitor

class MainWindow(QtGui.QMainWindow):

	def __init__(self, parent = None):

		QtGui.QMainWindow.__init__(self, parent)
		
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# initialize tabs
		self._processMonitorWidget = ProcessMonitor()
		self._memoryMonitorWidget = MemoryMonitor()

		self.ui.tabWidget.addTab(self._processMonitorWidget, "Processes")
		self.ui.tabWidget.addTab(self._memoryMonitorWidget, "Memory")