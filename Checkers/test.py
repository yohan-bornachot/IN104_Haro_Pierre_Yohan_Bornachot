import IN104_simulateur as simu
brain1 = simu.ManualBrain()
brain2 = simu.ManualBrain()
timeLimit = 60 # each player will have 60 seconds to play
game = simu.Game(brain1, timeLimit, brain2, timeLimit)
game.runGame()
print(game.pdn) # display the game summary