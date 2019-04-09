import sys
import time
import random as rd

class RandomBrain:

    def __init__(self):
        print("Please enter your name")
        self.name = sys.stdin.readline()[0:-1]
        self.alwaysSeeAsWhite = False
    
    def play(self,gameState,timeLimit):
        possibleMoves = gameState.findPossibleMoves()
        print(gameState.toDisplay(True))
        i=rd.randint(0,len(possibleMoves)-1)
        move = possibleMoves[i]
        choice = gameState.doMove(move, inplace = False)

        return(choice)
    
