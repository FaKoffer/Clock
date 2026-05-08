import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Clock(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = Clock()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()