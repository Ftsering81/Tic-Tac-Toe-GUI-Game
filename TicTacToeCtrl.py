from PyQt5.QtWidgets import QMessageBox
from functools import partial
import time


class TicTacToeCtrl:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        # initialized with the 3x3 buttons bc those are the ones shown when app opens
        self._buttons = self._view.buttons3x3
        self._connectSignals()

    # Function that marks 'X' on the board for human player
    def markX(self, selectedbtnKey):
        button = self._buttons[selectedbtnKey]
        pos = [int(selectedbtnKey[0]), int(selectedbtnKey[1])]
        player = self._model.player
        marked = self._model.playerMark(player, pos)
        if marked:  # only show X on button if pos marked successfully
            button.setText("X")
            button.setStyleSheet("QPushButton {background-color: pink; color: RoyalBlue}")
        else:
            return
        gameOver = self.checkIfGameOver()
        if not gameOver:  # game not over yet, so now computer's turn
            for btnKey, btn in self._buttons.items():
                btn.setEnabled(False)  # Disable buttons for the player when it's computer turn
            self.markO()

    # Function for computer player to mark 'O' on the board
    def markO(self):
        time.sleep(0.1)
        computer_player = self._model.computer
        self._model.computerMark()  # Computer will randomly choose a non-marked box to mark
        pos_marked = computer_player.getPosPlayerMarked()
        button = self._buttons[f"{pos_marked[0]}{pos_marked[1]}"]
        button.setText('O')
        button.setStyleSheet("QPushButton {background-color: pink; color: OrangeRed}") # make marker red for

        gameOver = self.checkIfGameOver()
        if not gameOver:  # game not over yet, so now player's turn
            for btnKey, btn in self._buttons.items():
                btn.setEnabled(True)  # Re-enable buttons for the player's turn

    def checkIfGameOver(self):
        gameOver = self._model.checkIfGameOver()
        winner = self._model.checkWhoWon()
        if gameOver and winner == 'O':
            self.displayGameOverMsg("YOU LOST!")
            self.updateScoreBoard()
            self.resetBoard()
            return True
        elif gameOver and winner == 'X':
            self.displayGameOverMsg("YOU WON!")
            self.updateScoreBoard()
            self.resetBoard()
            return True
        elif gameOver:  # draw
            self.displayGameOverMsg("THERE WAS A DRAW!")
            self.resetBoard()
            return True
        else:  # game not over
            return False

    def updateScoreBoard(self):
        scoreBoard = self._model.scoreBoard
        self._view.playerScore.setText(f"{scoreBoard['X']}")
        self._view.enemyScore.setText(f"{scoreBoard['O']}")

    def displayGameOverMsg(self, message):
        msg = QMessageBox()
        msg.setGeometry(300, 300, 100, 100)
        msg.setText(message)
        btnClicked = msg.exec_()  # shows the message

    def resetBoard(self):
        self._model.gameBoard.clearBoard()
        for btnKey, btn in self._buttons.items():
            btn.setText("")
            btn.setEnabled(True)  # Enable buttons for new game in case computer won and buttons are disabled

    def startNewGame(self):
        msg = QMessageBox()
        msg.setGeometry(300, 300, 100, 100)
        msg.setText("STARTING A NEW GAME")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        btnClicked = msg.exec_()

        if btnClicked == QMessageBox.Ok:  # only reset game if user clicks OK
            self._model.resetGame()
            self.resetBoard() # updates the UI
            self.updateScoreBoard()

    def changeBoardDimension(self):
        self.resetBoard()  # clear the board and the model grid before switching to the other grid
        dimensionSelected = self._view.boardSizeComboBox.currentText()
        num_rows = int(dimensionSelected[0])
        num_cols = int(dimensionSelected[2])
        # Update the gameBoard grid of _model
        self._model.gameBoard.changeBoardSize(num_rows, num_cols)

        # Now need to update the grid on the UI to reflect change in the model
        if dimensionSelected == "4x4":
            self._view.stackedWidget.setCurrentIndex(1) # switches to the 4x4 grid at index 1 in the stack widget
            self._buttons = self._view.buttons4x4 # since the grid is the 4x4 grid, use the buttons part of that grid
        else:
            self._view.stackedWidget.setCurrentIndex(0) # swithes to the 3x3 grid at index 0 in the stack widget
            self._buttons = self._view.buttons3x3 # since the grid is now the 3x3 grid, use the buttons part of that grid


    def _connectSignals(self):
        # Connects the 3x3 grid buttons
        for btnKey, btn in self._view.buttons3x3.items():
            btn.clicked.connect(partial(self.markX, btnKey))

        # Connects the 4x4 grid buttons
        for btnKey, btn in self._view.buttons4x4.items():
            btn.clicked.connect(partial(self.markX, btnKey))

        # Connects the New Game button
        self._view.newGameButton.clicked.connect(self.startNewGame)

        # Connects the board dimension combo box
        self._view.boardSizeComboBox.currentIndexChanged.connect(self.changeBoardDimension)


