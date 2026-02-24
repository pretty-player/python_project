class BankAccount:
    def __init__(self, name, account_number, initial_balance=0.0):
        # Private attributes (Encapsulation)
        self.__name = name
        self.__account_number = account_number
        self.__balance = initial_balance

    # Getter method for Account Holder Name
    def get_account_holder(self):
        return self.__name

    # Getter method for Balance (Read-only access)
    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        """Validates and adds money to the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited ${amount:.2f}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        """Validates balance and subtracts money from the account."""
        if amount > self.__balance:
            print("Error: Insufficient funds.")
        elif amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Successfully withdrew ${amount:.2f}")

# --- Testing the Encapsulation ---

my_account = BankAccount("Sarah Jenkins", "123456789", 500.0)

# Accessing data through methods (The right way)
print(f"Account Holder: {my_account.get_account_holder()}")
print(f"Starting Balance: ${my_account.check_balance()}")

# Attempting transactions
my_account.deposit(150.0)
my_account.withdraw(100.0)
my_account.withdraw(1000.0) # Should trigger insufficient funds

# Accessing data directly (The wrong way - will trigger an AttributeError)
try:
    print(my_account.__balance)
except AttributeError:
    print("\nAccess Denied: You cannot access '__balance' directly due to encapsulation.")