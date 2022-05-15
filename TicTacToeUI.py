import PyQt5
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

class TicTacToeUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TIC TAC TOE")
        self.mainLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self._centralWidget)

        self.createGrid()

    def createGrid(self):
        gridLayout = QGridLayout()
        self.buttons = {}
        for row in range(3):
            for col in range(3):
                button = QPushButton(f"{row}{col}")
                button.setFixedSize(100, 100)
                self.buttons[f"{row}{col}"] = button
                gridLayout.addWidget(button, row, col)

        self.mainLayout.addLayout(gridLayout)






