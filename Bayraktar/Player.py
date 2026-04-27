from PyQt6.QtWidgets import QGraphicsRectItem
from PyQt6.QtCore import Qt
from Bullet import Bullet


class Player(QGraphicsRectItem):
    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Space:
            bullet = Bullet()

            bullet.setPos(self.x() + self.rect().width() / 2 - bullet.rect().width() / 2, self.y())
            self.scene().addItem(bullet)


        elif event.key() == Qt.Key.Key_Left:
            self.setPos(self.x() - 10, self.y())

        elif event.key() == Qt.Key.Key_Right:
            self.setPos(self.x() + 10, self.y())

        elif event.key() == Qt.Key.Key_Up:
            self.setPos(self.x(), self.y() - 10)

        elif event.key() == Qt.Key.Key_Down:
            self.setPos(self.x(), self.y() + 10)