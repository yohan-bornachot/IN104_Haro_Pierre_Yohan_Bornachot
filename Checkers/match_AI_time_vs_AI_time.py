import IN104_simulateur as simu
from minimaxTime import MinimaxTime
from minimaxTime_bis import MinimaxTimeBis
rules={}
rules['menCaptureBackward']=False
rules['kingsCanFly']=True
rules['menMustStop']=False
rules['noCaptureMax']=16

brain1 = MinimaxTime() #White
brain2 = MinimaxTimeBis() #Black
player_time = 30 #the player will have 30s to play
ai_time = 0.5 #the AI will have 10 sec to play
game = simu.Game(brain1, ai_time, brain2, ai_time, rules=rules)
game.displayLevel = 1   # this prints the board after each move
game.runGame()
print(game.pdn) #print the summary of the game. 

result=open("score.txt","a")
result.write(game.pdn)
result.close()