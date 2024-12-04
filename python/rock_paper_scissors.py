# -*- coding: utf-8 -*-
import random

print('===================\nRock Paper Scissors\n===================')
print('1) ✊\n2) ✋\n3) ✌️')
player = int(input("Pick a number: "))
computer = random.randint(1, 3)
print()
if player == 1:
        print('You chose: ✊')
if player == 2:
        print('You chose: ✋')
if player == 3:
        print('You chose: ✌️')

if computer == 1:
        print('CPU chose: ✊')
if computer == 2:
        print('CPU chose: ✋')
if computer == 3:
        print('CPU chose: ✌️')

if (player == computer):
    print("Egality, try again")
if (player == 1 and computer == 2):
    print("The CPU won!")
if (player == 2 and computer == 3):
    print("The CPU won!")
if (player == 3 and computer == 1):
    print("The CPU won!")
if (player == 1 and computer == 3):
    print("The player won!")
if (player == 2 and computer == 1):
    print("The player won!")
if (player == 3 and computer == 2):
    print("The player won!")