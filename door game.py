'''
Author:Nandana Hasheed
Date:3/12/2024
Write a program to play a sticks game in which there are 16 sticks. Two players take turns to play the game. Each player picks one set of sticks (needn’t be adjacent) during his turn. A set contains 1, 2, or 3 sticks. The player who takes the last stick is the loser. The number of sticks in the set is to be input.
'''
    from random import randint
    choice=int(input("open a door(1,2 or 3):"))
    a=randint( 1, 4)
    if a==choice:
        secondchoice=input("opens th door,revealing a car\nDo you want to switch your door(Y/N):")
        secondchoice.casefold()
        if secondchoice=='y':
            finalchoice=input("enter your final choice:")
            if finalchoice==a:
                print("congrats you won the car")
            else:
                print("congrats you won a goat")
        else:
            print("congrats you won a car")
    else:
        secondchoice=input("opens the door,revealing a goat\nDo you want to switch your door(Y/N):")
        if secondchoice=='y':
            finalchoice=input("enter your final choice:")
            if finalchoice==a:
                print("congrats you won a car")
            else:
                print("congrats you won a goat")
        else:
            print("congrats you won a GOAT")
monty()
