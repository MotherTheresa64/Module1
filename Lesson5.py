# ====================
# Engage & Apply: Design a program that will help someone decide between two activities based on the weather and mood. (Pre-provided)
# ====================

# Taking user input for weather and mood
weather = input("Is the weather sunny or raining? ").lower()
mood = input("Are you feeling happy or tired? ").lower()

# Decision making based on weather and mood
if weather == "sunny" and mood == "happy":
    print("Go for a hike!")
elif weather == "raining" and mood == "tired":
    print("Relax indoors.")
else:
    print("It's a good day to stay in and rest!")


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Taking user input for weather and mood
weather = input("What's the weather like today? (sunny/rainy) ").lower()
mood = input("How are you feeling? (happy/tired) ").lower()

# Decision making based on weather and mood
if weather == "sunny" and mood == "happy":
    print("You should go for a walk in the park!")
elif weather == "rainy" and mood == "tired":
    print("Perfect time to stay home and relax with a book.")
else:
    print("Maybe go for a drive or watch a movie!")


# ====================
# Final Challenge: Write a program where the user has to guess a secret number between 1 and 10. (Pre-provided)
# ====================

import random

# Randomly select a secret number between 1 and 10
secret_number = random.randint(1, 10)

# Asking the user to guess the number
guess = int(input("Guess the secret number between 1 and 10: "))

# Giving feedback based on the user's guess
if guess == secret_number:
    print("Congratulations, You guessed the secret number!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Too high!")


# ====================
# My Version of the Final Challenge
# ====================

import random

# Randomly select a secret number between 1 and 20
secret_number = random.randint(1, 20)

# Asking the user to guess the number
guess = int(input("Guess the secret number between 1 and 20: "))

# Giving feedback based on the user's guess
if guess == secret_number:
    print("Congratulations, You guessed the secret number!")
elif guess < secret_number:
    print("Too low! Try again!")
else:
    print("Too high! Give it another shot!")
