# ====================
# Lesson 9: Safeguarding Your Code - Python Exception Handling
# ====================

# ====================
# Engage & Apply: Write a program that prompts the user for two numbers, then divides the first by the second.
# Handle the exceptions where the user enters invalid data (non-numeric) or tries to divide by zero.
# ====================

try:
    # Step 2a/2b: Prompt user to input two numbers & convert inputs to integers or floats.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Step 2c: Perform the division
    result = num1 / num2
    print(f"The result is: {result}")

except ValueError:
    # Step 3a: Handle non-numeric input
    print("Invalid input! Please enter valid numbers.")

except ZeroDivisionError:
    # Step 3b: Handle division by zero
    print("Error! You can't divide by zero.")


# ====================
# Final Challenge: Create a program that simulates an ATM withdrawal process.
# ====================

account_balance = 1500  # Initial account balance

try:
    # Step 1: Allow user to input withdrawal amount
    withdrawal_amount = float(input("Enter the amount to withdraw: "))
    
    # Step 2: Raise exception if withdrawal amount is negative
    if withdrawal_amount < 0:
        raise ValueError("Withdrawal amount cannot be negative!")
    
    # Step 3: Ensure withdrawal doesn’t exceed the balance
    if withdrawal_amount > account_balance:
        raise ValueError("Insufficient funds!")
    
    # Proceed with withdrawal
    account_balance -= withdrawal_amount
    print(f"Withdrawal successful! Remaining balance: ${account_balance}")
    
except ValueError as e:
    # Handle invalid withdrawal input or exceeding funds
    print(f"Error: {e}")
    
finally:
    # Always display the remaining balance
    print(f"Your remaining balance is: ${account_balance}")


# ====================
# My Version of the Engage & Apply Challenge
# ====================

try:
    # Prompt user to input two numbers for division
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Perform the division
    result = num1 / num2
    print(f"The result is: {result}")

except ValueError:
    # Handle invalid input (non-numeric)
    print("Oops! You must enter valid numbers.")
    
except ZeroDivisionError:
    # Handle division by zero
    print("Oops! Can't divide by zero!")

    
# ====================
# My Version of the Final Challenge
# ====================

account_balance = 2000  # Starting with a higher balance

try:
    # User inputs withdrawal amount
    withdrawal_amount = float(input("Enter withdrawal amount: "))
    
    # Ensure withdrawal amount is positive
    if withdrawal_amount < 0:
        raise ValueError("Withdrawal amount must be positive.")
    
    # Ensure sufficient funds
    if withdrawal_amount > account_balance:
        raise ValueError("Not enough balance for this withdrawal.")
    
    # Update balance after successful withdrawal
    account_balance -= withdrawal_amount
    print(f"Successful withdrawal! Remaining balance: ${account_balance}")

except ValueError as e:
    # Display error messages for invalid input or insufficient balance
    print(f"Error: {e}")
    
finally:
    # Display remaining balance at the end
    print(f"Your final balance is: ${account_balance}")
