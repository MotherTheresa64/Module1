# ====================
# Engage & Apply: Create a function introduce_yourself that takes a name and favorite hobby. The function should print a greeting and mention the person's hobby.
# ====================

# Define the function
def introduce_yourself(name, hobby):
    print(f"Hello, {name}! Correct me if I'm wrong, but your favorite hobby is {hobby}!")

# Call the function with test cases
introduce_yourself("Christian", "coding")  # Output: Hello, Christian! Correct me if I'm wrong, but your favorite hobby is coding!
introduce_yourself("Travis", "photography")  # Output: Hello, Travis! Correct me if I'm wrong, but your favorite hobby is photography!


# ====================
# Final Challenge: Create a function that takes a list of numbers as an argument, squares each number, and returns a new list with the squared values.
# ====================

# Define the function
def square_numbers(numbers):
    squared_numbers = []  # Empty list to store squared values
    for number in numbers:
        squared_numbers.append(number ** 2)  # Square each number and add to the list
    return squared_numbers

# Test the function with a sample list of numbers
list_of_numbers = [3, 99, 12, 1, 7]
squared_list = square_numbers(list_of_numbers)

# Print the result
print(squared_list)  # Output: [9, 9801, 144, 1, 49]


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Define the function
def introduce_yourself(name, hobby):
    print(f"Hi, {name}! I believe your favorite hobby is {hobby}. Let me know if that's true!")

# Call the function with test cases
introduce_yourself("Alice", "painting")  # Output: Hi, Alice! I believe your favorite hobby is painting. Let me know if that's true!
introduce_yourself("Bob", "gaming")  # Output: Hi, Bob! I believe your favorite hobby is gaming. Let me know if that's true!


# ====================
# My Version of the Final Challenge
# ====================

# Define the function
def square_numbers(numbers):
    squared_numbers = []  # Empty list to store squared values
    for number in numbers:
        squared_numbers.append(number ** 2)  # Square each number and add to the list
    return squared_numbers

# Test the function with a sample list of numbers
list_of_numbers = [5, 15, 8, 11, 9]
squared_list = square_numbers(list_of_numbers)

# Print the result
print(f"Squared numbers: {squared_list}")  # Output: Squared numbers: [25, 225, 64, 121, 81]
