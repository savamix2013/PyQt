from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QGraphicsRectItem
from random import randint
from Health import Health



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



        colliding_items = self.collidingItems()

        for item in colliding_items:
            from Player import Player
            if isinstance(item, Player):
                for scene_items in self.scene().items():
                    if isinstance(scene_items, Health):
                        scene_items.decrease()
                        print("Health decreased")

                        if not scene_items.isActive():
                            print("Game Over")
                            self.scene().views()[0].close()

                self.scene().removeItem(self)
                self.timer.stop()
                return