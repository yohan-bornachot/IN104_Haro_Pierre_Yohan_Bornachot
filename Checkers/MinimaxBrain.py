import IN104_simulateur as simu
from evaluation import evaluate
from minimax import minimax
simu.GameState.get_children = simu.GameState.findNextStates
simu.GameState.evaluate = evaluate

class MinimaxBrain:

    def __init__(self, config=None, rules=None):
        self.name = 'AI' # set your AI name here
        self.depth = 8 # Set the exploration depth here
    
    def play(self, gameState, timeLimit):
        possibleStates = gameState.findNextStates()
        #print(gameState.toDisplay(True))
        value=float("-inf")
        dico_state={}
        next_state = gameState
        for state in possibleStates:
            new_value = minimax(state,self.depth,True,dico_state)
            if new_value >= value:
                value = new_value
                next_state = state
        return next_state
    
    def __str__(self):
        return self.name