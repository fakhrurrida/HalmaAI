from square import Square
from math import *
import random

pairedRed = [] # RED's GOAL, has been set as nearest, list of tuple
pairedGreen = [] # GREEN's GOAL, has been set as nearest, list of tuple

def jarakTitik(pInit, pGoal):
# pInit, pGoal --> Square
    return sqrt(pow((pInit.row - pGoal.row), 2) + pow((pInit.col - pGoal.col), 2))

def findRedGoal(board):
# Return list of Square
    listOfRedGoal = []
    n = len(board)
    for row in range(n):
        for col in range(n):
            if (board[row][col].tile == Square.T_RED):
                listOfRedGoal.append(board[row][col])
    return listOfRedGoal

def findGreenGoal(board):
# Return list of Square
    listOfGreenGoal = []
    n = len(board)
    for row in range(n):
        for col in range(n):
            if (board[row][col].tile == Square.T_GREEN):
                listOfGreenGoal.append(board[row][col])
    return listOfGreenGoal

def findNearest(pInit, board):
# pInit --> Square, board --> Papan
# Return (pNearest loc) --> tuple, (jarakTitik pInit and pNearest) --> integer
    jarak = 99999
    nearest = (None, None)
    redGoal = findRedGoal(board)
    greenGoal = findGreenGoal(board)

    n = len(board)
    if (pInit.piece == Square.P_GREEN):
        if (pInit in greenGoal): # ALREADY IN GOAL 
            nearest = pInit.loc
            jarak = 0
        else: # NOT YET IN GOAL
            # iterate all square in board, find the nearest
            for goal in greenGoal: # goal --> square
                if (goal not in pairedGreen):
                    thisJarak = jarakTitik(pInit, goal)
                    
                    if (thisJarak < jarak):
                        jarak = thisJarak
                        nearest = goal.loc
            pairedGreen.append(nearest)

    else: #  pInit.piece == Square.P_RED
        # print("WOI")
        if (pInit in redGoal): # ALREADY IN GOAL 
            nearest = pInit.loc
            jarak = 0
            # print("masuk if")
        else: # NOT YET IN GOAL
            
            # iterate all square in board, find the nearest
            for goal in redGoal: # goal --> square
                # print("masuk else")
                if (goal not in pairedRed):
                    thisJarak = jarakTitik(pInit, goal)
                    # print("MASOK")
                    if (thisJarak < jarak):
                        jarak = thisJarak
                        nearest = goal.loc
            pairedRed.append(nearest)

    return nearest, jarak # TUPLE, integer


def gameStateValue(board): 
    jarakRed = 0
    jarakGreen = 0
    arrRed = []
    arrGreen = []
    for row in range(len(board)):
        for col in range(len(board)):
            thisSquare = board[row][col] # SQUARE
            if (thisSquare.piece == Square.P_RED): # assumption: computer == RED
                    near, jarak = findNearest(thisSquare, board)
                    jarakRed += jarak
                    arrRed.append(jarak)
            
            elif (thisSquare.piece == Square.P_GREEN): # assumption: computer == RED
                    near, jarak = findNearest(thisSquare, board)
                    jarakGreen += jarak
                    arrGreen.append(jarak)
            
    print(arrRed)
    print(arrGreen)
    totalJarak = jarakRed - jarakGreen # assumption: computer == RED
    return (totalJarak * (-1))

# n = 8

# board = [[0 for i in range(n)] for j in range(n)]
# jumlahsatu = 0
# jumlahdua = 0
# for row in range(n):
#     for col in range(n):
#         if (jumlahdua < 10): # dua masih bisa
#             if (jumlahsatu < 10): # satu masih bisa
#                 a = random.randint(0,2) # 0, 1, 2
#             else: # satu udah 10
#                 a = random.randint(0,1) # 0, 1
#                 if (a == 1):
#                     a = 2
#         else: # dua udah 10
#             if (jumlahsatu < 10): # satu masih bisa
#                 a = random.randint(0,1) # 0, 1
#             else: # satu udah 10
#                 a = 0
# # if (row + col < 4) --> T_RED
# # elif (row + col) > (2 * (b_size - 3)) --> T_GREEN
#         if a == 1:
#             jumlahsatu += 1
#             if (row + col < 4): # T_RED
#                 board[row][col] = Square(1, 1, row, col)
#             elif (row + col) > (2 * (len(board) - 3)): # T_GREEN
#                 board[row][col] = Square(2, 1, row, col)
#             else: # T_NONE
#                 board[row][col] = Square(0, 1, row, col)
            
#         elif a == 2:
#             jumlahdua += 1
#             if (row + col < 4): # T_RED
#                 board[row][col] = Square(1, 2, row, col)
#             elif (row + col) > (2 * (len(board) - 3)): # T_GREEN
#                 board[row][col] = Square(2, 2, row, col)
#             else: # T_NONE
#                 board[row][col] = Square(0, 2, row, col)

#         else:
#             if (row + col < 4): # T_RED
#                 board[row][col] = Square(1, 0, row, col)
#             elif (row + col) > (2 * (len(board) - 3)): # T_GREEN
#                 board[row][col] = Square(2, 0, row, col)
#             else: # T_NONE
#                 board[row][col] = Square(0, 0, row, col)
        


# def tryDisplay(board):
#         angka = 0
#         for shaf in range(len(board)):
#             for banjar in range(len(board)):
#                 if (banjar != 7):
#                     print(board[shaf][banjar].piece, end=" ")
#                 else:
#                     print(board[shaf][banjar].piece)
#                 angka+=1

# # for i 
# tryDisplay(board)
# print(gameStateValue(board))