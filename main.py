''''
Pseudocode:
1. Create the UI for the tic tac toe game
'''

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from TicTacToeUI import TicTacToeUI
from TicTacToeUI import TicTacToeCtrl

if __name__ == "__main__":
    print("Hello World!")
    ticTacToe = QApplication(sys.argv)

    view = TicTacToeUI()
    controller = TicTacToeCtrl(view)
    view.show()
    sys.exit(ticTacToe.exec())
