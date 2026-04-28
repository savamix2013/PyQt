import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem
from Player import Player
from PyQt6.QtCore import QTimer
from Enemy import Enemy
from Score import Score
from Health import Health


class Window(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()

        #rect = QGraphicsRectItem()
        self.player = Player()
        self.player.setRect(0, 0, 100, 100)

        self.scene.addItem(self.player)

        self.setScene(self.scene)

        self.player.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.player.setFocus()

        self.setFixedSize(800, 600)

        self.scene.setSceneRect(0, 0, 800, 600) 

        #self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        #self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.setWindowTitle("Bayraktar")

        # adding score
        self.score = Score()
        self.scene.addItem(self.score)

        # adding health
        self.health = Health()
        self.scene.addItem(self.health)
        self.health.setPos(self.health.x(), self.health.y() + 28)

        self.player.setPos(self.scene.width() / 2 - self.player.rect().width() / 2,
                           self.scene.height() - self.player.rect().height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.spawn)
        self.timer.start(2000)

    def spawn(self):
        enemy = Enemy()
        self.scene.addItem(enemy)




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())