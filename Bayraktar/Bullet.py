from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtCore import QTimer


class Bullet(QGraphicsRectItem):
    def __init__(self):
        super().__init__()

        self.setRect(0,0,10,50)

        self.timer = QTimer()

        self.timer.timeout.connect(self.move)

        self.timer.start(50)

    def move(self):
        self.setPos(self.x(), self.y() - 10)
        
        