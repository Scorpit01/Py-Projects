import random

hangman = {
    0: "   "
       "   "
       "   ",
    1: " o "
       "   "
       "   ",
    2: " o \n"
       " | "
       "   ",
    3: " o \n"
       "/| \n"
       "   ",
    4: " o \n"
       "/|\\"
       "   ",
    5: " o \n"
       "/|  \n"
       "|  ",
    6: " o \n"
       "/|\\"
       "\n| |"
}


def hang(guesses):
    print("#########")
    print(hangman[guesses])
    print("#########")


WordList = ["chocolates", "table", "chair", "pillow",
            "lock", "phone", "bag", "scale", "book", "programming", "cable",
            "bed", "laptop", "card", "jacket", "keyboard", "computer", "key"]


print(f"WELCOME TO HANGMAN! You will get 6 wrong guesses before its called a hangman!")
replay = True
while replay:
    wordington = random.choice(WordList)
    hint = ["_"] * len(wordington)
    guesses = 0
    chances = 6
    guessed_letters = set()
    guess = ""

    while guesses < chances and "_" in hint:
        print(" ".join(hint))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter only a single letter!")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter! Please try again!")
            continue

        guessed_letters.add(guess)

        if guess in wordington:
            for i in range(len(wordington)):
                if guess == wordington[i]:
                    hint[i] = guess
            print("correct!")
        else:
            guesses += 1
            print(hangman[guesses])
            print(f"You have {chances - guesses}chances left!")
            continue

    if "_" not in hint and guesses <= chances:
        print(f"Congrats you have won the game!! The word was {wordington}!!")
    else:
        print(f"Sorry! You've lost the game! The word was {wordington}!")

    choice = input("Do you want to play again?[Y/N]")
    if "Y" != choice.upper():
        print("Thank you for playing!")
        break

##HOLY SHIT THIS HAS GOT TO BE ONE OF THOSE PROJECTS THAT HAS TAUGHT ME THE MOST!!!