
import psutil

from wsw.model import QAbstractItemModel, QTimer, Signal
from model.util import humanize_bytes

class MemoryInfo(QAbstractItemModel):
    
    def __init__(self, memType, parent=None):
        super(MemoryInfo, self).__init__(parent)
        self._type = 'virt' if memType == 'virt' else 'swap'

        self.totalChanged = Signal(str)
        self.availableChanged = Signal(str)
        self.percentChanged = Signal(str)
        self.usedChanged = Signal(str)
        self.freeChanged = Signal(str)


        self.timer = QTimer(self)
        self.timer.timeout.connect(self._refresh)
        self.timer.start(1000)

        self._refresh()

    def _refresh(self):
        print("Memory info refresh")
        if self._type == 'virt':
            memUsage = psutil.virtual_memory()
        else:
            memUsage = psutil.swap_memory()

        self.totalChanged.emit(humanize_bytes(memUsage.total, 2))
        if self._type == 'virt':
            self.availableChanged.emit(humanize_bytes(memUsage.available, 2))
        self.percentChanged.emit(str(memUsage.percent) + '%')
        self.usedChanged.emit(humanize_bytes(memUsage.used, 2))
        self.freeChanged.emit(humanize_bytes(memUsage.free, 2))