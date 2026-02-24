import os

# Custom Exception for Banking Logic
class InsufficientBalanceError(Exception):
    """Raised when a user attempts to withdraw more than their balance."""
    pass

class BankSystem:
    def __init__(self, filename="accounts.txt"):
        self.filename = filename
        # Ensure the file exists
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("0") # Initial balance if new file

    def get_balance(self):
        try:
            with open(self.filename, "r") as f:
                return float(f.read())
        except FileNotFoundError:
            print("Error: Account file missing.")
            return 0.0
        except ValueError:
            print("Error: Corrupted data in account file.")
            return 0.0

    def update_balance(self, amount):
        try:
            with open(self.filename, "w") as f:
                f.write(str(amount))
        except IOError as e:
            print(f"File Safety Error: Could not save data. {e}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("Deposit must be positive.")
            
            current = self.get_balance()
            new_balance = current + amount
            self.update_balance(new_balance)
            print(f"Successfully deposited ${amount:.2f}. New Balance: ${new_balance:.2f}")
        except ValueError as ve:
            print(f"Invalid Input: {ve}")
        finally:
            print("Deposit transaction attempt complete.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            current = self.get_balance()
            
            if amount > current:
                raise InsufficientBalanceError(f"Shortfall of ${amount - current:.2f}")
            if amount <= 0:
                raise ValueError("Withdrawal must be positive.")

            new_balance = current - amount
            self.update_balance(new_balance)
            print(f"Successfully withdrew ${amount:.2f}. New Balance: ${new_balance:.2f}")
            
        except InsufficientBalanceError as ibe:
            print(f"Transaction Denied: {ibe}")
        except ValueError as ve:
            print(f"Invalid Input: {ve}")
        finally:
            print("Withdrawal transaction attempt complete.")

def main():
    bank = BankSystem()
    
    while True:
        print("\n--- 🏦 Secure Bank Menu ---")
        print("1. Create/Reset Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        try:
            if choice == '1':
                bank.update_balance(0.0)
                print("Account created/reset to $0.00")
            elif choice == '2':
                bank.deposit()
            elif choice == '3':
                bank.withdraw()
            elif choice == '4':
                print(f"Current Balance: ${bank.get_balance():.2f}")
            elif choice == '5':
                print("Thank you for using our banking system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-5.")
        except Exception as e:
            print(f"A critical system error occurred: {e}")

if __name__ == "__main__":
    main()