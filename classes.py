from pprint import pprint
import random


class Player:
    def __init__(self, marker: str='X', isHuman: bool=True):
        self.marker = marker
        self.isHuman = isHuman
        self.isWinner = False
        self.mostRecentMark = [] # coordinate of board where user marked

    def __str__(self):
        return f"{self.marker}"

    def getPosPlayerMarked(self):
        return self.mostRecentMark


class GameBoard:
    # GameBoard must be be a square so assumes num_rows and num_cols are equal
    def __init__(self, num_rows=3, num_cols=3):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid = [["" for j in range(num_rows)] for i in range(num_cols)]  # 3x3 grid by default
        self.unmarkedPositions = []  # will be initialized with all positions unmarked
        self._initilize_unmarkedPositions()

    def _initilize_unmarkedPositions(self):
        self.unmarkedPositions = []  # make sure to empty it first
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.unmarkedPositions.append(f"{row}{col}")
        print("unmarkedPositions after initialization", self.unmarkedPositions)

    def markPosition(self, player: Player, pos=[]):
        print(f"markPosition called for {player.marker}")
        if len(self.unmarkedPositions) != 0:
            if self.grid[pos[0]][pos[1]] == "":
                self.grid[pos[0]][pos[1]] = player.marker  # pos marked by player
                print(f"Grid just marked {player.marker} at position {pos}")
                self.printGameBoard()
                self.unmarkedPositions.remove(f"{pos[0]}{pos[1]}")  # remove position from unmarkedPositions
                player.mostRecentMark = pos
                return True  # to signify success
            else: # pos already marked, either by player or the enemy player
                print("Failed to mark grid {player.marker} at position {pos} bc pos taken")
                return False

    # resets the board
    def clearBoard(self):
        self.grid = [["" for j in range(self.num_cols)] for i in range(self.num_cols)]  # make grid 3x3 empty grid again
        self._initilize_unmarkedPositions() # reinitialize unmarkedPositions array

    # This method creates a new board of given dimensions and replaces the current board with it.
    def changeBoardSize(self, num_rows, num_cols):
        self.grid = [["" for j in range(num_rows)] for i in range(num_cols)]  # 3x3 grid by default
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._initilize_unmarkedPositions()  # reinitialize the unmarkedPositions array.

    def printGameBoard(self):
        pprint(self.grid)


class TicTacToe:
    def __init__(self, gameBoard, player):
        self.gameBoard = gameBoard
        self.player = player
        self.computer = Player(marker='O', isHuman=False)
        self.scoreBoard = {self.player.marker: 0, self.computer.marker: 0}
        self.winner = None

    def computerMark(self):
        gameBoard = self.gameBoard
        marked = False
        print("unmarkedposition: ", self.gameBoard.unmarkedPositions)
        while not marked:
            if len(self.gameBoard.unmarkedPositions) == 0:  # no more unmarked positions
                break
            else:
                randomPos = random.choice(self.gameBoard.unmarkedPositions)  # randomly choose an unmarked position
                print("randomPos: ", randomPos)
                unmarkedPos = [int(randomPos[0]), int(randomPos[1])]
                marked = gameBoard.markPosition(self.computer, unmarkedPos)  # mark that row,col in board with O

    def playerMark(self, player, pos: []):
        gameBoard = self.gameBoard
        marked = False
        print("unmarkedposition: ", self.gameBoard.unmarkedPositions)

        if len(self.gameBoard.unmarkedPositions) == 0:  # no more unmarked positions
            return
        else:
            marked = gameBoard.markPosition(player, pos)  # mark that row,col in board with O
            if marked:
                return True  # square marked successfully
            else:
                return False # square couldn't be marked. Already marked.

    #  Checks all horizontal, vertical and diagnol rows to see if any winner.
    #  Returns true if there is a winner or a draw, else returns false.
    def checkIfGameOver(self):
        winning_hv_pattern = self._checkHorizontalAndVerticalRows()
        winning_diagnol_pattern = self._checkDiagnolRows()
        if winning_hv_pattern or winning_diagnol_pattern:
            return True

        # If all positions in the gamebord is marked and it had no winning patterns,
        # then there is a draw and game is over so return True.
        if len(self.gameBoard.unmarkedPositions) == 0:
            self.player.isWinner = False
            self.computer.isWinner = False  # fixed the bug that caused some draws to send you won message
            return True

        return False # if the above code didn't return, that means game is not over

    # Checks all horizontal and vertical rows to see if there is a winner.
    # Returns true if winning pattern exists, else returns false
    def _checkHorizontalAndVerticalRows(self):
        # Checks all horizontal and vertical rows to see if any winner
        num_rows = self.gameBoard.num_rows
        num_cols = self.gameBoard.num_cols
        player_winning_pattern = "X" * num_rows
        computer_winning_pattern = "O" * num_rows

        for row in range(num_rows):
            horizontalPattern = ""
            verticalPattern = ""
            for col in range(num_cols):
                horizontalPattern = horizontalPattern + self.gameBoard.grid[row][col]  # so if row = 2, col = 3
                verticalPattern = verticalPattern + self.gameBoard.grid[col][row]  # then row = 3 and col = 2
            if horizontalPattern == player_winning_pattern or verticalPattern == player_winning_pattern:
                self.player.isWinner = True
                self.computer.isWinner = False  # just to be safe
                self.scoreBoard[self.player.marker] += 1  # increment win count for user for the score board
                return True
            elif horizontalPattern == computer_winning_pattern or verticalPattern == computer_winning_pattern:
                self.computer.isWinner = True
                self.player.isWinner = False
                self.scoreBoard[self.computer.marker] += 1  # increment win count for user for the score board
                return True

        return False # No winning horizontal or vertical patterns

    # Checks the diagnol rows to see if there is a winner.
    # Returns true if winning pattern exists, else returns false
    def _checkDiagnolRows(self):
        # checks the diagnol rows to see if winner
        num_rows = self.gameBoard.num_rows
        num_cols = self.gameBoard.num_cols
        player_winning_pattern = "X" * num_rows
        computer_winning_pattern = "O" * num_rows

        diagnol1_pattern = ""
        for row in range(num_rows): # checks the negative slope diagnol
            diagnol1_pattern = diagnol1_pattern + self.gameBoard.grid[row][row] # the negative pattern

        diagnol2_pattern = ""
        col = 0  # start from last row, col 0
        for row in range(num_rows-1, -1, -1): # checks the positive slope diagnol
            print(f"[{row}, {col}]")
            diagnol2_pattern = diagnol2_pattern + self.gameBoard.grid[row][col] # the negative pattern
            col = col + 1

        if diagnol1_pattern == player_winning_pattern or diagnol2_pattern == player_winning_pattern:
            self.player.isWinner = True
            self.computer.isWinner = False  # just to be safe
            self.scoreBoard[self.player.marker] += 1  # increment win count for user for the score board
            return True
        elif diagnol1_pattern == computer_winning_pattern or diagnol2_pattern == computer_winning_pattern:
            self.computer.isWinner = True
            self.player.isWinner = False
            self.scoreBoard[self.computer.marker] += 1  # increment win count for user for the score board
            return True

        return False  # No winning diagnol patterns


    def checkWhoWon(self):
        if self.player.isWinner:
            return self.player.marker
        elif self.computer.isWinner:
            return self.computer.marker


    # Reset board, scoreboard and winner status for new game
    def resetGame(self):
        self.gameBoard.clearBoard() # unmarks all squares of the board
        self.scoreBoard = {self.player.marker: 0, self.computer.marker: 0}
        self.winner = None






