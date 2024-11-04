import random

while True:
    print("WELCOME! This is a random number guessing game where you choose the range.\nYou will be getting 10 chances in this game!\nBest of Luck!")
    chances = 10
    a = int(input("Enter the range for the number you want to guess: "))
    n = random.randrange(a)
    guess = int(input("Guess your first number: "))
    guess_count = 0

    while guess != n:
        guess_count += 1
        if guess < n:
            guess = int(input("Too Low! Try Again!: "))
        elif guess > n:
            guess = int(input("Too High! Try Again!: "))

    if guess == n:
        print(f'CONGRATS! You won in {guess_count + 1} guesses:)')
    else:
        print('Sorry, You ran out of guesses! The number was', n, "\nBetter luck next time:) ")

    play_again = (input("Do you want to play again? (Y/N): ").strip().upper())

    if play_again != "Y":
        print("Thank you for playing! Goodbye!")
        break