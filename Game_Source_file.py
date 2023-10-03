# This is Snake Water Gun game

import random

#  This is for check condition win and lose
def gamewin(com,you):
    if com == you:
        return None
    elif com == "s" :
        if you == "w" or you== "W":
            return False
        elif you == "g" or you=="G":
            return True
    elif com == "w":
        if you == "g" or you== "G":
            return False
        elif you == "s" or you== "S":
            return True
    elif com == "g" :
        if you == "s" or you== "S":
            return False
        elif you == "w" or you== "W":
            return True
score=0
play_time=0
# This is for automatic run 
while True:
    print("It's for computer turn (s=snake, w=water, g=gun): ")
    # This is take random number by computer and compare by there strings
    r=random.randint(1, 3)
    if r == 1:
        com = "s" 
    elif r == 2:
        com = "w" 
    elif r == 3:
        com = "g" 
    
# This is your turn for take input
    l = ["s","w","g", "S", "W", "G"]
    you= input("It's your turn (s=snake, w=water, g=gun): ")

    if you == "q" or you == "Q":
        print(f"your score : {score} & total playtime : {play_time}")
        break
    elif you not in l:
        print("chose right key for play")
        continue
   
    a=gamewin(com, you)
    print(f"chosen by coumpetr : {com}")
    print(f"chosen by you  : {you}")

    # score=0

    if a== None:
        score=score+1
        play_time=play_time+1
        print("match tie")
    elif a:
        score=score+2
        play_time=play_time+1
        print("you win")
    else:
        score=score+0
        play_time=play_time+1
        print("you lose")

    
    