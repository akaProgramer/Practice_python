#!/usr/bin/env python3

__author__ = "Jugal Kishore & Akash Shiva"
__version__ = "1.0"


import random
import os
hum_score=0
com_score=0
while True:
    print("///Rock Paper Scissor Game///")
    print("")
    print("1. for Rock")
    print("2. for Paper")
    print("3. for Scissor")
    print("4. to exit")
    print("")
    print("Enter your choice:")
    total = ["Rock", "Paper", "Scissor"]
    try:
        human_put = int(input()) - 1
    except ValueError:
        print("")
        print("Not an integer")
        break
    comp_put = random.randint(0, 2)
    if human_put == 0:
        choice = "Rock"
    elif human_put == 1:
        choice = "Paper"
    elif human_put == 2:
        choice = "Scissor"
    elif human_put == 3:
        print("Bye Bye")
        break
    else:
        print("")
        print("Available Choices are: 1, 2, 3, 4")
        print("")
        print("Press any key to continue...")
        input()
        os.system("cls")
        continue
    print("")
    print("Your Choice: ", choice)
    print("")
    print("Computer Choice: ", total[comp_put])
    print("")
    if human_put == comp_put:
        print("It's a Tie")
    elif (human_put==0 and comp_put==1) or (human_put==1 and comp_put==2) or (human_put==2 and comp_put==0):
        com_score+=1
        print("You Lost!")
    elif (comp_put==0 and human_put==1) or (comp_put==1 and human_put==2) or (comp_put==2 and human_put==0):
        hum_score+=1
        print("You Won!")
    print("")
    print("Press any key to continue...")
    input()
    os.system("cls")
if com_score<hum_score:
    print('Your Score=',hum_score,"Computer Score=",com_score)
    print("You won this game")
elif com_score==hum_score:
    print('Your Score=',hum_score,"Computer Score=",com_score)
    print("Game Tied kante ki takkar")
else:
    print('Your Score=',hum_score,"Computer Score=",com_score)
    print("You loose chullu bhar pani me doob ke marja")
print("\nCreated by Jugal Kishore & Akash Shiva -- 2020")