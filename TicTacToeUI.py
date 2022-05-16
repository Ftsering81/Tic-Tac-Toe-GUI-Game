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
from functools import partial
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox


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




class TicTacToeCtrl:
    def __init__(self, model, view):
        self.model = model
        self._view = view
        self._connectSignals()

    def markX(self, selectedbtnKey):
        button = self._view.buttons[selectedbtnKey]
        if button.text() == "":
            player = self.model.player
            pos = [int(selectedbtnKey[0]), int(selectedbtnKey[1])]
            self.model.gameBoard.markPosition(player.marker, pos)
            self.model.gameBoard.printGameBoard()
            button.setText("X")

            gameOver = model.checkIfWinner()
            if gameOver and player.:
                self.displayGameOverMsg("GAME OVER! YOU WON!")
            else:
                self.model.playerTurn = False # now computer's turn
            # check to see if the there are any horizontal, vertical or diagnol marks in a row for user

    def displayGameOverMsg(self, message):
        msg = QMessageBox()
        msg.setGeometry(300, 300, 100, 100)
        msg.setText(message)
        btnClicked = msg.exec_() # shows the message


    def resetGrid(self):
        msg = QMessageBox()
        msg.setGeometry(300, 300, 100, 100)
        msg.setText("STARTING A NEW GAME")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        btnClicked = msg.exec_()

        if btnClicked == QMessageBox.Ok: # only reset game if user says ok
            for btnKey, btn in self._view.buttons.items():
                btn.setText("")


    def _connectSignals(self):
        for btnKey, btn in self._view.buttons.items():
            btn.clicked.connect(partial(self.markX, btnKey))

        self._view.newGameButton.clicked.connect(self.resetGrid)



