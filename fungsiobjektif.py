from square import Square
from math import *

pairedRed = [] # RED's GOAL, has been set as nearest, list of tuple
pairedGreen = [] # GREEN's GOAL, has been set as nearest, list of tuple
print(pairedGreen)
print(pairedRed)

def jarakTitik(pInit, pGoal):
# pInit, pGoal --> Square
    return sqrt(pow((pInit.row - pGoal.row), 2) + pow((pInit.col - pGoal.col), 2))

def findRedGoal(board):
# Return list of Square
    listOfRedGoal = []
    n = len(board)
    for row in range(n-4, board.n):
        for col in range(n-4, n):
            if (board[row][col].piece == Square.P_RED):
                listOfRedGoal.append(board[row][col])
    return listOfRedGoal

def findGreenGoal(board):
# Return list of Square
    listOfGreenGoal = []
    for row in range(4):
        for col in range(4):
            if (board[row][col].piece == Square.P_GREEN):
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
            for goal in greenGoal: # goal --> square
                if (goal not in pairedGreen):
                    thisJarak = jarakTitik(pInit, goal)
                    if (thisJarak < jarak):
                        jarak = thisJarak
                        nearest = goal.loc
            pairedGreen.append(nearest)

    else: #  pInit.piece == Square.P_RED
        if (pInit in redGoal): # ALREADY IN GOAL 
            nearest = pInit.loc
            jarak = 0
        else: # NOT YET IN GOAL
            # iterate all square in board, find the nearest
            for goal in redGoal: # goal --> square
                if (goal not in pairedRed):
                    thisJarak = jarakTitik(pInit, goal)
                    if (thisJarak < jarak):
                        jarak = thisJarak
                        nearest = goal.loc
            pairedRed.append(nearest)

    return nearest, jarak # TUPLE, integer


def gameStateValue(board): 
    jarakRed = 0
    jarakGreen = 0
    for row in range(len(board)):
        for col in range(len(board)):
            thisSquare = board[row][col] # SQUARE
            if (thisSquare.piece == Square.P_RED): # assumption: computer == RED
                    near, jarak = findNearest(thisSquare, board)
                    jarakRed += jarak
            
            elif (thisSquare.piece == Square.P_GREEN): # assumption: computer == RED
                    near, jarak = findNearest(thisSquare, board)
                    jarakGreen += jarak
    
    totalJarak = jarakRed - jarakGreen # assumption: computer == RED
    return (totalJarak * (-1))
