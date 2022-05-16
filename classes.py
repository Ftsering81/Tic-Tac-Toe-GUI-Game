import pprint

class Player:
    def __init__(self,marker: str, isHuman: bool):
        self.marker = marker
        self.isHuman = isHuman

    def getPlayerMove(self):



class GameBoard:
    def __init__(self):
        self.grid = [["" for j in range(3)] for i in range(3)]  # 3x3 grid


    def markPosition(self, player: Player, pos=[]):
        if self.grid[pos[0][pos[1]]] == "":
            self.grid[pos[0][pos[1]]] == player.marker # pos marked by player
            return True # to signify success
        else: # pos already marked, either by player or the enemy player
            return False

    def clearBoard(self):
        self.grid = [[]]


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

    def checkIfWinner(self)
        # if player won then:
        #     scoreBoard[player.marker] += 1  # increment win count for user for the score board
        #     self.winner = player
        pass





