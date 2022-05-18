from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QToolBar, QComboBox, QStackedWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class TicTacToeUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TIC TAC TOE")
        self.setFixedSize(780, 720)
        self.setGeometry(100, 100, 280, 80)
        self.mainLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self._centralWidget)
        self.left_side_layout = QVBoxLayout()
        self.game_with_score_board = QHBoxLayout()

        self._createToolBar()
        self._createTitle()
        self._createBoardSizeComboBoxMenu()
        self._createGrids()
        self._createScoreBoard()

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction("Exit", self.close)

    def _createTitle(self):
        title = QLabel("TIC TAC TOE")
        title.setStyleSheet("QLabel {color : green; font-size: 80pt; font-weight: 80pt; font-family: Georgia}")
        self.mainLayout.addWidget(title, alignment=Qt.AlignLeft)

    def _createBoardSizeComboBoxMenu(self):
        boardSizeLayout = QVBoxLayout()
        label = QLabel("Board Dimensions")
        label.setStyleSheet("QLabel {font-weight: bold;}")
        boardSizeLayout.addWidget(label)
        self.boardSizeComboBox = QComboBox()
        self.boardSizeComboBox.addItem("3x3")
        self.boardSizeComboBox.addItem("4x4")
        self.boardSizeComboBox.setFixedWidth(80)
        boardSizeLayout.addWidget(self.boardSizeComboBox)
        self.left_side_layout.addLayout(boardSizeLayout)

    # Creates the 3x3 and the 4x4 grids and adds them to a stacked widget
    def _createGrids(self):
        self.stackedWidget = QStackedWidget()
        self._create3x3Grid()
        self._create4x4Grid()

        self.stackedWidget.addWidget(self.grid3x3Widget)  # added to stackedWidget at index 0
        self.stackedWidget.addWidget(self.grid4x4Widget)  # added to stackedWidget at index 1

        self.left_side_layout.addWidget(self.stackedWidget)  # add to the left layout
        # added to the left side of the horizontal layout
        self.game_with_score_board.addLayout(self.left_side_layout)


    def _create3x3Grid(self):
        grid3x3Layout = QGridLayout()
        self.grid3x3Widget = QWidget()
        self.buttons3x3 = {}
        for row in range(3):
            for col in range(3):
                button = QPushButton()
                # button.setFixedSize(150, 150)
                button.setMinimumSize(150, 150)
                button.setMaximumSize(400, 400)
                button.setFont(QFont("Times", 100, QFont.Bold))
                button.setStyleSheet("QPushButton {background-color: pink}")

                self.buttons3x3[f"{row}{col}"] = button
                grid3x3Layout.addWidget(button, row, col)
                grid3x3Layout.setSpacing(20)
        self.grid3x3Widget.setLayout(grid3x3Layout)

    def _create4x4Grid(self):
        grid4x4Layout = QGridLayout()
        self.grid4x4Widget = QWidget()
        self.buttons4x4 = {}
        for row in range(4):
            for col in range(4):
                button = QPushButton()
                button.setFixedSize(120, 120)
                button.setFont(QFont("Times", 90, QFont.Bold))
                button.setStyleSheet("QPushButton {background-color: pink}")

                self.buttons4x4[f"{row}{col}"] = button
                grid4x4Layout.addWidget(button, row, col)
        self.grid4x4Widget.setLayout(grid4x4Layout)

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






