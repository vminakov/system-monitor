
import psutil, random

from PySide import QtCore
from wsw.model import QAbstractItemModel
from model.util import humanize_bytes

class MemoryInfo(QAbstractItemModel):
    
    totalChanged = QtCore.Signal(str)
    availableChanged = QtCore.Signal(str)
    percentChanged = QtCore.Signal(str)
    usedChanged = QtCore.Signal(str)
    freeChanged = QtCore.Signal(str)

    def __init__(self, memType, parent=None):
        print("MEminfo init")
        super(MemoryInfo, self).__init__(parent)
        self._type = 'virt' if memType == 'virt' else 'swap'


        timer = QtCore.QTimer(self)
        timer.timeout.connect(self._refresh)
        timer.start(1000)

        self._refresh()

    def _refresh(self):
        print("Memory info refresh")
        if self._type == 'virt':
            memUsage = psutil.virtual_memory()
        else:
            memUsage = psutil.swap_memory()
        print memUsage

        self.totalChanged.emit(humanize_bytes(memUsage.total, 2))
        if self._type == 'virt':
            self.availableChanged.emit(humanize_bytes(memUsage.available, 2))
        self.percentChanged.emit(str(memUsage.percent) + '%')
        self.usedChanged.emit(humanize_bytes(memUsage.used, 2))
        self.freeChanged.emit(humanize_bytes(memUsage.free, 2))