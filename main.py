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


def main():
    ticTacToe = QApplication(sys.argv)
    view = TicTacToeUI()
    player = Player(marker='X', isHuman=True)
    board = GameBoard()
    game = TicTacToe(board, player)
    controller = TicTacToeCtrl(game, view)
    view.show()
    sys.exit(ticTacToe.exec())


if __name__ == "__main__":
    main()
