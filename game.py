import random

with open("./words.txt") as wordfile:
    words = wordfile.read().split()



def isWordValid(choice):
    while ("-" in choice or " " in choice):
        choice = random.choice(words)


def splitWord(word):
    list = [c for c in word]
    return list


def game():
    numberTries = 6;
    choice = random.choice(words)
    isWordValid(choice)
    for i in range(numberTries):
        user = input("Guess a letter: ")
        if (user == choice):
            print("you win")
            return
        else:
            print(f"wrong guess you have {numberTries - 1 - i} left ")
game()