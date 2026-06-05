#input score of 11 player and then display there score in python
player_score = [] #sequentil data structure ised ony to store data or heterogenous elemets (mutuable delete and modification)
#lsit dtor like referncd dting(hekko) in backgrund internal working
#input of score from user
#program takes 11 player data display the score of the player with highest score

player_score = []
for i in range(11):
    score = int(input(f"Enter the score of player {i+1}: "))
    while score < 0:
        print("Score cannot be negative. Please enter a valid score.")
        score = int(input(f"Enter the score of player {i+1}: "))
    player_score.append(score)

highest_score = player_score[0]
for index in range(1, len(player_score)):
    if player_score[index] > highest_score:
        highest_score = player_score[index]

print("The highest score is:", highest_score)