from pprint import pprint
import random

class Player:
    def __init__(self, marker: str='X', isHuman: bool=True):
        self.marker = marker
        self.isHuman = isHuman
        self.isWinner = False
        self.mostRecentMark = [] # coordinate of board where user marked

    def getPosPlayerMarked(self):
        return self.mostRecentMark


class GameBoard:
    def __init__(self):
        self.grid = [["" for j in range(3)] for i in range(3)]  # 3x3 grid
        self.unmarkedPositions = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
                                 # all positions unmarked initially

    def markPosition(self, player: Player, pos=[]):
        print(f"markPosition called for {player.marker}")
        if len(self.unmarkedPositions) != 0:
            if self.grid[pos[0]][pos[1]] == "":
                self.grid[pos[0]][pos[1]] = player.marker  # pos marked by player
                print(f"Grid just marked {player.marker} at position {pos}")
                self.unmarkedPositions.remove(f"{pos[0]}{pos[1]}")  # remove position from unmarkedPositions
                player.mostRecentMark = pos
                return True  # to signify success
            else: # pos already marked, either by player or the enemy player
                print("Failed to mark grid {player.marker} at position {pos} bc pos taken")
                return False

    # reset the board
    def clearBoard(self):
        self.grid = [["" for j in range(3)] for i in range(3)]  # make grid 3x3 empty grid again
        self.unmarkedPositions = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]


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


    def checkIfGameOver(self):
        # Checks all horizontal and vertical rows to see if any winner
        for row in range(3):
            horizontalPattern = ""
            verticalPattern = ""
            for col in range(3):
                horizontalPattern = horizontalPattern + self.gameBoard.grid[row][col]  # so if row = 2, col = 3
                verticalPattern = verticalPattern + self.gameBoard.grid[col][row]  # then row = 3 and col = 2
            if horizontalPattern == "XXX" or verticalPattern == "XXX":
                self.player.isWinner = True
                self.computer.isWinner = False  # just to be safe
                self.scoreBoard[self.player.marker] += 1  # increment win count for user for the score board
                return True
            elif horizontalPattern == "OOO" or verticalPattern == "OOO":
                self.computer.isWinner = True
                self.player.isWinner = False
                self.scoreBoard[self.computer.marker] += 1  # increment win count for user for the score board
                return True

        # checks the diagnol rows to see if winner
        diagnol1 = self.gameBoard.grid[0][0] + self.gameBoard.grid[1][1] + self.gameBoard.grid[2][2]
        diagnol2 = self.gameBoard.grid[2][0] + self.gameBoard.grid[1][1] + self.gameBoard.grid[0][2]
        if diagnol1 == "XXX" or diagnol2 == "XXX":
            self.player.isWinner = True
            self.computer.isWinner = False  # just to be safe
            self.scoreBoard[self.player.marker] += 1  # increment win count for user for the score board
            return True
        elif diagnol1 == "OOO" or diagnol2 == "OOO":
            self.computer.isWinner = True
            self.player.isWinner = False
            self.scoreBoard[self.computer.marker] += 1  # increment win count for user for the score board
            return True

        # If all positions in the gamebord is marked and it had none of the above patterns,
        # then there is a draw and game is over so return True.
        if len(self.gameBoard.unmarkedPositions) == 0:
            return True

        return False  # NO WINNER


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






