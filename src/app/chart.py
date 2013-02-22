
from PySide import QtGui, QtCore

class Chart(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)

        self.points = [20, 30, 15, 3, 10]

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBackground(qp)
        self.drawChart(qp)
        qp.end()

    def drawBackground(self, qp):
        brush = QtGui.QBrush(QtCore.Qt.CrossPattern)
        qp.setBrush(brush)

        qp.drawRect(0, 0, self.height(), self.width())

    def drawChart(self, qp):
        height = self.height()
        print height

        qp.drawLine(50, height, 100, 100)

        # x = 0
        # x_step = self.width() / 5
        # y = height / 100 * self.points[0]
        # print y

        # for point_index in range(1, len(self.points)):
        #     prev_x = x
        #     prev_y = y

        #     x = x + x_step
        #     y = height / 100 * self.points[point_index]
        #     print y

        #     qp.drawLine(prev_x, prev_y, x, y)

