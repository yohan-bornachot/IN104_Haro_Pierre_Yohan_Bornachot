import IN104_simulateur as simu
from evaluation_improving import evaluate
from minimax_alphabeta import minimax


class MinimaxBrain:

    def __init__(self, config=None, rules=None):
        self.name = 'AI' # set your AI name here
        self.depth = 6 # Set the exploration depth here

    def play(self, gameState, timeLimit):
        possibleStates = gameState.findNextStates()
        #print(gameState.toDisplay(True))
        value=float("-inf")
        dico_state={}
        next_state = gameState
        for state in possibleStates:
            new_value = minimax(state, self.depth, False, simu.GameState.findNextStates, evaluate, dico_state)
            if new_value >= value:
                value = new_value
                next_state = state
        return next_state
    
    def __str__(self):
        return self.name