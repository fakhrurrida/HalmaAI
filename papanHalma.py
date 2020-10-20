from square import Square
import fungsiobjektif
import math
import fungsikemenangan
import time
import random
import copy

class Papan():
    
    def __init__(self, b_size, time_max, pilihan):
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
        self.time_limit = time_max
        self.time_mulai = time.time()
        self.current_turn = Square.P_GREEN
        self.eksekusi = False
        self.win = False
        self.green_goals = fungsikemenangan.getAllGreen(self.board)
        self.red_goals = fungsikemenangan.getAllRed(self.board)
        self.pilihan = pilihan
        
        if(pilihan == 1 or pilihan == 2):
            print("Sebagai player, Anda ingin jadi pemain yang mana?")
            print("Red (Ketik 2) / Green (Ketik 1)")
            tile_pemain = int(input())
            self.tile_pemain = tile_pemain
            # if(tile_pemain == 1):
            #     self.computer = Square.P_RED
            # else:
            #     self.computer = Square.P_GREEN
            print("")
            print("Bentuk papan halma pertama:")
            self.tryDisplay()
            while (not self.win):
                if self.current_turn == self.computer:
                    print("Sekarang giliran:", (self.current_turn if self.tile_pemain==1 else 1))
                    self.execute_computer()
                    print("Papan halma menjadi:")
                    self.tryDisplay()
                    print("")
                    
                else:
                    print("Sekarang giliran:", (self.current_turn if self.tile_pemain==1 else 2)) 
                    self.move_player()
                    print("")
                    print("Papan halma menjadi:")
                    self.tryDisplay()
                    print("")
        
    #Fungsi eksekusi move computer/Red (AI)
    #def execute(self):

    def move(self, before, after):
        #after.piece = before.piece
        #before.piece = Square.P_NONE
        self.board[after.row][after.col].piece = self.board[before.row][before.col].piece
        self.board[before.row][before.col].piece = Square.P_NONE


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
    
    
    # def minimax(self, max_time, a=float("-inf"),
    #             b=float("inf"), maxing=True, depth=3):

    #     # Bottomed out base case
    #     if depth == 0 or fungsikemenangan.cekWinner(self.board, self.red_goals, self.green_goals) or time.time() > max_time:
    #         return self.utility_distance(), None

    #     # Setup initial variables and find moves
    #     best_move = None
        
    #     # if maxing:
    #     #     best_val = float("-inf")
    #     #     moves = self.get_next_moves(player_to_max)
    #     # else:
    #     #     best_val = float("inf")
    #     #     moves = self.get_next_moves((Square.P_RED
    #     #             if player_to_max == Square.P_GREEN else Square.P_GREEN))

    #     best_val = math.inf if maxing else -math.inf
        
    #     moves = []
    #     i=0
    #     print(self.board[5][5].piece)    
    #     if maxing:
    #         print("MAXIMIZING")
    #         allRed = fungsikemenangan.getAllRed(self.board)
    #         for square in allRed:
    #             row, col = square.loc
    #             move = self.possibleMoveAndJump(self.board, row, col, [])
    #             moves.append((square, move))

    #     else:
    #         print("MINIMIZING")
    #         allGreen = fungsikemenangan.getAllGreen(self.board)
    #         for square in allGreen:
    #             row, col = square.loc
    #             move = self.possibleMoveAndJump(self.board, row, col, [])
    #             moves.append((square,move))
        
    #     # For each move
    #     for move in moves:
    #         for to in move[1]:

    #             # Bail out when we're out of time
    #             if time.time() > max_time:
    #                 return best_val, best_move

    #             # Move piece to the move outlined
    #             piece = move[0].piece
    #             move[0].piece = Square.P_NONE
    #             to.piece = piece

    #             # Recursively call self
    #             val, _ = self.minimax(
    #                 max_time, a, b, not maxing, depth - 1)
                
    #             # Move the piece back
    #             to.piece = Square.P_NONE
    #             move[0].piece = piece

    #             if maxing and val > best_val:
    #                 best_val = val
    #                 best_move = (move[0].loc, to.loc)
    #                 a = max(a, val)

    #             if not maxing and val < best_val:
    #                 best_val = val
    #                 best_move = (move[0].loc, to.loc)
    #                 b = min(b, val)

    #             if b <= a:
    #                 return best_val, best_move

    #     return best_val, best_move
    
    
    # def minimax(self, t_limit, a=-math.inf, b=math.inf, maximizing=True,  depth=3):
        

    #     #basis
    #     if depth == 0 or fungsikemenangan.cekWinner(self.board, self.red_goals, self.green_goals) or time.time() > t_limit:
            
    #         return fungsiobjektif.gameStateValue(self.board), None
    
    #     bestValue = math.inf if maximizing else -math.inf
    #     bestMove = None
    #     moves = []
    #     i=0
    #     print(self.board[5][5].piece)    
    #     if maximizing:
    #         print("MAXIMIZING")
    #         allRed = fungsikemenangan.getAllRed(self.board)
    #         for square in allRed:
    #             row, col = square.loc
    #             move = self.possibleMoveAndJump(self.board, row, col, [])
    #             moves.append((square, move))

    #     else:
    #         print("MINIMIZING")
    #         allGreen = fungsikemenangan.getAllGreen(self.board)
    #         for square in allGreen:
    #             row, col = square.loc
    #             move = self.possibleMoveAndJump(self.board, row, col, [])
    #             moves.append((square,move))
        
    #     print(depth)
    #     print(len(moves))
    #     # print("MAsuk ga")
    #     for move in moves:
    #         for tujuan in move[1]:
                
    #             if time.time() > t_limit:
    #                 return bestValue, bestMove
                
    #             # self.move(move[0], tujuan)
                
    #             print("------------------------")
                
    #             piece = move[0].piece
    #             move[0].piece = Square.P_NONE
    #             tujuan.piece = piece
                
    #             value, Move = self.minimax(t_limit, a, b, not maximizing, depth-1)
                
    #             print(value)
    #             #print(bestMove[0].loc,bestMove[1].loc)
    #             print("LEWATIN REKURSIF")

    #             tujuan.piece = Square.P_NONE
    #             move[0].piece = piece
                
    #             if maximizing and value < bestValue:  #BALIKIN LAGI TANDANYA JANGAN LUPA
    #                 bestValue = value
    #                 bestMove = (move[0].loc, tujuan.loc)
    #                 a = max(a, value)
    #                 print("MAXING")

    #             if not maximizing and value > bestValue:
    #                 bestValue = value
    #                 bestMove = (move[0].loc, tujuan.loc)
    #                 b = min(b, value)
    #                 print("MINING")

    #             if b <= a:
    #                 ("DAPET B")
    #                 return bestValue, bestMove
    #     # return int, (squareAwal.loc, squareTujuan.loc)
    #     # print(bestMove)
    #     return bestValue, bestMove
    
    def moveBoardBaru(self, boardBaru, squareAwal, squareTujuan):
        boardBaru[squareTujuan.row][squareTujuan.col] = boardBaru[squareAwal.row][squareAwal.col]
        boardBaru[squareAwal.row][squareAwal.col] = Square.P_NONE
    
    
    def minimax(self, boardBaru, t_limit, a=-math.inf, b=math.inf, maximizing=True,  depth=3):
        #basis
        if depth == 0 or fungsikemenangan.cekWinner(boardBaru, self.red_goals, self.green_goals) or time.time() > t_limit:
            
            return fungsiobjektif.gameStateValue(boardBaru), None
    
        bestValue = float("-inf") if maximizing else float("inf")
        bestMove = None
        moves = []
        i=0
        #print(self.board[5][5].piece, ",", self.board[6][6].piece)    
        if maximizing:
            allRed = fungsikemenangan.getAllRed(boardBaru)
            for square in allRed:
                row, col = square.loc
                move = self.cleanPossibleMoveAndJump(row, col, self.possibleMoveAndJump(boardBaru, row, col, []))
                moves.append((square, move))

        else:
            allGreen = fungsikemenangan.getAllGreen(boardBaru)
            for square in allGreen:
                row, col = square.loc
                move = self.cleanPossibleMoveAndJump(row, col, self.possibleMoveAndJump(boardBaru, row, col, [])) 
                moves.append((square,move))
                
        
        
        # bestMove = None
        # if maximizing:
        #     bestValue = float("-inf")
        #     moves = self.get_next_moves(Square.P_RED)
        # else:
        #     bestValue= float("inf")
        #     moves = self.get_next_moves((Square.P_GREEN))
        
        #print(depth)
        #print(len(moves))
        # print("MAsuk ga")
        for move in moves:
            for tujuan in move[1]:
                
                if time.time() > t_limit:
                    return bestValue, bestMove
                
                # self.move(move[0], tujuan)
                
                #print("------------------------")
                
                piece = move[0].piece
                move[0].piece = Square.P_NONE
                tujuan.piece = piece
                
                #boardBaru[tujuan.row][tujuan.col] = boardBaru[move[0].row][move[0].col]
                #boardBaru[move[0].row][move[0].col] = Square.P_NONE
                
                value, Move = self.minimax(boardBaru, t_limit, a, b, not maximizing, depth-1)
                
                #print(value)
                #print(bestMove[0].loc,bestMove[1].loc)
                #print("LEWATIN REKURSIF")
                
                #boardBaru[move[0].row][move[0].col] = 
                # boardBaru[tujuan.row][tujuan.col] = Square.P_NONE
                #print(value)
                #print(bestMove[0].loc,bestMove[1].loc)

                tujuan.piece = Square.P_NONE
                move[0].piece = piece
                
                if maximizing and value > bestValue:  #BALIKIN LAGI TANDANYA JANGAN LUPA
                    bestValue = value
                    bestMove = (move[0].loc, tujuan.loc)
                    a = max(a, value)
                    #print("MAXING")

                if not maximizing and value < bestValue:
                    bestValue = value
                    bestMove = (move[0].loc, tujuan.loc)
                    b = min(b, value)
                    #print("MINING")

                if b <= a:
                    #("DAPET B")
                    return bestValue, bestMove
        # return int, (squareAwal.loc, squareTujuan.loc)
        # print(bestMove)
        return bestValue, bestMove
    
    def minimaxLocal(self, boardBaru, t_limit, a=-math.inf, b=math.inf, maximizing=True,  depth=3):
        #basis
        if depth == 0 or fungsikemenangan.cekWinner(boardBaru, self.red_goals, self.green_goals) or time.time() > t_limit:
            
            return fungsiobjektif.gameStateValue(boardBaru), None
    
        bestValue = float("-inf") if maximizing else float("inf")
        bestMove = None
        moves = []
        i=0
        #print(self.board[5][5].piece, ",", self.board[6][6].piece)    
        if maximizing:
            allRed = fungsikemenangan.getAllRed(boardBaru)
            for square in allRed:
                row, col = square.loc
                move = self.cleanPossibleMoveAndJump(row, col, self.possibleMoveAndJump(boardBaru, row, col, []))
                moves.append((square, move))

        else:
            allGreen = fungsikemenangan.getAllGreen(boardBaru)
            for square in allGreen:
                row, col = square.loc
                move = self.cleanPossibleMoveAndJump(row, col, self.possibleMoveAndJump(boardBaru, row, col, [])) 
                moves.append((square,move))
                
        
        
        # bestMove = None
        # if maximizing:
        #     bestValue = float("-inf")
        #     moves = self.get_next_moves(Square.P_RED)
        # else:
        #     bestValue= float("inf")
        #     moves = self.get_next_moves((Square.P_GREEN))
        
        #print(depth)
        #print(len(moves))
        # print("MAsuk ga")
        randAwal = random.randint(0, len(moves)-1)
        moveAwal = moves[randAwal]
        for tujuan in moveAwal[1]:
            
            if time.time() > t_limit:
                    return bestValue, bestMove
                
                # self.move(move[0], tujuan)
                
                #print("------------------------")
            
            piece = moveAwal[0].piece
            moveAwal[0].piece = Square.P_NONE
            tujuan.piece = piece
            
            #boardBaru[tujuan.row][tujuan.col] = boardBaru[move[0].row][move[0].col]
            #boardBaru[move[0].row][move[0].col] = Square.P_NONE
            
            value, Move = self.minimax(boardBaru, t_limit, a, b, not maximizing, depth-1)
            
            #print(value)
            #print(bestMove[0].loc,bestMove[1].loc)
            #print("LEWATIN REKURSIF")
            
            #boardBaru[move[0].row][move[0].col] = 
            # boardBaru[tujuan.row][tujuan.col] = Square.P_NONE
            #print(value)
            #print(bestMove[0].loc,bestMove[1].loc)

            tujuan.piece = Square.P_NONE
            moveAwal[0].piece = piece
            
            if maximizing and value > bestValue:  #BALIKIN LAGI TANDANYA JANGAN LUPA
                bestValue = value
                bestMove = (moveAwal[0].loc, tujuan.loc)
                a = max(a, value)
                #print("MAXING")

            if not maximizing and value < bestValue:
                bestValue = value
                bestMove = (moveAwal[0].loc, tujuan.loc)
                b = min(b, value)
                #print("MINING")

            if b <= a:
                #("DAPET B")
                return bestValue, bestMove
        # return int, (squareAwal.loc, squareTujuan.loc)
        # print(bestMove)
        return bestValue, bestMove
        
        # for move in moves:
        #     for tujuan in move[1]:
                
        #         if time.time() > t_limit:
        #             return bestValue, bestMove
                
        #         # self.move(move[0], tujuan)
                
        #         #print("------------------------")
                
        #         piece = move[0].piece
        #         move[0].piece = Square.P_NONE
        #         tujuan.piece = piece
                
        #         #boardBaru[tujuan.row][tujuan.col] = boardBaru[move[0].row][move[0].col]
        #         #boardBaru[move[0].row][move[0].col] = Square.P_NONE
                
        #         value, Move = self.minimax(boardBaru, t_limit, a, b, not maximizing, depth-1)
                
        #         #print(value)
        #         #print(bestMove[0].loc,bestMove[1].loc)
        #         #print("LEWATIN REKURSIF")
                
        #         #boardBaru[move[0].row][move[0].col] = 
        #         # boardBaru[tujuan.row][tujuan.col] = Square.P_NONE
        #         #print(value)
        #         #print(bestMove[0].loc,bestMove[1].loc)

        #         tujuan.piece = Square.P_NONE
        #         move[0].piece = piece
                
        #         if maximizing and value > bestValue:  #BALIKIN LAGI TANDANYA JANGAN LUPA
        #             bestValue = value
        #             bestMove = (move[0].loc, tujuan.loc)
        #             a = max(a, value)
        #             #print("MAXING")

        #         if not maximizing and value < bestValue:
        #             bestValue = value
        #             bestMove = (move[0].loc, tujuan.loc)
        #             b = min(b, value)
        #             #print("MINING")

        #         if b <= a:
        #             #("DAPET B")
        #             return bestValue, bestMove
        # # return int, (squareAwal.loc, squareTujuan.loc)
        # # print(bestMove)
        # return bestValue, bestMove
    
    
    def copyBoard(self, boardLama):
        boardBaru = [[None for i in range(len(boardLama))] for j in range(len(boardLama))]
        
        for baris in range(len(boardLama)):
            for kolom in range(len(boardLama)):
                a = boardLama[baris][kolom]
                x = Square(a.tile, a.piece, a.row, a.col)
                boardBaru[baris][kolom] = x
        return boardBaru

    def execute_computer(self):
        self.eksekusi = True
        print("")
        print("Sedang berpikir............................")
        print("")
        y = self.copyBoard(self.board)
        waktu_maks = time.time() + self.time_limit
        waktu_mulai = time.time()
        if self.pilihan == 1:
            minimaxValue, best_move = self.minimax(y, waktu_maks)
        elif self.pilihan == 2:
            minimaxValue, best_move = self.minimaxLocal(y, waktu_maks)
            
        waktu_akhir = time.time()
        print("Waktu minimax: ", waktu_akhir-waktu_mulai)
        print("Perpindahan kotak yang dipilih: ", best_move)
        print("Dengan value yang diambil sbesar: ", minimaxValue)
        square_before = self.board[best_move[0][0]][best_move[0][1]]
        square_after = self.board[best_move[1][0]][best_move[1][1]]
        #self.tryDisplay()
        print("Kotak sebelum: ",square_before.getLoc())
        print("Pindah ke kotak:",square_after.getLoc())

        self.move(square_before,square_after)


        
        isWin = fungsikemenangan.cekWinner(self.board, self.red_goals, self.green_goals)
        if (isWin):
            if (isWin == Square.P_GREEN):
                print("PLAYER WINNER WINNER CHICKEN DINNER")
            elif (isWin == Square.P_RED):
                print("COMPUTER WINNER WINNER CHICKEN DINNER")
            self.current_turn = None
            self.win = True
        else:
            if (self.current_turn == Square.P_GREEN):
                self.current_turn = Square.P_RED
            elif (self.current_turn == Square.P_RED):
                self.current_turn = Square.P_GREEN
        
        
        self.eksekusi = False

    def move_player(self):
        board = self.board
        possible_tetangga = []
        kolom_tujuan = -999
        row_tujuan = -999
        status_asal = False

        while (status_asal == False):
            print("Masukkan titik asal yang sesuai yang tersedia!")
            row = int(input("Masukkan row dari titik yang ingin dipindah: "))
            kolom = int(input("Masukkan kolom dari titik yang ingin dipindah: "))
            if(board[row][kolom].piece == 1):
                status_asal = True
        for a in (self.cleanPossibleMoveAndJump(row, kolom, self.possibleMoveAndJump(board, row, kolom, [])) ):
            #print(a)
            possible_tetangga.append(a.getLoc())
            print("Possible Moves: ", a.getLoc())
        
        while ((kolom_tujuan, row_tujuan) not in possible_tetangga):   
            print("Masukkan titik tujuan yang sesuai dengan pilihan tetangga yang tersedia!")
            kolom_tujuan = int(input("Masukkan row dari titik yang ingin dituju: "))
            row_tujuan = int(input("Masukkan kolom dari titik yang ingin dituju: ")) 
            
        self.move(self.board[row][kolom], self.board[kolom_tujuan][row_tujuan])

        isWin = fungsikemenangan.cekWinner(board, self.red_goals, self.green_goals)
        if (isWin):
            if (isWin == Square.P_GREEN):
                print("PLAYER WINNER WINNER CHICKEN DINNER")
            elif (isWin == Square.P_RED):
                print("COMPUTER WINNER WINNER CHICKEN DINNER")
            self.current_turn = None
            self.win = True
        else:
            if (self.current_turn == Square.P_GREEN):
                self.current_turn = Square.P_RED
            elif (self.current_turn == Square.P_RED):
                self.current_turn = Square.P_GREEN

    def tryDisplay(self):
        angka = 0
        if (self.tile_pemain == 1):
            for shaf in range (self.b_size):
                for banjar in range (self.b_size):
                    if (banjar != self.b_size-1):                  
                        print(self.board[shaf][banjar].piece, end=" ")
                    else:
                        print(self.board[shaf][banjar].piece)
                    angka+=1
        elif (self.tile_pemain == 2):
            for shaf in range (self.b_size):
                for banjar in range (self.b_size):
                    if (banjar != self.b_size-1): 
                        if(self.board[shaf][banjar].piece == 1):               
                            print(2, end=" ")
                        elif(self.board[shaf][banjar].piece == 2):
                            print(1, end=" ")
                        else:
                            print(0, end=" ")
                    else:
                        if(self.board[shaf][banjar].piece == 1):               
                            print(2)
                        elif(self.board[shaf][banjar].piece == 2):
                            print(1)
                        else:
                            print(0)
                    angka+=1
        #print(angka)

    def cleanPossibleMoveAndJump(self, shaf, banjar, list_sebelah):
        for sebelah in list_sebelah:
            if (self.current_turn==Square.P_GREEN):
                if (self.board[shaf][banjar].tile==0 and sebelah.tile==Square.P_GREEN):
                    list_sebelah.remove(sebelah)
            elif (self.current_turn==Square.P_RED):
                if (self.board[shaf][banjar].tile==0 and sebelah.tile==Square.P_RED):
                    list_sebelah.remove(sebelah)
        return list_sebelah

    def possibleMoveAndJump(self, board, shaf, banjar, list_sebelah=[], isJumpMove=False):
        if (list_sebelah is None):
            # print("masuk list kosong")
            list_sebelah = []

        occupy = [0, 1, 2]
        if (board[shaf][banjar].tile != board[shaf][banjar].piece):
            # print("masuk remove 1")
            occupy.remove(1)
        if (board[shaf][banjar].tile != 0) and (board[shaf][banjar].piece != board[shaf][banjar].tile):
            # print("masuk remove 0")
            occupy.remove(0)

        for i in ([-1, 0, 1]):
            for j in ([-1, 0, 1]):
                banjar_tetangga = banjar + i
                shaf_tetangga = shaf + j
            
                # skip invalid move
                if (banjar_tetangga == banjar and shaf_tetangga == shaf) or (shaf_tetangga < 0 or banjar_tetangga < 0 or shaf_tetangga > self.b_size-1 or banjar_tetangga > self.b_size-1):
                    continue
                
                tetangga = board[shaf_tetangga][banjar_tetangga]
                if (tetangga.tile not in occupy):
                    continue
                if (tetangga.piece == 0):
                    if (not isJumpMove):
                        list_sebelah.append(tetangga)
                    continue
                
                # Check jump tiles
                jump_shaf = shaf_tetangga + j
                jump_banjar = banjar_tetangga + i
                
                if (jump_shaf < 0 or jump_banjar < 0 or jump_shaf > self.b_size-1 or jump_banjar > self.b_size-1):
                    continue
                
                jump_tetangga = board[jump_shaf][jump_banjar]
                if (jump_tetangga in list_sebelah) or (jump_tetangga.tile not in occupy):
                    continue

                if jump_tetangga.piece == 0:
                    list_sebelah.insert(0, jump_tetangga)
                    self.possibleMoveAndJump(board, jump_tetangga.getLoc()[0], jump_tetangga.getLoc()[1], list_sebelah, True)
        return list_sebelah
    
    # def utility_distance(self):
    
    #     def point_distance(p0, p1):
    #         return math.sqrt((p1[0] - p0[0])**2 + (p1[1] - p0[1])**2)

    #     value = 0

    #     for col in range(self.b_size):
    #         for row in range(self.b_size):

    #             tile = self.board[row][col]

    #             if tile.piece == Square.P_GREEN:
    #                 distances = [point_distance(tile.loc, g.loc) for g in
    #                              self.red_goals if g.piece != Square.P_GREEN]
    #                 value -= max(distances) if len(distances) else -50

    #             elif tile.piece == Square.P_RED:
    #                 distances = [point_distance(tile.loc, g.loc) for g in
    #                              self.green_goals if g.piece != Square.P_RED]
    #                 value += max(distances) if len(distances) else -50

    #     return value*-1

print("SELAMAT DATANG DI PERMAINAN HALMA XIXIXI")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")
print("")
besar_papan = int(input("Silahkan masukkan besar papan halma:"))
max_time = int(input("Silahkan masukkan waktu maksimal Computer berpikir dalam detik(Untuk efisiensi pilih 10-30): "))
print("MENU PERMAINAN")
print("1. Computer (Minimax) vs Player")
print("2. Computer (Minimax + Local Search) vs Player")
print("3. Computer (Minimax) vs Computer (Minimax + Local Search)")
menu = int(input("Masukkan menu yang diinginkan: "))
print("SELAMAT BERMAIN HEHE!")
b = Papan(besar_papan, max_time, menu)
#b = Papan(8)
# b.board[2][2].piece = 1
# b.board[7][7].piece = 0
# b.tryDisplay()
# for sebelah in b.possibleMoveAndJump(b.board, 0, 2, []):
#     print(sebelah.getLoc())