
class Pawn():
    line = 0
    column = 0
    team = ""
    def __init__(self , line , column , team):
        self.line = line
        self.column = column
        self.team = team #white or black
    
    #return a list of possible points where the pawn can move
    #on the given board
    def GetPossibleMoves(self , board):
        possible_moves = []
        piece = board[self.line][self.column]
        