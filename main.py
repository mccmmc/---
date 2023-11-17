import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint

from UI import Ui_MainWindow


class Suprematism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setBrush(QColor(*self.set_colors()))
        qp.drawEllipse(x, y, size, size)

    @classmethod
    def set_colors(cls):
        colors = tuple((randint(0, 255), randint(0, 255), randint(0, 255)))
        return colors


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
