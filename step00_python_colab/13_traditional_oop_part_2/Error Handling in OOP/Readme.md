# **Error Handling in OOP**

Error handling is a critical aspect of writing robust and reliable code. In Object-Oriented Programming (OOP), you can handle errors by raising exceptions in methods and creating custom exceptions to represent specific error conditions in your application.

## **Raising Exceptions in Methods**
In Python, you can raise exceptions using the raise keyword. This is useful for signaling that an error has occurred in a method.

## **Custom Exceptions in Classes**
Custom exceptions are user-defined exceptions that inherit from Python’s built-in Exception class. They allow you to define specific error types for your application.

## **Example: Handling Errors in OOP**
Let’s create a BankAccount class to demonstrate error handling in OOP. We’ll raise exceptions for invalid operations and define a custom exception for insufficient funds.

### **Code Example**
```python
# Custom exception for insufficient funds
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient funds: balance is {balance}, but {amount} was requested.")
        self.balance = balance
        self.amount = amount

# BankAccount class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    # Method to display account details
    def display(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")

# Create a BankAccount instance
account = BankAccount("Alice", 1000)

# Deposit money
try:
    account.deposit(500)  # Output: Deposited 500. New balance: 1500
except ValueError as e:
    print(e)

# Withdraw money
try:
    account.withdraw(2000)  # Raises InsufficientFundsError
except InsufficientFundsError as e:
    print(e)  # Output: Insufficient funds: balance is 1500, but 2000 was requested.
except ValueError as e:
    print(e)

# Display account details
account.display()  # Output: Account Holder: Alice, Balance: 1500
```
```bash
Deposited 500. New balance: 1500
Insufficient funds: balance is 1500, but 2000 was requested.
Account Holder: Alice, Balance: 1500
```

## **Explanation of the Code**

1. **Custom Exception (InsufficientFundsError):**

    * Inherits from Python’s Exception class.

    * Includes a custom error message that displays the account balance and the requested withdrawal amount.

2. **BankAccount Class:**

    * deposit method: Raises a ValueError if the deposit amount is not positive.

    * withdraw method: Raises a ValueError if the withdrawal amount is not positive and raises InsufficientFundsError if the balance is insufficient.

    * display method: Prints the account holder’s name and balance.

3. **Error Handling:**

    * The try and except blocks are used to catch and handle exceptions raised by the deposit and withdraw methods.

## **Key Takeaways**

* `Raising exceptions` is a way to signal errors in methods.
* `Custom exceptions` allow you to define specific error types for your application.
* Use try and except blocks to handle exceptions gracefully.
* Error handling in OOP ensures that your program can recover from unexpected situations and provide meaningful feedback to users.

This example demonstrates how to handle errors in Python OOP effectively. 🚀