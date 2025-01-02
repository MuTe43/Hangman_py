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
        attempt = "_    "*len(choice)
        print(attempt)
        user = input("Guess a letter: ")
        # guessedLetter = [i if i in a and i in user else "_" for i in a ]
        guessedLetter = [i if i in enumerate(a) and i in enumerate(user) else "_" for i in enumerate(user) ]
        if (user == choice):
            print("you win")
            return
        elif (len(guessedLetter)>=1):
            print(f"you guessed some letters {guessedLetter}")

        else:
            print(f"wrong guess you have {numberTries - 1 - i} left ")
game()