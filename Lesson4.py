# ====================
# Engage & Apply: Calculate the total cost of the following items. Then, apply a 10% discount and display the final amount. (Pre-provided)
# ====================

# Define the costs of the items
milk = 5
eggs = 3
coffee = 10

# Calculate the total cost of the items
total_cost = milk + eggs + coffee

# Calculate the discount (10% of the total cost)
discount = total_cost * 0.10

# Calculate the final amount after the discount
final_amount = total_cost - discount

# Print the results
print(f"The Total Cost: ${total_cost}")
print(f"Final Amount after 10% discount: ${final_amount}")


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# Define the costs of some other items
book = 12
pen = 2
notebook = 5

# Calculate the total cost of these items
total_cost = book + pen + notebook

# Apply a 15% discount to the total
discount = total_cost * 0.15

# Calculate the final amount after the discount
final_amount = total_cost - discount

# Print the results
print(f"The Total Cost: ${total_cost}")
print(f"Final Amount after 15% discount: ${final_amount}")


# ====================
# Final Challenge: Design a simple calculator that performs operations on two integers provided by the user. (Pre-provided)
# ====================

# Taking user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined"  # Handle division by zero

# Display the results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")


# ====================
# My Version of the Final Challenge
# ====================

# Taking user input for two numbers
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined"  # Handle division by zero
modulus = num1 % num2 if num2 != 0 else "undefined"  # Modulus operation

# Display the results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")
