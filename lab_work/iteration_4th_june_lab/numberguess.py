#program to guess number game
ecret = 25   # Fixed secret number

guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct Guess")

print("Total Attempts =", attempts) 