from square import Square
import random


def getRedGoals(board):
    array = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==Square.P_RED:
                array.append((i,j))
    return array

def getGreenGoals(board):
    array = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==Square.P_GREEN:
                array.append((i,j))
    return array

def cekWinner(Board, redGoals, greenGoals):
    totalGoals = len(redGoals)
    jumlahMerah = 0
    jumlahHijau = 0
    for Square in redGoals:
        if Square == Square.P_GREEN:
            jumlahHijau += 1
    
    for Square in redGoals:
        if Square == Square.P_RED:
            jumlahMerah += 1
            
    if jumlahHijau == totalGoals:
        return Square.P_GREEN
    elif jumlahMerah == totalGoals:
        return Square.P_RED
    else:
        return None

n = 4

board = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        a = random.randint(0,2)
        if a == 1:
            board[i][j] = Square.P_RED
        else:
            board[i][j] = Square.P_GREEN

print(board)
a = getGreenGoals(board)
b = getRedGoals(board)
print(a)
print(b)
print(cekWinner(board, b, a))