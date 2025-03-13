# ====================
# Engage & Apply: Create a program that takes your name, age, and favorite color as input and prints them out. (Pre-provided)
# ====================

# Taking user input for name, age, and favorite color
name = input("What is your name? ")
age = input("How old are you? ")
favorite_color = input("What is your favorite color? ")

# Printing out the inputs
print(name)
print(age)
print(favorite_color)


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Taking user input for their favorite animal, hometown, and favorite hobby
animal = input("What's your favorite animal? ")
hometown = input("Where are you from? ")
hobby = input("What’s your favorite hobby? ")

# Display the user's inputs with additional context
print(f"Favorite Animal: {animal}")
print(f"Hometown: {hometown}")
print(f"Favorite Hobby: {hobby}")
 

# ====================
# Final Challenge: Build a program that asks the user to input their exam score and then prints a message. (Pre-provided)
# ====================

# Taking user input for exam score
score = int(input("Enter your exam score: "))

# Conditional statements to print messages based on score
if score > 90:
    print("Excellent")
elif score >= 70 and score <= 90:
    print("Good")
else:
    print("Needs Improvement")


# ====================
# My Version of the Final Challenge
# ====================

# Asking for the user's age and suggesting an activity based on their age
age = int(input("How old are you? "))

# Suggesting an activity based on the user's age
if age < 13:
    print("You should try playing video games or drawing!")
elif 13 <= age <= 18:
    print("How about joining a sports team or learning a musical instrument?")
else:
    print("Maybe consider learning a new skill or starting a hobby!")
