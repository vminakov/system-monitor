from PySide import QtGui
from ui.ui_cpuchart import Ui_CpuChart

class CpuMonitorWidget(QtGui.QWidget):

    def __init__(self, index, chart, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_CpuChart()
        self.ui.setupUi(self)

        self.ui.cpuChart.setModel(chart)
        self.ui.groupBox.setTitle("CPU %s:" % index)
        