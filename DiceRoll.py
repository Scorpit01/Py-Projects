import random

rolly = True
while rolly:
    print("You rolled the dice and got: ", random.randint(1, 6))
    print("Do you want to roll the dice again?[Y/N]")
    rolly = "Y" in input().upper()