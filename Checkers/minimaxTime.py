import IN104_simulateur as simu
import time
from evaluation import evaluate
from minimax_time import minimax


class MinimaxTime:

    def __init__(self, config=None, rules=None):
        self.name = 'AI' # set your AI name here

    def play(self, gameState, timeLimit):
        possibleStates = gameState.findNextStates()
        value=float("-inf")
        dico_state={}
        next_state = gameState
        for state in possibleStates:
            new_value = minimax(state,timeLimit/(len(possibleStates)+1),False,simu.GameState.findNextStates,evaluate,dico_state)
            if new_value >= value:
                value = new_value
                next_state = state
        return next_state
    
    def __str__(self):
        return self.name