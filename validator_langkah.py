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

#mengembalikan list berisi titik-titik di sebelah board[row][col] yang ditempati pion dengan kode pionCode (0,1,2)
def sebelahnyaTitik(pionCode, board, shaf, banjar, list_sebelah=[]):
    if (shaf==7 or shaf == 0 or banjar == 7 or banjar == 0):
        if (shaf == 7 and (banjar != 0 and banjar != 7)):
            if (board[shaf-1][banjar].tile in pionCode) and (shaf != 0):
                list_sebelah.append(board[shaf-1][banjar])
            if (board[shaf][banjar+1].tile in pionCode) and (banjar != 7):
                list_sebelah.append(board[shaf][banjar+1])
            if (board[shaf][banjar-1].tile in pionCode) and (banjar != 0):
                list_sebelah.append(board[shaf][banjar-1])
            if (board[shaf-1][banjar-1].tile in pionCode) and (shaf != 0 or banjar != 0):
                list_sebelah.append(board[shaf-1][banjar-1])
            if (board[shaf-1][banjar+1].tile in pionCode) and (shaf != 0 or banjar != 7):
                list_sebelah.append(board[shaf-1][banjar+1])
        elif (shaf == 0 and (banjar != 0 and banjar != 7)):
            if (board[shaf+1][banjar].tile in pionCode) and (shaf != 7):
                list_sebelah.append(board[shaf+1][banjar])
            if (board[shaf][banjar+1].tile in pionCode) and (banjar != 7):
                list_sebelah.append(board[shaf][banjar+1])
            if (board[shaf][banjar-1].tile in pionCode) and (banjar != 0):
                list_sebelah.append(board[shaf][banjar-1])
            if (board[shaf+1][banjar+1].tile in pionCode) and (shaf != 7 or banjar != 7):
                list_sebelah.append(board[shaf+1][banjar+1])
            if (board[shaf+1][banjar-1].tile in pionCode) and (shaf != 7 or banjar != 0):
                list_sebelah.append(board[shaf+1][banjar-1])
        elif (banjar == 7 and (shaf != 0 and shaf != 7)):
            if (board[shaf+1][banjar].tile in pionCode) and (shaf != 7):
                list_sebelah.append(board[shaf+1][banjar])
            if (board[shaf-1][banjar].tile in pionCode) and (shaf != 0):
                list_sebelah.append(board[shaf-1][banjar])
            if (board[shaf][banjar-1].tile in pionCode) and (banjar != 0):
                list_sebelah.append(board[shaf][banjar-1])
            if (board[shaf-1][banjar-1].tile in pionCode) and (shaf != 0 or banjar != 0):
                list_sebelah.append(board[shaf-1][banjar-1])
            if (board[shaf+1][banjar-1].tile in pionCode) and (shaf != 7 or banjar != 0):
                list_sebelah.append(board[shaf+1][banjar-1])
        elif (banjar == 0 and (shaf != 0 and shaf != 7)):
            if (board[shaf+1][banjar].tile in pionCode) and (shaf != 7):
                list_sebelah.append(board[shaf+1][banjar])
            if (board[shaf-1][banjar].tile in pionCode) and (shaf != 0):
                list_sebelah.append(board[shaf-1][banjar])
            if (board[shaf][banjar+1].tile in pionCode) and (banjar != 7):
                list_sebelah.append(board[shaf][banjar+1])
            if (board[shaf+1][banjar+1].tile in pionCode) and (shaf != 7 or banjar != 7):
                list_sebelah.append(board[shaf+1][banjar+1])
            if (board[shaf-1][banjar+1].tile in pionCode) and (shaf != 0 or banjar != 7):
                list_sebelah.append(board[shaf-1][banjar+1])
        
        elif (shaf == 0 and banjar == 0):
            if (board[shaf+1][banjar].tile in pionCode) and (shaf != 7):
                list_sebelah.append(board[shaf+1][banjar])
            if (board[shaf][banjar+1].tile in pionCode) and (banjar != 7):
                list_sebelah.append(board[shaf][banjar+1])
            if (board[shaf+1][banjar+1].tile in pionCode) and (shaf != 7 or banjar != 7):
                list_sebelah.append(board[shaf+1][banjar+1])
        elif (shaf == 0 and banjar == 7):
            if (board[shaf+1][banjar].tile in pionCode) and (shaf != 7):
                list_sebelah.append(board[shaf+1][banjar])
            if (board[shaf][banjar-1].tile in pionCode) and (banjar != 0):
                list_sebelah.append(board[shaf][banjar-1])
            if (board[shaf+1][banjar-1].tile in pionCode) and (shaf != 7 or banjar != 0):
                list_sebelah.append(board[shaf+1][banjar-1])
        elif (shaf == 7 and banjar == 7):
            if (board[shaf-1][banjar].tile in pionCode) and (shaf != 0):
                list_sebelah.append(board[shaf-1][banjar])
            if (board[shaf][banjar-1].tile in pionCode) and (banjar != 0):
                list_sebelah.append(board[shaf][banjar-1])
            if (board[shaf-1][banjar-1].tile in pionCode) and (shaf != 0 or banjar != 0):
                list_sebelah.append(board[shaf-1][banjar-1])
        elif (shaf == 7 and banjar == 0):
            if (board[shaf-1][banjar].tile in pionCode) and (shaf != 0):
                list_sebelah.append(board[shaf-1][banjar])
            if (board[shaf][banjar+1].tile in pionCode) and (banjar != 7):
                list_sebelah.append(board[shaf][banjar+1])
            if (board[shaf-1][banjar+1].tile in pionCode) and (shaf != 0 or banjar != 7):
                list_sebelah.append(board[shaf-1][banjar+1])
    else:
        if (board[shaf+1][banjar].tile in pionCode) and (shaf != 7):
            list_sebelah.append(board[shaf+1][banjar])
        if (board[shaf-1][banjar].tile in pionCode) and (shaf != 0):
            list_sebelah.append(board[shaf-1][banjar])
        if (board[shaf][banjar+1].tile in pionCode) and (banjar != 7):
            list_sebelah.append(board[shaf][banjar+1])
        if (board[shaf][banjar-1].tile in pionCode) and (banjar != 0):
            list_sebelah.append(board[shaf][banjar-1])
        if (board[shaf+1][banjar+1].tile in pionCode) and (shaf != 7 or banjar != 7):
            list_sebelah.append(board[shaf+1][banjar+1])
        if (board[shaf-1][banjar-1].tile in pionCode) and (shaf != 0 or banjar != 0):
            list_sebelah.append(board[shaf-1][banjar-1])
        if (board[shaf+1][banjar-1].tile in pionCode) and (shaf != 7 or banjar != 0):
            list_sebelah.append(board[shaf+1][banjar-1])
        if (board[shaf-1][banjar+1].tile in pionCode) and (shaf != 0 or banjar != 7):
            list_sebelah.append(board[shaf-1][banjar+1])
    return(list_sebelah)

def possibleMoveAndJump(board, shaf, banjar, list_sebelah=[], isJumpMove=False):
    if (len(list_sebelah)==0):
        print("masuk list kosong")
        list_sebelah = []

    occupy = [0, 1, 2]
    if (board[shaf][banjar].tile != 1):
        print("masuk remove 1")
        occupy.remove(1)
    if (board[shaf][banjar].tile != 0) and (board[shaf][banjar].tile != 1):
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
            if (tetangga.tile not in occupy):
                continue
            if (tetangga.tile == 0):
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
                possibleMoveAndJump(board, jump_tetangga.getLoc()[0], jump_tetangga.getLoc()[1], list_sebelah, True)
    return list_sebelah

def generateTetangga(a, player):
    tetangga_list = []
    if player == 1:
        pass
    if player == 2:
        pass
    for tetangga in (tetangga_list):
        tryDisplay(tetangga)

b = Papan(8)
tryDisplay(b)
for a in (sebelahnyaTitik([0,1,2,3], b.board, 3,4)):
    print("tetangga: ", a.getLoc())

for a in (possibleMoveAndJump(b.board,6,7)):
    print("tetangga JUMP: ", a.getLoc())