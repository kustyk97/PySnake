import random
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QWidget
from PyQt5.QtCore import QBasicTimer, Qt, QPoint, QTime
from PyQt5.QtGui import QPainter

from PySnake.Config import *


class QSnake(QWidget):
    def __init__(self, score_label, time_label, time_delay=100):
        super().__init__()
        self.initUI()
        self.score_label = score_label
        self.time_label = time_label
        self.timer = QBasicTimer()
        self.snake = list(
            reversed([QPoint(MAP_STEP * i, 0) for i in range(SNAKE_LENGTH)])
        )
        self.direction = QPoint(MAP_STEP, 0)
        self.food = QPoint(0, 0)
        self.isGameOver = False
        self.score = 0

        self.h_count_cells = QSNAKE_WIDTH // MAP_STEP
        self.v_count_cells = QSNAKE_HEIGHT // MAP_STEP
        self.placeFood()
        self.start_time = QTime.currentTime()
        self.timer.start(time_delay, self)

    def initUI(self):
        self.setWindowTitle("Snake Game")
        self.setGeometry(0, 0, QSNAKE_WIDTH, QSNAKE_HEIGHT)
        self.setFocusPolicy(Qt.StrongFocus)
        self.show()

    def placeFood(self):
        x = random.randint(0, self.h_count_cells - 1) * MAP_STEP
        y = random.randint(0, self.v_count_cells - 1) * MAP_STEP
        self.food = QPoint(x, y)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawSnake(painter)
        self.drawFood(painter)

    def drawSnake(self, painter):
        for segment in self.snake:
            painter.fillRect(segment.x(), segment.y(), MAP_STEP, MAP_STEP, SNAKE_COLOR)

    def drawFood(self, painter):
        painter.fillRect(self.food.x(), self.food.y(), MAP_STEP, MAP_STEP, FOOD_COLOR)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:
            QApplication.instance().quit()
        elif event.key() == Qt.Key_Up and self.direction != QPoint(0, MAP_STEP):
            self.direction = QPoint(0, -MAP_STEP)
        elif event.key() == Qt.Key_Down and self.direction != QPoint(0, -MAP_STEP):
            self.direction = QPoint(0, MAP_STEP)
        elif event.key() == Qt.Key_Left and self.direction != QPoint(MAP_STEP, 0):
            self.direction = QPoint(-MAP_STEP, 0)
        elif event.key() == Qt.Key_Right and self.direction != QPoint(-MAP_STEP, 0):
            self.direction = QPoint(MAP_STEP, 0)

    def update_time(self) -> None:
        elapsed_time = self.start_time.secsTo(QTime.currentTime())
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        self.time_label.setText(f"Time: {minutes}:{seconds:02d}")

    def update_score(self) -> None:
        self.score_label.setText(f"Score: {self.score}")

    def timerEvent(self, event):
        if self.isGameOver:
            return
        self.moveSnake()
        self.checkCollision()
        self.update_time()
        self.update()

    def moveSnake(self):
        head = self.snake[0] + self.direction
        self.snake.insert(0, head)
        if head == self.food:
            self.score += 1
            self.update_score()
            self.placeFood()
        else:
            self.snake.pop()

    def checkCollision(self):
        head = self.snake[0]
        if (
            head.x() < 0
            or head.x() >= QSNAKE_WIDTH
            or head.y() < 0
            or head.y() >= QSNAKE_HEIGHT
            or head in self.snake[1:]
        ):
            self.isGameOver = True

            QMessageBox.information(self, "Game Over", f"Your score: {self.score}")
            QApplication.instance().quit()
