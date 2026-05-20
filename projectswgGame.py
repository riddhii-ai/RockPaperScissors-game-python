'''
Project 1 snake water gun game
rock -1
paper 0
scissor 1
'''
import random
computer = random.choice([-1, 0, 1])

print("Enter s for scissors, r for rock and p for paper")

player = input("Enter : ")
pdict = {"r" : -1, "p" : 0, "s" : 1}
rdict = {-1: "Rock", 0: "Paper", 1: "Scissors"}
pnum = pdict[player]

print("You chose :", rdict[pnum])
print("Computer chose :", rdict[computer])


diff = pnum - computer
if(diff == 0):
    print("Tie")
elif(diff == 1):
    print("player wins")
elif(diff == -1):
    print("computer wins")
elif(diff == -2):
    print("player wins")
elif(diff == 2):
    print("computer wins")
else:
    print("Something went  wrong")