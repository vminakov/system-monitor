# -*- coding: utf-8 -*-
#
#       cpuchart.py
#       
#       Model class for monitoring CPU usage

import psutil

from PySide import QtCore
from wsw.model import QAbstractItemModel, QTimer

class CpuChart(QAbstractItemModel):
    """
    Model class for monitoring CPU usage

    Can be used as a data source for app.chart view.
    Stores CPU usage values for the last 10 seconds
    and updates CPU info every second
    """
    def __init__(self, cpuNum, parent=None):
        super(CpuChart, self).__init__(parent)

        self._cpuNum = cpuNum
        cpuUsage = psutil.cpu_percent(interval=None, percpu=True)[self._cpuNum]

        self._data = [cpuUsage] * 10

        # update CPU usage values every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._refresh)
        self.timer.start(1000)

        self._refresh()

    def _refresh(self):
        """
        Get CPU usage values and emit dataChanged signal

        Protected method
        """
        cpuUsage = psutil.cpu_percent(interval=None, percpu=True)[self._cpuNum]        

        if self._cpuNum == 1:
            print cpuUsage
        self._data.pop(0)
        self._data.append(cpuUsage)

        self.dataChanged.emit(0, 0)

    def data(self, index=None, role=QtCore.Qt.DisplayRole):
        """
        Return list of CPU usage values
        """
        return self._data