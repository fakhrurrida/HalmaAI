from square import Square
import fungsiobjektif
import math
import validator_langkah
import fungsikemenangan
import time
import random

class Papan():
    
    def __init__(self, b_size):
        board = [[None for i in range(b_size)] for j in range(b_size)]
        
        for row in range(b_size):
            for col in range(b_size):
                if row + col < 4: # RED
                    element = Square(2, 2, row, col)
                elif row + col > 2 * (b_size - 3): # GREEN
                    element = Square(1, 1, row, col)
                else: # EMPTY
                    element = Square(0, 0, row, col)

                board[row][col] = element
    
        #Kondisi Permainan
        self.computer = Square.P_RED
        self.b_size = b_size
        self.board = board
        self.t_limit = 60
        self.selected_square = None
        self.valid_moves = []
        self.current_turn = Square.P_GREEN
        self.eksekusi = False

        self.green_goals = fungsikemenangan.getAllGreen
        self.red_goals = fungsikemenangan.getAllRed

    #if self.current_turn == self.computer:
    #    self.execute()
    
    #Fungsi eksekusi move computer/Red (AI)
    #def execute(self):

    # def move(self, before, after):
    #     after.piece = before.piece
    #     before.piece = Square.P_NONE


    # def validator(self, array):
    #     return array

    # def maxi(self, depth=3, t_limit=60, board=self.board):
    #     if depth == 0:
    #         return None, fungsiobjektif.gameStateValue(self)

    #     redLoc = fungsikemenangan.getAllRed
    #     maxValue = -math.inf
    #     moveTaken = []
    #     for square in redLoc:
    #         row, col = square.loc
    #         move = validator_langkah.possibleMoveAndJump(board, row, col)
    #         moveTaken.append(move)
        
    #     for tetangga in moveTaken:
    #         pass
        
    # def mini(self, depth=3, t_limit=60,board=self.board):
    #     if depth == 0:
    #         return None, fungsiobjektif.gameStateValue(self)
    #         # return movetaken, maxUtil
    #         # return best_val, best_move
    #     greenLoc = fungsikemenangan.getAllGreen
    #     minValue = math.inf
    #     moveTaken = []
    #     for square in greenLoc:
    #         row, col = square.loc
    #         move = validator_langkah.possibleMoveAndJump(board, row, col)
    #         moveTaken.append(move)
        
    #     for tetangga in moveTaken:
    #         continue
        


    def minimax(self, a=-math.inf, b=math.inf, maximizing=True,  depth=3, t_limit=60):
        
        #basis
        if depth == 0 or fungsikemenangan.find_winner(self.board) or time.time() > t_limit:
            moves = []
            for square in allRed:
                row, col = square.loc
                move = validator_langkah.possibleMoveAndJump(board, row, col)
                moves.append((square, move))
            # moves = [(sqaureAwal, [squareTujuan])]
            randAwal = moves[random.randint(0, len(moves))][0]
            jumlahTujuan = len(moves[random.randint(0, len(moves))][1])
            randTujuan = moves[random.randint(0, len(moves))][1][random.randint(0,jumlahTujuan)]
            
            return fungsiobjektif.utility_distance(self.board), (randAwal, randTujuan)
        
        bestValue = math.inf if maximizing else -math.inf
        bestMove = None
        moves = []
        
        if maximizing:
            allRed = fungsikemenangan.getAllRed
            for square in allRed:
                row, col = square.loc
                move = validator_langkah.possibleMoveAndJump(board, row, col)
                moves.append((square, move))
        
        else:
            allGreen = fungsikemenangan.getAllGreen
            for square in allGreen:
                row, col = square.loc
                move = validator_langkah.possibleMoveAndJump(board, row, col)
                moves.append((square,move))
        
        
        for move in moves:
            for tujuan in moves[[1]]:
                
                if time.time()> t_limit:
                    return bestValue, bestMove
                
                self.move(move[0], tujuan)
                
                piece = move[0].piece
                move[0].piece = Square.P_NONE
                tujuan.piece = piece
                
                value, Move = self.minimax(a, b, not maximizing, depth-1)
                
                tujuan.piece = Square.P_NONE
                move[0].piece = piece
                
                if maximizing and value > bestValue:
                    best_val = value
                    best_move = (move[0].loc, tujuan.loc)
                    a = max(a, value)

                if not maximizing and value < best_val:
                    best_val = value
                    best_move = (move[0].loc, tujuan.loc)
                    b = min(b, value)

                if b <= a:
                    return best_val, best_move
        # return int, (squareAwal, squareTujuan)
        return best_val, best_move
        

    