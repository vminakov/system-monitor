
import psutil, random

from PySide import QtCore
from wsw.model import QAbstractItemModel

class MemoryChart(QAbstractItemModel):
    def __init__(self, parent=None):
        super(MemoryChart, self).__init__(parent)
        self._data = [0] * 10

        #timer = QtCore.QTimer(self)
        #timer.timeout.connect(self._refresh)
        #timer.start(1000)

        self._refresh()

    def _refresh(self):
        new_value = int(random.random() * 100)

        self._data.pop(0)
        self._data.append(new_value)

        self.dataChanged.emit(0, 0)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        return self._data