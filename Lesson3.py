# ====================
# Engage & Apply: Create a string with a sentence of your choice.
# Use string methods to:
# - Convert it to uppercase.
# - Remove any leading or trailing whitespace.
# - Replace a word with another word of your choice.
# - Split it into a list of words.
# ====================

# Create a sentence string
my_string = '            Coding temple is the best bootcamp ever!      '

# Apply string methods
uppercase_string = my_string.upper()  # Convert to uppercase
stripped_string = my_string.strip()  # Remove leading and trailing whitespace
replaced_string = my_string.replace("best", "greatest")  # Replace word
split_string = my_string.split()  # Split the string into a list of words

# Print the results
print(uppercase_string)  # Output: 'CODING TEMPLE IS THE BEST BOOTCAMP EVER!'
print(stripped_string)  # Output: 'Coding temple is the best bootcamp ever!'
print(replaced_string)  # Output: 'Coding temple is the greatest bootcamp ever!'
print(split_string)  # Output: ['Coding', 'temple', 'is', 'the', 'best', 'bootcamp', 'ever!']


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Create a sentence string
my_sentence = "   Python programming is super fun and engaging!    "

# Apply string methods
upper_sentence = my_sentence.upper()  # Convert to uppercase
trimmed_sentence = my_sentence.strip()  # Remove any leading or trailing spaces
replaced_sentence = my_sentence.replace("fun", "amazing")  # Replace word
split_sentence = my_sentence.split()  # Split into words

# Print the results
print(upper_sentence)  # Output: 'PYTHON PROGRAMMING IS SUPER FUN AND ENGAGING!'
print(trimmed_sentence)  # Output: 'Python programming is super fun and engaging!'
print(replaced_sentence)  # Output: 'Python programming is super amazing and engaging!'
print(split_sentence)  # Output: ['Python', 'programming', 'is', 'super', 'fun', 'and', 'engaging!']


# ====================
# Final Challenge: Build a text-based name generator that combines random first and last names using string manipulation. (Pre-provided)
# ====================

import random

# Two lists of first and last names
first_names = ["Christian", "Dylan", "Travis", "Katelyn"]
last_names = ["Sachs", "Katina", "Peck", "Mehner"]

# Generate a random first and last name
random_first = random.choice(first_names)
random_last = random.choice(last_names)

# Combine them to create a full name
full_name = random_first + " " + random_last

# Print the generated name
print(f"Generated Name: {full_name}")


# ====================
# My Version of the Final Challenge
# ====================

import random

# Two lists of fun adjectives and animals
adjectives = ["Brave", "Clever", "Quick", "Majestic"]
animals = ["Lion", "Tiger", "Eagle", "Wolf"]

# Generate a random adjective and animal
random_adjective = random.choice(adjectives)
random_animal = random.choice(animals)

# Combine them to create a fun nickname
nickname = random_adjective + " " + random_animal

# Print the generated nickname
print(f"Generated Nickname: {nickname}")
