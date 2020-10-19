from square import Square
import random

def getAllRed(board):
    array = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j].piece == Square.P_RED:
                array.append(board[i][j])
    return array


def getAllGreen(board):
    array = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j].piece == Square.P_GREEN:
                array.append(board[i][j])
    return array

    
def cekWinner(Board, redGoals, greenGoals):
    totalGoals = len(redGoals)
    jumlahMerah = 0
    jumlahHijau = 0

    for kotak in redGoals:
        if kotak.piece == Square.P_GREEN:
            jumlahHijau += 1
    
    for kotak in greenGoals:
        if kotak.piece == Square.P_RED:
            jumlahMerah += 1
            
    if jumlahHijau == totalGoals:
        return Square.P_GREEN
    elif jumlahMerah == totalGoals:
        return Square.P_RED
    else:
        return None

n = 8

board = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        a = random.randint(0,2)
        if a == 1:
            board[i][j] = Square(2, 2, i, j)
        else:
            board[i][j]= Square(1, 1, i, j)


# print(board)
# a = getAllGreen(board)
# # b = getAllRed(board)
# # for x in a:
# #     print(x.loc)

# # print("pemisah")
# # for y in b:
# #     print(y.loc)
# # print(a)
# # print(b)
# print(cekWinner(board, b, a))