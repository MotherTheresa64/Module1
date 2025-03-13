# ====================
# Engage & Apply: Manipulate Python Lists, their characteristics, and operations. (Pre-provided)
# ====================

# Defining the list "fruits"
fruits = ["apple", "banana", "cherry", "date"]

# Printing the first item in the list
print(f"First item: {fruits[0]}")  # Output: apple

# Printing the last item using negative indexing
print(f"Last item: {fruits[-1]}")  # Output: date

# Adding "elderberry" to the end of the list
fruits.append("elderberry")
print(f"List after appending 'elderberry': {fruits}")

# Inserting "blueberry" at index 1
fruits.insert(1, "blueberry")
print(f"List after inserting 'blueberry' at index 1: {fruits}")

# Removing "banana" from the list
fruits.remove("banana")
print(f"List after removing 'banana': {fruits}")

# Deleting the first item from the list
del fruits[0]
print(f"List after deleting the first item: {fruits}")

# Slicing the list to create a subset called "citrus_fruits"
citrus_fruits = fruits[2:4]  # Index 2 to 3 (inclusive of 2, exclusive of 4)
print(f"Citrus fruits: {citrus_fruits}")


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Defining the list "fruits"
fruits = ["apple", "banana", "cherry", "date"]

# Printing the first item in the list
print(f"First fruit: {fruits[0]}")  # Output: apple

# Printing the last item using negative indexing
print(f"Last fruit: {fruits[-1]}")  # Output: date

# Adding "elderberry" to the end of the list
fruits.append("elderberry")
print(f"List after appending 'elderberry': {fruits}")

# Inserting "blueberry" at index 1
fruits.insert(1, "blueberry")
print(f"List after inserting 'blueberry' at index 1: {fruits}")

# Removing "banana" from the list
fruits.remove("banana")
print(f"List after removing 'banana': {fruits}")

# Deleting the first item from the list
del fruits[0]
print(f"List after deleting the first item: {fruits}")

# Slicing the list to create a subset called "citrus_fruits"
citrus_fruits = fruits[1:3]  # Index 1 to 2 (inclusive of 1, exclusive of 3)
print(f"Citrus fruits: {citrus_fruits}")


# ====================
# Final Challenge: Create a program that asks the user for their top 3 favorite books, stores them in a list, and prints the list in a sorted order. (Pre-provided)
# ====================

# Initialize an empty list to store favorite books
favorite_books = []

# Prompt the user for their top 3 favorite books
for i in range(3):
    book = input(f"Enter your favorite book #{i+1}: ")
    favorite_books.append(book)

# Sort the list alphabetically
favorite_books.sort()

# Print the sorted list of favorite books
print("Your top 3 favorite books in sorted order:")
for book in favorite_books:
    print(book)


# ====================
# My Version of the Final Challenge
# ====================

# Initialize an empty list to store favorite books
favorite_books = []

# Prompt the user for their top 3 favorite books
for i in range(3):
    book = input(f"Please enter your top {i+1} favorite book: ")
    favorite_books.append(book)

# Sort the list alphabetically
favorite_books.sort()

# Print the sorted list of favorite books
print("Here are your top 3 favorite books in alphabetical order:")
for book in favorite_books:
    print(book)
