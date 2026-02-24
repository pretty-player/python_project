class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        """Base method to be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement abstract method")

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        print(f"💳 Processing Credit Card payment of ₹{self.amount}...")
        print(f"Verifying card ending in {self.card_number[-4:]}. Payment Successful!")

class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def pay(self):
        print(f"🅿️ Redirecting to PayPal for ₹{self.amount}...")
        print(f"Authenticated as {self.email}. Payment Successful!")

class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def pay(self):
        print(f"📲 Opening UPI app for ₹{self.amount}...")
        print(f"Request sent to {self.upi_id}. Transaction Successful!")

# --- Common Interface (Polymorphism in action) ---

def process_transaction(payment_method):
    """
    This function doesn't care if it's UPI, PayPal, or Credit Card.
    It just knows that any 'Payment' object has a .pay() method.
    """
    payment_method.pay()
    print("-" * 30)

# Testing the system with different inputs
cc = CreditCardPayment(4500, "1234-5678-9012-3456")
pp = PayPalPayment(1200, "customer@email.com")
upi = UPIPayment(500, "user@okaxis")

# Processing all through the same interface
payments = [cc, pp, upi]

print("--- 🛒 Checkout Processing ---")
for p in payments:
    process_transaction(p)