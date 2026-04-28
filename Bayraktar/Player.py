from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtCore import Qt, QUrl
from Bullet import Bullet
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput


class Player(QGraphicsRectItem):
    def __init__(self):
        super().__init__()

        self.bullet_sound = QMediaPlayer()
        self.audio = QAudioOutput()
        self.bullet_sound.setAudioOutput(self.audio)

        #load the bullet sound
        bullet_sound_url = QUrl.fromLocalFile("bullet2.mp3")
        self.bullet_sound.setSource(bullet_sound_url)



    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Space:
            bullet = Bullet()

            bullet.setPos(self.x() + self.rect().width() / 2 - bullet.rect().width() / 2, self.y())
            self.scene().addItem(bullet)


            if self.bullet_sound.playbackRate() == QMediaPlayer.PlaybackState.PlayingState:
                self.bullet_sound.stop()

            self.bullet_sound.play()


        elif event.key() == Qt.Key.Key_Left:
            self.setPos(self.x() - 10, self.y())

        elif event.key() == Qt.Key.Key_Right:
            self.setPos(self.x() + 10, self.y())

        elif event.key() == Qt.Key.Key_Up:
            self.setPos(self.x(), self.y() - 10)

        elif event.key() == Qt.Key.Key_Down:
            self.setPos(self.x(), self.y() + 10)