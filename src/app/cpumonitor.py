
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


        # self.ui = Ui_MemoryMonitor()
        # self.ui.setupUi(self)
        
        # self.ui.virtChart.setModel(MemoryChart("virt"))
        # self.ui.swapChart.setModel(MemoryChart("swap"))

        # self.memInfoVirt = MemoryInfo("virt")
        # self.memInfoVirt.totalChanged.connect(self.ui.labelVirtTotal.setText)
        # self.memInfoVirt.availableChanged.connect(self.ui.labelVirtAvailable.setText)
        # self.memInfoVirt.percentChanged.connect(self.ui.labelVirtPercent.setText)
        # self.memInfoVirt.usedChanged.connect(self.ui.labelVirtUsed.setText)
        # self.memInfoVirt.freeChanged.connect(self.ui.labelVirtFree.setText)

        # self.memInfoSwap = MemoryInfo("swap")
        # self.memInfoSwap.totalChanged.connect(self.ui.labelSwapTotal.setText)
        # self.memInfoSwap.percentChanged.connect(self.ui.labelSwapPercent.setText)
        # self.memInfoSwap.usedChanged.connect(self.ui.labelSwapUsed.setText)
        # self.memInfoSwap.freeChanged.connect(self.ui.labelSwapFree.setText)
