from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QGraphicsPixmapItem
from random import randint
from Health import Health
from PyQt6.QtGui import QPixmap



class Enemy(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

        random_number = randint(10, 1000) % 700
        self.setPos(random_number, 0)

        self.setPixmap(QPixmap("enemy.png"))

        self.timer = QTimer()
        self.timer.timeout.connect(self.move)
        self.timer.start(50)


    def move(self):
        self.setPos(self.x(), self.y() + 5)

        if self.pos().y() + self.pixmap().height() < 0:
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

                        if scene_items.is_dead():
                            print("Game Over")
                            view = self.scene().views()[0]
                            if hasattr(view, "game_over"):
                                view.game_over()

                self.scene().removeItem(self)
                self.timer.stop()
                return