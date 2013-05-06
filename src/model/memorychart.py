
import psutil, random

from PySide import QtCore
from wsw.model import QAbstractItemModel, QTimer

class MemoryChart(QAbstractItemModel):
    def __init__(self, memType, parent=None):
        super(MemoryChart, self).__init__(parent)
        self._type = 'virt' if memType == 'virt' else 'swap'

        # fetch initial memory data
        if self._type == 'virt':
            memUsage = psutil.virtual_memory().percent
        else:
            memUsage = psutil.swap_memory().percent
        self._data = [memUsage] * 10

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._refresh)
        self.timer.start(1000)

        self._refresh()

    def _refresh(self):
        if self._type == 'virt':
            newMemUsage = psutil.virtual_memory().percent
        else:
            newMemUsage = psutil.swap_memory().percent

        self._data.pop(0)
        self._data.append(newMemUsage)

        self.dataChanged.emit(0, 0)
        print("Memory chart refresh called")

    def data(self, index, role=QtCore.Qt.DisplayRole):
        return self._data