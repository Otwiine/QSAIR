

class BankAccount:

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder              # Public
        self._account_number = self._generate_account_number()  # Protected
        self.__balance = initial_balance                  # Private

    def deposit(self, amount):
        if self._validate_amount(amount):
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if self._validate_amount(amount) and amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        # Public interface to access private data
        return self.__balance

    def _validate_amount(self, amount):
        # Protected helper method
        return isinstance(amount, (int, float)) and amount > 0

    def _generate_account_number(self):
        import random
        return random.randint(100000, 999999)
