import random

#tried using the english-words python library, but it had some important features missing and the library is huge :(
#so with the missing features it would make the game impossible so, I just stuck with establishing a list myself :)
#As this is open source, feel free to add more according to your liking :)

words = ["chocolates", "table", "chair", "pillow",
         "bed", "laptop", "card", "jacket", "keyboard", "computer", "key",
         "lock", "phone", "bag", "scale", "book","programming", "cable"]
name = input("What is your name?: ")
print(f"WELCOME {name.upper()}! This is a Word Guessing Game\nBefore starting I would recommend taking a brief look at the words used in the game if you wish to")

while True:
    TheChosenOne = random.choice(words)
    tries = 9
    guesses = 0
    lookup = input("Do you want to lookup the words?[Y/N]: ").strip().upper()

    if lookup == "Y":
        for i in words:
            print(i)
    else:
        print("Alright! Lets proceed with the game:)")

    print("You will be getting 9 tries to guess the correct word!")
    print(f"The word chosen is a {len(TheChosenOne)} letter long word. Think wisely!")
    word = input(f"Enter your first guess! You have {tries} tries! : ")

    while TheChosenOne != word:
        guesses += 1
        if TheChosenOne != word and tries > guesses:
             print(f"OOPS! This is not the correct word! You have {tries - guesses} tr(y/ies) left!")
             word = input("Enter a different word: ")
        elif TheChosenOne != word and tries == guesses:
            print(f"OH NO!\nYou have unfortunately lost the game by running out of tr(y/ies) :(\nThe word was {TheChosenOne}")
            break

    if TheChosenOne == word and tries >= guesses:
        print(f"CONGRATS! You got the word right in {guesses+1} tr(y/ies)")

    replay = input("Do you want to play again?[Y/N]: ").strip().upper()
    if replay != "Y":
        print("Thank you for playing the game:)")
        break
