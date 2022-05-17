''''
Pseudocode:
1. Create the UI for the tic tac toe game
'''

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from TicTacToeUI import TicTacToeUI
from TicTacToeCtrl import TicTacToeCtrl
from classes import GameBoard, Player, TicTacToe


if __name__ == "__main__":
    print("Hello World!")
    ticTacToe = QApplication(sys.argv)

    view = TicTacToeUI()
    player = Player(marker='X', isHuman=True)
    board = GameBoard()
    # board.printGameBoard()
    game = TicTacToe(board, player)
    controller = TicTacToeCtrl(game, view)
    view.show()
    sys.exit(ticTacToe.exec())
