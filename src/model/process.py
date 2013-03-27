
import psutil

from PySide import QtCore

class Process(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super(Process, self).__init__(parent)

        #self._data = [
        #    [1, 'Test Data', 'Stuff'],
        #    [2, 'Test Data 2', 'Stuff'],
        #    [3, 'Test Data 3', 'Stuff']
        #]
        self._refresh()

        #timer = QtCore.QTimer(self)
        #timer.timeout.connect(self._refresh)
        #timer.start(3000)

    def _refresh(self):
        print("Refresh called")
        self._data = []
        

        #processes = psutil.get_pid_list()
        #for pid in processes:
        #    p = psutil.Process(pid)
        #    self._data.append([
        #        pid,
        #        p.name,
        #        p.username,
        #        str(p.get_cpu_percent(interval=None))
        #    ])
        for p in psutil.process_iter():
            self._data.append([
                p.pid,
                p.name,
                p.username,
                str(p.get_cpu_percent(interval=None))
            ])

        self._data = sorted(self._data, key=lambda p: p[3], reverse=True)
        self.reset()

        #print self._data

        #top_left = self.index(0, 0)
        #bottom_right = self.index(self.rowCount() - 1, self.columnCount() - 1)
        #'self.dataChanged.emit(top_left, bottom_right)

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
            return 'Column 2'
        elif section == 2:
            return 'Column 3'
        elif section == 3:
            return 'CPU usage'
