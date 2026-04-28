import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsTextItem
from Player import Player
from PyQt6.QtCore import QTimer, QUrl, Qt
from Enemy import Enemy
from Score import Score
from Health import Health
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtGui import QPixmap, QFont


class Window(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setup_music()

        self.scene = QGraphicsScene()

        self.setStyleSheet('background-color:#8b624c')

        self.player = Player()
        self.player.setPixmap(QPixmap("player.png"))

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

        self.player.setPos(self.scene.width() / 2 - self.player.pixmap().width() / 2,
                           self.scene.height() - self.player.pixmap().height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.spawn)
        self.timer.start(2000)




    def spawn(self):
        enemy = Enemy()
        self.scene.addItem(enemy)

    def game_over(self):
        self.timer.stop()

        for item in self.scene.items():
            if isinstance(item, Enemy):
                item.timer.stop()

        self.player.setEnabled(False)
        self.player.clearFocus()

        game_over_text = QGraphicsTextItem("Гра закінчена")
        game_over_text.setDefaultTextColor(Qt.GlobalColor.white)
        game_over_text.setFont(QFont("Sanserif", 32))
        game_over_text.setPos(
            self.scene.width() / 2 - game_over_text.boundingRect().width() / 2,
            self.scene.height() / 2 - game_over_text.boundingRect().height() / 2
        )
        self.scene.addItem(game_over_text)

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