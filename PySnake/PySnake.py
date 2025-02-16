from PySnake.QSnake import QSnake
from PySnake.Config import * 

from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QWidget

class PySnake(QMainWindow):
    def __init__(self, time_delay = 100):
        super().__init__()
        self.setWindowTitle("Snake Game")
        self.setGeometry(100, 100, QSNAKE_WIDTH, QSNAKE_HEIGHT + LABEL_HEIGHT)

        self.score_label = QLabel("Score: 0")
        self.score_label.setFixedHeight(LABEL_HEIGHT)
        self.time_label = QLabel("Time: 0")
        self.time_label.setFixedHeight(LABEL_HEIGHT)
        
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(0)
        top_layout.addWidget(self.score_label)
        top_layout.addWidget(self.time_label)

        game_frame = QFrame(self)
        game_frame.setStyleSheet("border: 1px solid gray; background-color: white;")
        game_frame.setGeometry(0, LABEL_HEIGHT, QSNAKE_WIDTH, QSNAKE_HEIGHT)
        game_widget = QSnake(self.score_label, self.time_label, time_delay)
        game_widget.setParent(game_frame)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(top_layout)
        main_layout.addWidget(game_frame)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)