'''
Author:Nandana Hasheed
Date:3/12/2024
Write a program to play a sticks game in which there are 16 sticks. Two players take turns to play the game. Each player picks one set of sticks (needn’t be adjacent) during his turn. A set contains 1, 2, or 3 sticks. The player who takes the last stick is the loser. The number of sticks in the set is to be input.
'''
def stick_game():
    print("Rules")
total_sticks=int(input("Enter the number of sticks"))
name1=input("Enter the first players name")
name2=input("Enter the second players name")
while total_sticks >0:
    A=int(input(f"{name1},pick 1,2,or 3 sticks"))
    total_sticks-=A
    print("Sticks remaining",total_sticks)
    B=int(input(f"{name2},pick 1,2,or 3 sticks"))
    total_sticks-=B
    print("Sticks remaining: ",total_sticks)
    print(f"There are {total_sticks} sticks left")
    if total_sticks==0:
        print(name2,"wins",name1,"loses")
        break
    print(name2,"Your turn:")
    user1=int(input("Enter 1,2,3, sticks"))
    total_sticks=user1
    print("sticks remaining",total_sticks)
    if total_sticks==0:
        print(name1,"wins",name2,"loses")
        break
stick_game()






