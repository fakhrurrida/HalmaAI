from square import Square
from math import *

pairedRed = [] # RED's GOAL, has been set as nearest
pairedGreen = [] # GREEN's GOAL, has been set as nearest

def jarakTitik(pInit, pGoal):
# pInit, pGoal --> Square
    return sqrt(pow((pInit.row - pGoal.row), 2) + pow((pInit.col - pGoal.col), 2))

def findNearest(pInit, board):
# pInit --> Square
    b_size = len(board)
    jarak = -100
    nearest = (None, None)

    if (pInit.piece == Square.P_GREEN):
        for row in range(3):
            for col in range(3):
                if (((row + col) < 4) and ((row, col) not in pairedGreen)): # GREEN's GOAL
                    if not(board[row][col].piece == Square.P_GREEN): # unassigned with GREEN
                        thisJarak = jarakTitik(pInit, board[row][col])
                        if (thisJarak < jarak):
                            jarak = thisJarak
                            nearest = (row, col)
        pairedGreen.append(nearest)

    else: #  pInit.piece == Square.P_RED
        for row in range((b_size-4), b_size):
            for col in range((b_size-4), b_size):
                if ((row + col > 2 * (b_size - 3)) and ((row, col) not in pairedRed)): # RED's GOAL
                    if not(board[row][col].piece == Square.P_RED): # unassigned with RED
                        thisJarak = jarakTitik(pInit, board[row][col])
                        if (thisJarak < jarak):
                            jarak = thisJarak
                            nearest = (row, col)
        pairedRed.append(nearest)

    return nearest, jarak # TUPLE, integer


def gameStateValue(board): 
    # def getAllRed(board):
    # # location of RED 
    #     locOfRed = []
    #     for row in range(len(board)):
    #         for col in range(len(board)):
    #             if (board[row][col].piece == Square.P_RED):
    #                 locOfRed.append(row,col)
    #     return locOfRed


    # def getAllGreen(board):
    # # location of GREEN
    #     locOfGreen = []
    #     for row in range(len(board)):
    #         for col in range(len(board)):
    #             if (board[row][col].piece == Square.P_RED):
    #                 locOfGreen.append(row,col)
    #     return locOfGreen

    jarakRed = 0
    jarakGreen = 0

    for row in range(len(board)):
        for col in range(len(board)):
            if (board[row][col].piece == Square.P_RED): # assumption: computer == RED
                    thisSquare = board[row][col] # SQUARE
                    near, jarak = findNearest(thisSquare, board)
                    jarakRed += jarak
            
            elif (board[row][col].piece == Square.P_GREEN): # assumption: computer == RED
                    thisSquare = board[row][col] # SQUARE
                    near, jarak = findNearest(thisSquare, board)
                    jarakGreen += jarak
    
    totalJarak = jarakRed - jarakGreen
    return (totalJarak * (-1))

