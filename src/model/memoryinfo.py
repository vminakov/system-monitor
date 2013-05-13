
import psutil

from wsw.model import QAbstractItemModel, QTimer, Signal
from model.util import humanize_bytes

class MemoryInfo(QAbstractItemModel):
    
    totalChanged = Signal(str)
    availableChanged = Signal(str)
    percentChanged = Signal(str)
    usedChanged = Signal(str)
    freeChanged = Signal(str)

    def __init__(self, memType, parent=None):
        super(MemoryInfo, self).__init__(parent)
        self._type = 'virt' if memType == 'virt' else 'swap'

        self._total = None
        self._available = None
        self._percent = None
        self._used = None
        self._free = None

        self._firstRun = True

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._refresh)
        self.timer.start(1000)

    def _refresh(self):
        if self._type == 'virt':
            memUsage = psutil.virtual_memory()
        else:
            memUsage = psutil.swap_memory()

        if self._total != humanize_bytes(memUsage.total, 2):
            self._total = humanize_bytes(memUsage.total, 2)
            self.totalChanged.emit(self._total)

        if self._type == 'virt':
            if self._available != humanize_bytes(memUsage.available, 2):
                self._available = humanize_bytes(memUsage.available, 2)
                self.availableChanged.emit(self._available)

        if self._percent != str(memUsage.percent) + '%':
            self._percent = str(memUsage.percent) + '%'
            self.percentChanged.emit(self._percent)

        if self._used != humanize_bytes(memUsage.used, 2):
            self._used = humanize_bytes(memUsage.used, 2)
            self.usedChanged.emit(self._used)

        if self._free != humanize_bytes(memUsage.free, 2):
            self._free = humanize_bytes(memUsage.free, 2)
            self.freeChanged.emit(self._free)

    def getCounters(self, *args):
        return {
            'total': self._total,
            'available': self._available,
            'percent': self._percent,
            'used': self._used,
            'free': self._free}