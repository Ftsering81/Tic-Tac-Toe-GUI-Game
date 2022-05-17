import PyQt5
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QToolBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame


class TicTacToeUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TIC TAC TOE")
        self.setFixedSize(780, 600)
        self.setGeometry(100, 100, 280, 80)
        self.mainLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self._centralWidget)
        self.game_with_score_board = QHBoxLayout()

        self._createToolBar()
        self._createTitle()
        self._createGrid()
        self._createScoreBoard()

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction("Exit", self.close)

    def _createTitle(self):
        title = QLabel("TIC TAC TOE")
        title.setStyleSheet("QLabel {color : green; font-size: 80pt; font-weight: 80pt; font-family: Georgia}")
        self.mainLayout.addWidget(title, alignment=Qt.AlignLeft)

    def _createGrid(self):
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

        self.game_with_score_board.addWidget(self.gridWidget)


    def _createScoreBoard(self):
        self.rightLayout = QVBoxLayout()
        self.rightWidget = QWidget()
        # self.rightWidget.setStyleSheet("QWidget {background-color: brown;}")

        scoreBoardLabel = QLabel("SCOREBOARD")
        scoreBoardLabel.setStyleSheet("QLabel {font-size: 30pt; font-family: Georgia; color: DarkGoldenRod}")
        scoreBoardLabel.setFixedHeight(50)
        self.rightLayout.addWidget(scoreBoardLabel)
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
        self.scoreBoardWidget.setStyleSheet(" QLineEdit {font-size: 20pt; font-weight: bold; color: DarkGoldenRod; }")
        self.scoreBoardWidget.setFixedHeight(100)


        self.rightLayout.addWidget(self.scoreBoardWidget)
        self._createnewGameButton()
        self.rightWidget.setLayout(self.rightLayout)
        self.game_with_score_board.addWidget(self.rightWidget)



        self.mainLayout.addLayout(self.game_with_score_board)

    def _createnewGameButton(self):
        self.newGameButton = QPushButton("NEW GAME")
        self.newGameButton.setFixedSize(160, 80)
        self.newGameButton.setStyleSheet("QPushButton {background-color: green; color: pink;font-size: 25pt; font-family: Georgia;}")
        # self.rightWidget.addWidget(self.newGameButton, alignment=Qt.AlignCenter)
        self.rightLayout.addWidget(self.newGameButton, alignment=Qt.AlignCenter)



