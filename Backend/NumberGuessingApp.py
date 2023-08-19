from random import randint


number = randint(0, 20)
guess = int(input("The number is between 0 and 20, Guess it : "))
while guess != number:
    if guess >= 0 and guess <= 20:
        if guess > number:
            guess = int(input("Too high, try another one : "))
        elif guess < number:
            guess = int(input("Too low, try another one : "))
    else:
        guess = int(input("Enter number between 0 and 20 : "))
print(f"Excellent, You guessed correctly. The number was {number}")