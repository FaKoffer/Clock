import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QFont
from PyQt5.QtCore import QDateTime
import math

window_dimensions = [800, 800]
base_width = 24

class Clock(QWidget):
    def __init__(self):
        super().__init__()

        self.clockPen = QPen()
        self.clockPen.setColor(QColor("black"))
        self.clockPen.setWidthF(base_width)
        self.numbersFont = QFont()
        self.numbersFont.setPointSize(base_width)

        self.hourPen = QPen()
        self.hourPen.setColor(QColor("black"))
        self.hourPen.setWidthF(base_width)

        self.minutePen = QPen()
        self.minutePen.setColor(QColor("black"))
        self.minutePen.setWidthF(base_width // 2)

        self.secondPen = QPen()
        self.secondPen.setColor(QColor("red"))
        self.secondPen.setWidthF(base_width // 4)

        self.initUI()
        
    #clears screen when called
    def paintEvent(self, event):

        date = QDateTime.currentDateTime()
        painter = QPainter(self)

        painter.setFont(self.numbersFont)
        painter.setPen(self.clockPen)
        self.draw_clock_face(painter)
        
        painter.setPen(self.hourPen)
        self.draw_clock_hand(painter, date.time().hour())

        painter.setPen(self.minutePen)
        self.draw_clock_hand(painter, date.time().minute())

        painter.setPen(self.secondPen)
        self.draw_clock_hand(painter, date.time().second())
        

    def draw_clock_face(self, painter):
        painter.drawEllipse(base_width // 2, base_width //2,
                            *[dim - base_width for dim in window_dimensions])

        center_x = self.width() // 2
        center_y = self.height() // 2

        radius = min(self.width(), self.height()) // 2 - base_width * 3

        for hour in range(1, 13):
            angle = math.radians(hour * 30 - 90)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            
            text = str(hour)
            metrics = painter.fontMetrics()

            painter.drawText(int(x - metrics.horizontalAdvance(text) / 2), int(y + metrics.ascent() / 2), str(hour))

    def draw_clock_hand(self, painter, time):
        pass     

    def initUI(self):
        self.resize(*window_dimensions)

def main():
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())        

if __name__ == "__main__":
    main()        