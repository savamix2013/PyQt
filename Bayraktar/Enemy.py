from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QGraphicsRectItem
from random import randint



class Enemy(QGraphicsRectItem):
    def __init__(self):
        super().__init__()

        random_number = randint(10, 1000) % 700
        self.setPos(random_number, 0)

        self.setRect(0,0, 100,100)

        self.timer = QTimer()
        self.timer.timeout.connect(self.move)
        self.timer.start(50)


    def move(self):
        self.setPos(self.x(), self.y() + 5)

        if self.pos().y() + self.rect().height() < 0:
            self.scene().removeItem(self)
            print("Deleted")