import random

print("***Welcome to the Number Guessing Game!***")
print("I'm thinking of a number between 1 and 100. Can you guess it?")
num = random.randint(1,100)
att = 0
while True:
    play = int(input("Enter your guess: "))
    if play > num:
        print("Too high! Try again.")
        att += 1
    elif play < num:
        print("Too low! Try again.")
        att += 1
    elif play == num:
        print(f"Congratulations! You guessed the number in {att + 1} attempts.")
        break
