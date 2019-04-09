import IN104_simulateur as simu
from evaluation import evaluate
from minimax import minimax
simu.GameState.get_children = simu.GameState.findNextStates
simu.GameState.evaluate = evaluate

class MinimaxBrain:

    def __init__(self, config=None, rules=None):
        self.name = ‘AI1’ # set your AI name here
        self.depth = 5 # Set the exploration depth here
    
    def play(self, gameState, timeLimit):
        possibleStates = gameState.findNextStates()
        print(gameState.toDisplay(True))
        value=float("-inf")
        next_state = gameState
        for state in possibleStates:
            new_value = minimax(state,self.depth,True)
            if new_value >= value:
                value = new_value
                next_state = state
        return next_state
    
    def __str__(self):
        return self.name