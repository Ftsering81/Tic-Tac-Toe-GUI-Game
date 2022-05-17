import PyQt5
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


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
        self.gridWidget = QWidget()
        self.buttons = {}
        for row in range(3):
            for col in range(3):
                button = QPushButton() # f"{row}{col}"
                # button.setFixedSize(150, 150)
                button.setMinimumSize(150, 150)
                button.setMaximumSize(400, 400)
                button.setFont(QFont("Times", 100, QFont.Bold))
                button.setStyleSheet("QPushButton {background-color: pink}")
                # button.setDisabled(True)

                self.buttons[f"{row}{col}"] = button
                gridLayout.addWidget(button, row, col)
                gridLayout.setSpacing(20)
        self.gridWidget.setLayout(gridLayout)

        self.mainLayout.addWidget(self.gridWidget)


    def createScoreBoard(self):
        self.rightLayout = QVBoxLayout()
        self.rightWidget = QWidget()

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
        print(self.rightLayout.contentsMargins())
        self.createnewGameButton()
        self.rightWidget.setLayout(self.rightLayout)
        self.mainLayout.addWidget(self.rightWidget)


    def createnewGameButton(self):
        self.newGameButton = QPushButton("NEW GAME")
        self.newGameButton.setFixedSize(100, 50)
        self.newGameButton.setStyleSheet("QPushButton {background-color: red}")
        self.rightLayout.addWidget(self.newGameButton, alignment=Qt.AlignCenter)



