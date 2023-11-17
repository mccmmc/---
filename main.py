import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.coords = None
        self.do_paint = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Рисование')

        self.do_paint = False
        self.coords = (150, 150)
        self.CircleButton.clicked.connect(self.can_draw)

    def can_draw(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_figures(qp)
        self.do_paint = False

    def draw_figures(self, qp):
        size = randint(20, 100)
        x = int(self.coords[0] - size / 2)
        y = int(self.coords[1] - size / 2)
        qp.setBrush(Qt.yellow)
        qp.drawEllipse(x, y, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
