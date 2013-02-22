from PySide import QtGui, QtCore
from app.chart import Chart
from ui.ui_memorymonitor import Ui_MemoryMonitor

class MemoryMonitor(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MemoryMonitor()
        self.ui.setupUi(self)

        chart_widget = Chart(self)
        hbox_layout = QtGui.QHBoxLayout()
        hbox_layout.addWidget(chart_widget)
        self.setLayout(hbox_layout)

    # def paintEvent(self, e):

    #     qp = QtGui.QPainter()
    #     qp.begin(self)
    #     self.drawBrushes(qp)
    #     qp.end()
        
    # def drawBrushes(self, qp):
      
    #     brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(10, 15, 90, 60)

    #     brush.setStyle(QtCore.Qt.Dense1Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(130, 15, 90, 60)

    #     brush.setStyle(QtCore.Qt.Dense2Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(250, 15, 90, 60)

    #     brush.setStyle(QtCore.Qt.Dense3Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(10, 105, 90, 60)

    #     brush.setStyle(QtCore.Qt.DiagCrossPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(10, 105, 90, 60)

    #     brush.setStyle(QtCore.Qt.Dense5Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(130, 105, 90, 60)

    #     brush.setStyle(QtCore.Qt.Dense6Pattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(250, 105, 90, 60)

    #     brush.setStyle(QtCore.Qt.HorPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(10, 195, 90, 60)

    #     brush.setStyle(QtCore.Qt.VerPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(130, 195, 90, 60)

    #     brush.setStyle(QtCore.Qt.BDiagPattern)
    #     qp.setBrush(brush)
    #     qp.drawRect(250, 195, 90, 60)
    #     