# 1.Number Guessing Game
#--------------------------

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Maximum number of attempts
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    # Check if the guess is out of range
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue


    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    # Give feedback
    if guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

    attempts -= 1

else:
    print("Better luck next time!")


# 2.Multiplication Table Generator
#---------------------------------

number = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)

# 3.BMI- Calculator - Function
#--------------------------------

def calculate_bmi(weight,height):
    bmi = weight/(height**2)
    return bmi

weight = float(input("Enter your weight in Kg:"))
height = float(input("Enter your height in meters:"))

bmi = calculate_bmi(weight,height)
print("Your BMI is:",format(bmi,".2f"))