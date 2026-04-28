from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtCore import Qt, QUrl
from Bullet import Bullet
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class Player(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

        self.bullet_sound = QMediaPlayer()
        self.audio = QAudioOutput()
        self.bullet_sound.setAudioOutput(self.audio)

        #load the bullet sound
        bullet_sound_url = QUrl.fromLocalFile("bullet2.mp3")
        self.bullet_sound.setSource(bullet_sound_url)



    def keyPressEvent(self, event):
        scene_width = self.scene().sceneRect().width()

        if event.key() == Qt.Key.Key_Space:
            bullet = Bullet()

            bullet.setPos(self.x() + self.pixmap().width() / 2 - bullet.pixmap().width() / 2, self.y())
            self.scene().addItem(bullet)


            if self.bullet_sound.playbackRate() == QMediaPlayer.PlaybackState.PlayingState:
                self.bullet_sound.stop()

            self.bullet_sound.play()


        elif event.key() == Qt.Key.Key_Left:
            if self.x() > 0:
                self.setPos(self.x() - 10, self.y())

        elif event.key() == Qt.Key.Key_Right:
            if self.x() + self.pixmap().width() < scene_width:
                self.setPos(self.x() + 10, self.y())