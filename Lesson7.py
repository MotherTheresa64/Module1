# ====================
# Engage & Apply: Write a Python program that prints all the even numbers between 1 and 20 using a while loop. (Pre-provided)
# ====================

# Initialize the variable
number = 1

# Set up the while loop
while number <= 20:
    # Check if the number is even
    if number % 2 == 0:
        print(number)
    # Increment the number
    number += 1


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Initialize the variable
number = 1

# Set up the while loop
while number <= 20:
    # Check if the number is even
    if number % 2 == 0:
        print(f"Even number: {number}")
    # Increment the number
    number += 1


# ====================
# Final Challenge: Write a Python program that processes a range of numbers from 1 to 30. The program should do the following: (Pre-provided)
# ====================

# Process the range of numbers from 1 to 30
for i in range(1, 31):
    # Skip numbers divisible by 3 using continue
    if i % 3 == 0:
        continue
    # Stop the loop if the number is greater than 25 using break
    if i > 25:
        break
    print(i)


# ====================
# My Version of the Final Challenge
# ====================

# Process the range of numbers from 1 to 30
for i in range(1, 31):
    # Skip numbers divisible by 3 using continue
    if i % 3 == 0:
        continue
    # Stop the loop if the number is greater than 25 using break
    if i > 25:
        break
    print(f"Processed number: {i}")
