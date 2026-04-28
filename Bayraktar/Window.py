import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem
from Player import Player
from PyQt6.QtCore import QTimer, QUrl
from Enemy import Enemy
from Score import Score
from Health import Health
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class Window(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setup_music()

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

    def setup_music(self):
        self.media_player = QMediaPlayer()

        self.audio = QAudioOutput()
        self.audio.setVolume(0.5)
        self.media_player.setAudioOutput(self.audio)

        music_file = QUrl.fromLocalFile("bg3.mp3")
        self.media_player.setSource(music_file)

        self.media_player.play()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())