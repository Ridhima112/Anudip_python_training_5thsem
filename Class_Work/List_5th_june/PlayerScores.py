#Player_score
player_score = []
#input of score from user
for i in range(11):
    score = int(input("enter the score of player ():"))
    player_score.append(score)
#display the score of player
print("\n------- player score ---------")
print("score of 11 player:", player_score)

#finding the highest score 
max_score = player_score[0]
for index in range(1,len(player_score)):
    if player_score[index] > max_score:
        max_score = player_score[index]
print("the highest score is:",max_score)        
