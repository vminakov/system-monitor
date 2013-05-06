
from PySide import QtGui
from model.systeminfo import SystemInfo
from ui.ui_systemwindow import Ui_SystemWindow

class SystemWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_SystemWindow()
        self.ui.setupUi(self)

        self._model = SystemInfo()
        self._initInfoUi()

    def _initInfoUi(self):
        # fetch Distro information
        distroLabel = QtGui.QLabel()
        distroLabel.setText(self._model.getDistro())

        kernelLabel = QtGui.QLabel()
        kernelLabel.setText("Kernel: " + self._model.getKernel())
        
        sysInfoVbox = QtGui.QVBoxLayout()
        sysInfoVbox.addWidget(distroLabel)
        sysInfoVbox.addWidget(kernelLabel)
        sysInfoVbox.addStretch(1)

        sysInfoGroupBox = QtGui.QGroupBox("System information:")
        sysInfoGroupBox.setLayout(sysInfoVbox)


        # hardware info
        memoryLabel = QtGui.QLabel("Memory:")
        memoryLabelValue = QtGui.QLabel(self._model.getTotalMemory())

        hardwareLayout = QtGui.QGridLayout()
        hardwareLayout.addWidget(memoryLabel, 0, 0)
        hardwareLayout.addWidget(memoryLabelValue, 0, 1)

        cpus = self._model.getCpu()
        for i, cpu in enumerate(cpus):
            procName = 'Processor #%s:' % (i)

            hardwareLayout.addWidget(QtGui.QLabel(procName), i + 1, 0)
            hardwareLayout.addWidget(QtGui.QLabel(cpu), i + 1, 1)

        hardwareGroupBox = QtGui.QGroupBox("Hardware information:")
        hardwareGroupBox.setLayout(hardwareLayout)


        # lay out groupboxes vertically
        groupBoxLayout = QtGui.QVBoxLayout()
        groupBoxLayout.addWidget(sysInfoGroupBox)
        groupBoxLayout.addWidget(hardwareGroupBox)
        groupBoxLayout.addStretch(1)

        self.ui.infoWidget.setLayout(groupBoxLayout)
