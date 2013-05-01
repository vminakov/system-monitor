
import psutil

from PySide import QtCore
from model.util import humanize_bytes

class Process(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super(Process, self).__init__(parent)

        self._refresh()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self._refresh)
        timer.start(3000)

    def _refresh(self):
        print("Refresh called")
        self._data = []
        

        for p in psutil.process_iter():
            mem = p.get_memory_info()

            self._data.append([
                p.pid,
                p.name,
                p.username,
                str(p.status),
                humanize_bytes(mem.vms),
                humanize_bytes(mem.rss),
                str(round(p.get_memory_percent(), 2)) + "%",
                str(p.get_cpu_percent(interval=None)) + "%"
            ])

        self._data = sorted(self._data, key=lambda p: float(p[-1][:-1]), reverse=True)
        self.reset()

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self._data[0])

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return None

        row = index.row()
        column = index.column()

        return self._data[row][column]

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return None

        if section == 0:
            return 'Id'
        elif section == 1:
            return 'Name'
        elif section == 2:
            return 'Owner'
        elif section == 3:
            return 'Status'
        elif section == 4:
            return 'Memory (virtual)'
        elif section == 5:
            return 'Memory (resident)'
        elif section == 6:
            return 'Memory usage'
        elif section == 7:
            return 'CPU usage'
