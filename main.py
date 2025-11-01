import random
# Pick a random number between 1 and 100
number = random.randint(1, 100)
print("I have picked a number between 1 and 100. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))
    # Check if input is within range
    if guess < 1 or guess > 100:
        print("Number out of range! Please enter a number between 1 and 100.")
        continue
    # Give hints
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number} correctly!")
        break