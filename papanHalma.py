from square import Square
import fungsiobjektif
import math
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
        self.time_limit = 60
        self.selected_square = None
        self.valid_moves = []
        self.current_turn = Square.P_GREEN
        self.eksekusi = False

        self.green_goals = fungsikemenangan.getAllGreen(self.board)
        self.red_goals = fungsikemenangan.getAllRed(self.board)

        if self.current_turn == self.computer:
            self.execute()
    
    #Fungsi eksekusi move computer/Red (AI)
    #def execute(self):

    def move(self, before, after):
        after.piece = before.piece
        before.piece = Square.P_NONE


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
                move = possibleMoveAndJump(board, row, col)
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
                move = possibleMoveAndJump(board, row, col)
                moves.append((square, move))
        
        else:
            allGreen = fungsikemenangan.getAllGreen
            for square in allGreen:
                row, col = square.loc
                move = possibleMoveAndJump(board, row, col)
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
                    bestValue = value
                    best_move = (move[0].loc, tujuan.loc)
                    a = max(a, value)

                if not maximizing and value < bestValue:
                    bestValue = value
                    best_move = (move[0].loc, tujuan.loc)
                    b = min(b, value)

                if b <= a:
                    return bestValue, best_move
        # return int, (squareAwal, squareTujuan)
        return bestValue, best_move
    
    def execute_computer(self):
        self.eksekusi = True

        waktu_maks = time.time() + self.time_limit
        waktu_mulai = time.time()

        minimaxValue, best_move = self.minimax()
        waktu_akhir = time.time()
        print("Waktu minimax: ", waktu_akhir-waktu_mulai)

        square_before = self.board[best_move[0][0]][best_move[0][1]]
        square_after = self.board[best_move[1][0]][best_move[1][1]]
        self.move(square_before,square_after)
        
        isWin = fungsikemenangan.cekWinner(board, self.red_goals, self.green_goals)
        if (isWin):
            if (isWin == Square.P_GREEN):
                print("GREEN WINNER WINNER CHICKEN DINNER")
            elif (isWin == Square.P_RED):
                print("RED WINNER WINNER CHICKEN DINNER")
            self.current_turn = None
        else:
            if (self.current_turn == Square.P_GREEN):
                self.current_turn = Square.P_RED
            if (self.current_turn == Square.P_RED):
                self.current_turn = Square.P_GREEN
        
        self.eksekusi = False

    def move_player(self):
        board = self.board
        kolom = int(input("Masukkan kolom dari titik yang ingin dipindah: "))
        row = int(input("Masukkan row dari titik yang ingin dipindah: "))
        for a in (self.possibleMoveAndJump(board,kolom,row)):
            print(a)
            print("tetangga JUMP: ", a.getLoc())
        kolom_tujuan = int(input("Masukkan kolom dari titik yang ingin dituju: "))
        row_tujuan = int(input("Masukkan row dari titik yang ingin dituju: "))
        #if pilihan valid:
        self.move(board[kolom][row], board[kolom_tujuan][row_tujuan])
        isWin = fungsikemenangan.cekWinner(board, self.red_goals, self.green_goals)
        if (isWin):
            if (isWin == Square.P_GREEN):
                print("GREEN WINNER WINNER CHICKEN DINNER")
            elif (isWin == Square.P_RED):
                print("RED WINNER WINNER CHICKEN DINNER")
            self.current_turn = None
        else:
            if (self.current_turn == Square.P_GREEN):
                self.current_turn = Square.P_RED
            if (self.current_turn == Square.P_RED):
                self.current_turn = Square.P_GREEN

    def tryDisplay(self):
        angka = 0
        for shaf in range (self.b_size):
            for banjar in range (self.b_size):
                if (banjar != 7):
                    print(self.board[shaf][banjar].piece, end=" ")
                else:
                    print((self.board[shaf][banjar]).piece)
                angka+=1

    def possibleMoveAndJump(self, board, shaf, banjar, list_sebelah=[], isJumpMove=False):
        if (len(list_sebelah)==0):
            print("masuk list kosong")
            list_sebelah = []

        occupy = [0, 1, 2]
        if (board[shaf][banjar].piece != 1):
            print("masuk remove 1")
            occupy.remove(1)
        if (board[shaf][banjar].piece != 0) and (board[shaf][banjar].piece != 1):
            print("masuk remove 0")
            occupy.remove(0)

        for i in ([-1, 0, 1]):
            for j in ([-1, 0, 1]):
                banjar_tetangga = banjar + i
                shaf_tetangga = shaf + j
            
                # skip invalid move
                if (banjar_tetangga == banjar and shaf_tetangga == shaf) or (shaf_tetangga < 0 or banjar_tetangga < 0 or shaf_tetangga > 7 or banjar_tetangga > 7):
                    continue
                
                tetangga = board[shaf_tetangga][banjar_tetangga]
                if (tetangga.piece not in occupy):
                    continue
                if (tetangga.piece == 0):
                    if (not isJumpMove):
                        list_sebelah.append(tetangga)
                    continue
                
                # Check jump tiles
                jump_shaf = shaf_tetangga + j
                jump_banjar = banjar_tetangga + i
                
                if (jump_shaf < 0 or jump_banjar < 0 or jump_shaf >= 7 or jump_banjar >= 7):
                    continue
                
                jump_tetangga = board[jump_shaf][jump_banjar]
                if (jump_tetangga in list_sebelah) or (jump_tetangga.tile not in occupy):
                    continue

                if jump_tetangga.tile == 0:
                    list_sebelah.insert(0, jump_tetangga)
                    self.possibleMoveAndJump(board, jump_tetangga.getLoc()[0], jump_tetangga.getLoc()[1], list_sebelah, True)
        return list_sebelah

b = Papan(8)
b.tryDisplay()
b.move_player()
b.tryDisplay()
