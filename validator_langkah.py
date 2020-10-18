from papanHalma import Papan
from square import Square

def tryDisplay(a):
    angka = 0
    for shaf in range (a.b_size):
        for banjar in range (a.b_size):
            if (banjar != 7):
                print(a.board[shaf][banjar].tile, end=" ")
            else:
                print((a.board[shaf][banjar]).tile)
            angka+=1

#mengembalikan list berisi titik-titik di sebelah board[row][col] yang belum ditempati pion lain
def sebelahnyaTitik(player, board, shaf, banjar):
    list_sebelah = []
    if (board[shaf+1][banjar].tile == 0) and (shaf != 7):
        pass
    elif (board[shaf-1][banjar]) and (shaf != 0):
        pass
    elif (board[shaf][banjar+1]) and (banjar != 7):
        pass
    elif (board[shaf][banjar-1]) and (banjar != 0):
        pass
    elif (board[shaf+1][banjar+1]) and (shaf != 7 or banjar != 7):
        pass
    elif (board[shaf-1][banjar-1]) and (shaf != 0 or banjar != 0):
        pass
    elif (board[shaf+1][banjar-1]) and (shaf != 7 or banjar != 0):
        pass
    elif (board[shaf-1][banjar+1]) and (shaf != 0 or banjar != 7):
        pass

def generateTetangga(a, player):
    tetangga_list = []
    if player == 1:
        pass
    if player == 2:
        pass
    for tetangga in (tetangga_list):
        tryDisplay(tetangga)

a = Papan(8)

tryDisplay(a)