
from PySide import QtGui, QtCore

class Chart(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)

        self.points = [20, 30, 15, 3, 10, 20, 4, 10, 90]

        self.model = None

    def setModel(self, model):
        self.model = model
        self.model.dataChanged.connect(self.fetchData)

    def getModel(self):
        return self.model

    def fetchData(self, topLeft, bottomRight):
        self.points = self.model.data(None)
        self.repaint()
        self.update()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBackground(qp)
        self.drawChart(qp)
        self.drawAxis(qp)
        qp.end()

    def drawBackground(self, qp):
        start_width = 40;
        start_height = 10;

        end_width = self.width();
        end_height = self.height() - 40;

        qp.fillRect(start_width, start_height, end_width, end_height, QtGui.QColor("white"))

    def drawAxis(self, qp):
        draw_area_height = self.height() - 40;
        draw_area_width = self.width() - 40;

        pen = QtGui.QPen()
        pen.setColor("black")
        pen.setStyle(QtCore.Qt.DashLine)
        qp.setPen(pen)

        # draw Y axis
        y_label_gap = draw_area_height / 5;
        y_offset = 10;
        for percent in range(100, 0, -20):
            # draw axis label
            qp.drawLine(35, y_offset, 40, y_offset)
            qp.drawText(0, y_offset + 5, str(percent) + "%")
            # draw axis horizontal bar
            qp.drawLine(40, y_offset, self.width(), y_offset)
            # increment vertical offeset for next label
            y_offset += y_label_gap

        # draw the "0%" label vertical label
        qp.drawLine(35, draw_area_height + 10, 40, draw_area_height + 10)
        qp.drawText(0, draw_area_height + 13, "0%")
        qp.drawLine(35, draw_area_height + 10, self.width(), draw_area_height + 10)


        pen.setStyle(QtCore.Qt.DotLine)
        qp.setPen(pen)

        # draw X axis
        x_label_gap = draw_area_width / len(self.points)
        x_offset = 40
        for second in range(len(self.points), 0, -1):
            # draw axis label
            qp.drawLine(x_offset, self.height() - 30, x_offset, self.height() - 25)
            qp.drawText(x_offset - 3, self.height() - 10, str(second))
            qp.drawLine(x_offset, 10, x_offset, self.height() - 30)
            x_offset += x_label_gap

        # draw the first horizontal label
        qp.drawLine(self.width() - 2, self.height() - 30, self.width() - 2, self.height() - 25)
        qp.drawText(self.width() - 7, self.height() - 10, "0")


    def drawChart(self, qp):
        draw_area_height = self.height() - 40

        x_gap = (self.width() - 40) / len(self.points)
        x = 0

        y_gap = draw_area_height / 100
        y = 0

        pen = QtGui.QPen()
        pen.setColor("darkGreen")
        pen.setWidth(2)
        qp.setPen(pen)

        for index, point_value in enumerate(self.points):
            #print index, point_value

            try:
                next_index = index + 1
                next_point_value = self.points[next_index]

                x = (index * x_gap) + 40
                y = draw_area_height - point_value * y_gap

                next_x = next_index * x_gap + 40
                next_y = draw_area_height - next_point_value * y_gap
                qp.drawLine(x, y, next_x, next_y)
            except IndexError:
                pass
