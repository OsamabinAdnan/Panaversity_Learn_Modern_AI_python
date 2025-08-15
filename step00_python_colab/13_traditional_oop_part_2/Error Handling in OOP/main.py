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