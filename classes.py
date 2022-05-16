from pprint import pprint

class Player:
    def __init__(self, marker: str='X', isHuman: bool=True):
        self.marker = marker
        self.isHuman = isHuman
        self.isWinner = False

    def getPlayerMove(self):
        pass



class GameBoard:
    def __init__(self):
        self.grid = [["" for j in range(3)] for i in range(3)]  # 3x3 grid


    def markPosition(self, player: Player, pos=[]):
        print(player.marker)
        print(pos)
        if self.grid[pos[0]][pos[1]] == "":
            self.grid[pos[0]][pos[1]] = player.marker  # pos marked by player
            return True # to signify success
        else: # pos already marked, either by player or the enemy player
            print("Pos taken")
            return False

    def clearBoard(self):
        self.grid = [["" for j in range(3)] for i in range(3)]  # make grid 3x3 empty grid again


    def printGameBoard(self):
        pprint(self.grid)



class TicTacToe:
    def __init__(self, gameBoard, player):
        self.gameBoard = gameBoard
        self.player = player
        self.computer = Player(marker='O', isHuman=False)
        self.playerTurn = True # player's turn initialized to true since player gets to go first
        self.scoreBoard = {self.player.marker: 0, self.computer.marker: 0}
        self.winner = None

    def checkIfWinner(self):
        # Checks all horizontal and vertical rows to see if any winner
        for row in range(3):
            horizontalPattern = ""
            verticalPattern = ""
            for col in range(3):
                horizontalPattern = horizontalPattern + self.gameBoard.grid[row][col] # so if row = 2, col = 3
                verticalPattern = verticalPattern + self.gameBoard.grid[col][row]  # then row = 3 and col = 2
            if horizontalPattern == "XXX" or verticalPattern == "XXX":
                self.player.isWinner = True
                self.scoreBoard[self.player.marker] += 1  # increment win count for user for the score board
                return True
            elif horizontalPattern == "OOO" or verticalPattern == "OOO":
                self.computer.isWinner = True
                self.scoreBoard[self.computer.marker] += 1  # increment win count for user for the score board
                return True

        # checks the diagnol rows to see if winner
        diagnol1 = self.gameBoard.grid[0][0] + self.gameBoard.grid[1][1] + self.gameBoard.grid[2][2]
        diagnol2 = self.gameBoard.grid[2][0] + self.gameBoard.grid[1][1] + self.gameBoard.grid[0][2]
        if diagnol1 == "XXX" or diagnol2 == "XXX":
            self.player.isWinner = True
            self.scoreBoard[self.player.marker] += 1  # increment win count for user for the score board
            return True
        elif diagnol1 == "OOO" or diagnol2 == "OOO":
            self.computer.isWinner = True
            self.scoreBoard[self.computer.marker] += 1  # increment win count for user for the score board
            return True

        return False # NO WINNER


    def checkWhoWon(self):
        if self.player.isWinner:
            return self.player.marker
        elif self.computer.isWinner:
            return self.computer.marker
        else:  # Both didn't win, meaning a draw
            return "None"


    def endGame(self):
        pass





