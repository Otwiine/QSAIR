# Instance methods operate on individual objects and can access and modify the object's attributes. The `self` parameter refers to the specific instance calling the method.

class BankAccount:

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds"
        else:
            return "Withdrawal amount must be positive"

    def get_balance(self):
        return f"Account balance: ${self.balance}"

    def get_transaction_history(self):
        return self.transaction_history


# Using the BankAccount class
account = BankAccount("Alice Johnson", 1000)

print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
print(account.get_transaction_history())

# Always validate input in your methods 
# to ensure data integrity and provide meaningful error messages.