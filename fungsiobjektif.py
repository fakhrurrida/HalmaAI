from square import Square
from math import *

pairedRed = [] # RED's GOAL, has been set as nearest, list of tuple
pairedGreen = [] # GREEN's GOAL, has been set as nearest, list of tuple

def jarakTitik(pInit, pGoal):
# pInit, pGoal --> Square
    return sqrt(pow((pInit.row - pGoal.row), 2) + pow((pInit.col - pGoal.col), 2))

def findRedGoal(board):
    listOfRedGoal = []
    n = len(board)
    for row in range(n-4, n):
        for col in range(n-4, n):
            listOfRedGoal.append(board[row][col])
    return listOfRedGoal

def findGreenGoal(board):
    listOfGreenGoal = []
    for row in range(4):
        for col in range(4):
            listOfGreenGoal.append(board[row][col])
    return listOfGreenGoal

def findNearest(pInit, board):
# pInit --> Square, board --> Papan
# Return (pNearest loc) --> tuple, (jarakTitik pInit and pNearest) --> integer
    jarak = -100
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
            for row in range(4):
                for col in range(4):
                    thisLoc = board[row][col]
                    if ((thisLoc in greenGoal) and ((row, col) not in pairedGreen)): # greenGoal and unassigned with Green
                        thisJarak = jarakTitik(pInit, thisLoc)
                        if (thisJarak < jarak):
                            jarak = thisJarak
                            nearest = (row, col)
        pairedGreen.append(nearest)

    else: #  pInit.piece == Square.P_RED
        if (pInit in redGoal): # ALREADY IN GOAL 
            nearest = pInit.loc
            jarak = 0
        else: # NOT YET IN GOAL
            # iterate all square in board, find the nearest
            for row in range(n-4, n):
                for col in range(n-4, n):
                    thisLoc = board[row][col]
                    if (((row + col) > (2 * (n - 3))) and ((row, col) not in pairedRed)): # redGoal and unassigned with Red
                        thisJarak = jarakTitik(pInit, thisLoc)
                        if (thisJarak < jarak):
                            jarak = thisJarak
                            nearest = (row, col)
        pairedRed.append(nearest)

    return nearest, jarak # TUPLE, integer


def gameStateValue(board): 
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
    
    totalJarak = jarakRed - jarakGreen # assumption: computer == RED
    return (totalJarak * (-1))

