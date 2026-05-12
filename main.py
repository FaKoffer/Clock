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
                            self.width() - base_width, self.height() - base_width)

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


        radius_lines = min(self.width(), self.height()) // 2 - base_width 
        for hour_lines in range(1,13):
            angle = math.radians(hour_lines * 30 - 90)

            x0 = center_x + radius_lines * math.cos(angle)
            y0 = center_y + radius_lines * math.sin(angle)

            x1 = center_x + (radius_lines - 10) * math.cos(angle)
            y1 = center_y + (radius_lines - 10) * math.sin(angle)

            painter.drawLine(int(x0), int(y0), int(x1), int(y1)) 

        # Smaller minute lines
        temp_smallPen = QPen()
        temp_smallPen.setColor(QColor("black"))
        temp_smallPen.setWidthF(base_width / 4)

        painter.setPen(temp_smallPen)
        
        for lines_rest in range(1,61):
            angle = math.radians(lines_rest * 6 - 90)

            x0 = center_x + radius_lines * math.cos(angle)
            y0 = center_y + radius_lines * math.sin(angle)

            x1 = center_x + (radius_lines - 6) * math.cos(angle)
            y1 = center_y + (radius_lines - 6) * math.sin(angle)

            painter.drawLine(int(x0), int(y0), int(x1), int(y1)) 



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