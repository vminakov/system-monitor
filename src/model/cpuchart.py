
import psutil, random

from PySide import QtCore
from wsw.model import QAbstractItemModel

class CpuChart(QAbstractItemModel):
    def __init__(self, cpuNum, parent=None):
        super(CpuChart, self).__init__(parent)

        self._cpuNum = cpuNum
        cpuUsage = psutil.cpu_percent(interval=None, percpu=True)[self._cpuNum]


        self._data = [cpuUsage] * 10

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self._refresh)
        timer.start(1000)

        self._refresh()

    def _refresh(self):
        cpuUsage = psutil.cpu_percent(interval=None, percpu=True)[self._cpuNum]        

        self._data.pop(0)
        self._data.append(cpuUsage)

        self.dataChanged.emit(0, 0)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        return self._data