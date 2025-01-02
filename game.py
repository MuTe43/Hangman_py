import random

with open("./words.txt") as wordfile:
    words = wordfile.readlines()
    #Removes the newline "\n" from the list AND makes sure the words are valid (no hyphen or spaces allowed)
    words=[words.rsplit("\n")[0] for words in words if (("-" not in words)and(" " not in words))]

print(words)

def splitWord(word):
    list = [c for c in word]
    return list


def game():
    numberTries = 6;
    choice = random.choice(words)
    a=splitWord(choice)
    print(a)
    for i in range(numberTries):
        user = input("Guess a letter: ")
        if (user == choice):
            print("you win")
            return
        else:
            print(f"wrong guess you have {numberTries - 1 - i} left ")
game()