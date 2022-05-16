import PyQt5
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFormLayout, QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

class TicTacToeUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TIC TAC TOE")
        # self.setFixedSize(490, 700)
        self.setGeometry(100, 100, 280, 80)
        self.mainLayout = QHBoxLayout()
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self._centralWidget)

        self.createGrid()
        self.createScoreBoard()

    def createGrid(self):
        gridLayout = QGridLayout()
        self.buttons = {}
        for row in range(3):
            for col in range(3):
                button = QPushButton(f"{row}{col}")
                # button.setFixedSize(150, 150)
                button.setMinimumSize(150, 150)
                button.setMaximumSize(400, 400)
                button.setStyleSheet("QPushButton {background-color: pink}")
                button.setDisabled(True)

                self.buttons[f"{row}{col}"] = button
                gridLayout.addWidget(button, row, col)
                gridLayout.setSpacing(20)
        self.mainLayout.addLayout(gridLayout)


    def createScoreBoard(self):
        self.rightLayout = QVBoxLayout()
        self.scoreBoardLayout = QFormLayout()
        self.playerScore = QLineEdit()
        self.enemyScore = QLineEdit()

        self.scoreBoardWidget = QWidget()
        self.playerScore.setDisabled(True)
        self.enemyScore.setDisabled(True)
        self.playerScore.setFixedSize(80, 30)
        self.playerScore.setPlaceholderText('0')
        self.enemyScore.setPlaceholderText('0')
        self.enemyScore.setFixedSize(80, 30)

        self.scoreBoardLayout.addRow('Player X:',  self.playerScore)
        self.scoreBoardLayout.addRow('Player O:',  self.enemyScore)
        self.scoreBoardWidget.setLayout(self.scoreBoardLayout)


        self.rightLayout.addWidget(self.scoreBoardWidget)
        self.createPlayButton()
        self.mainLayout.addLayout(self.rightLayout)


    def createPlayButton(self):
        self.playButton = QPushButton("NEW GAME")
        self.playButton.setFixedSize(100, 50)
        self.playButton.setStyleSheet("QPushButton {background-color: red}")
        self.rightLayout.addSpacing(10)
        self.rightLayout.addWidget(self.playButton, alignment=Qt.AlignCenter)








