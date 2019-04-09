import IN104_simulateur as simu
from MinimaxBrain import MinimaxBrain

brain1 = simu.ManualBrain()
brain2 = MinimaxBrain()
player_time = 50 #the player will have 30s to play
ai_time = 10 #the AI will have 10 sec to play
game = simu.Game(brain1, player_time, brain2, ai_time)
game.displayLevel = 1   # this prints the board after each move
game.runGame()
print(game.pdn) #print the summary of the game. 

result=open("score.txt","a")
result.write(game.pdn)
result.close()