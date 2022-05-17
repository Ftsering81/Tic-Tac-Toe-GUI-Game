from PyQt5.QtWidgets import QMessageBox
from functools import partial
import time


class TicTacToeCtrl:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connectSignals()

    # Function for human player to mark 'O' on the board
    def markX(self, selectedbtnKey):
        button = self._view.buttons[selectedbtnKey]
        pos = [int(selectedbtnKey[0]), int(selectedbtnKey[1])]
        print("markX() tapped")
        player = self._model.player
        marked = self._model.playerMark(player, pos)
        if marked:  # only show X on button if pos marked successfully
            button.setText("X")
        else:
            print("square already marked so do nothing and return. Nothing will happen until player clicks on the buttons again.")
            return
        gameOver = self.checkIfGameOver()
        if not gameOver:  # game not over yet, so now computer's turn
            for btnKey, btn in self._view.buttons.items():
                btn.setEnabled(False)  # Disable buttons for the player when it's computer turn
            self.markO()

    # Function for computer player to mark 'O' on the board
    def markO(self):
        # Make computer wait a lil before marking the board
        time.sleep(0.3)
        # Computer will randomly choose a non-marked box to mark
        gameBoard = self._model.gameBoard
        computer_player = self._model.computer
        self._model.computerMark()
        pos_marked = computer_player.getPosPlayerMarked()
        button = self._view.buttons[f"{pos_marked[0]}{pos_marked[1]}"]
        button.setText('O')
        gameBoard.printGameBoard()

        gameOver = self.checkIfGameOver()
        if not gameOver: # game not over yet, so now player's turn
            for btnKey, btn in self._view.buttons.items():
                btn.setEnabled(True)  # Re-enable buttons for the player's turn

    def checkIfGameOver(self):
        gameOver = self._model.checkIfGameOver()
        print("GameOver: ", gameOver)
        winner = self._model.checkWhoWon()
        print("Winner: ", winner)
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
        elif gameOver:  # draw // this evaluates to false for some reason
            self.displayGameOverMsg("THERE WAS A DRAW!")
            print("DRAW")
            self.resetBoard()
            return True
        else:
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
        for btnKey, btn in self._view.buttons.items():
            btn.setText("")
            btn.setEnabled(True)  # Enable buttons for new game since user goes first

    def startNewGame(self):
        msg = QMessageBox()
        msg.setGeometry(300, 300, 100, 100)
        msg.setText("STARTING A NEW GAME")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        btnClicked = msg.exec_()

        if btnClicked == QMessageBox.Ok:  # only reset game if user says ok
            self._model.resetGame()
            self.resetBoard() # updates the UI
            self.updateScoreBoard()

    def _connectSignals(self):
        for btnKey, btn in self._view.buttons.items():
            btn.clicked.connect(partial(self.markX, btnKey))

        self._view.newGameButton.clicked.connect(self.startNewGame)



