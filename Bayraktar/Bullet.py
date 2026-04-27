from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtCore import QTimer
from Enemy import Enemy


class Bullet(QGraphicsRectItem):
    def __init__(self):
        super().__init__()

        self.setRect(0,0,10,50)

        self.timer = QTimer()

        self.timer.timeout.connect(self.move)

        self.timer.start(50)

    def move(self):
        self.setPos(self.x(), self.y() - 10)
        
        colliding_items = self.collidingItems()

        for item in colliding_items:
            if isinstance(item, Enemy):
                self.scene().removeItem(item)
                self.scene().removeItem(self)


                print("Bullet hit an enemy")

                self.timer.stop()

                del item
                del self

                return

