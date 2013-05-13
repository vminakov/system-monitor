
import psutil

from PySide import QtGui, QtCore
from app.cpumonitorwidget import CpuMonitorWidget
from model.cpuchart import CpuChart

class CpuMonitor(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        gridLayout = QtGui.QGridLayout()

        numOfCpus = len(psutil.cpu_percent(interval=None, percpu=True))
        for i in range(numOfCpus):
            cpuChartModel = CpuChart(i)
            cpuChartWidget = CpuMonitorWidget(i, cpuChartModel)
            
            row = i / 2
            col = 0 if i % 2 == 0 else 1
            gridLayout.addWidget(cpuChartWidget, row, col)

        self.setLayout(gridLayout)
        self.show()
