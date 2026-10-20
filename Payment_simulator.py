# Day 11 - Payment Gateway Simulator

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")

class MpesaPayment(Payment):
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return f"M-PESA:  STK push sent for KES {amount:,.2f}"

class CardPayment(Payment):
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return f"CARD:    Charged KES {amount:,.2f} to card ending in 1234"

class PayPalPayment(Payment):
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return f"PAYPAL:  Redirecting to PayPal for KES {amount:,.2f}"

class BankTransferPayment(Payment):
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return f"BANK:    Bank transfer initiated for KES {amount:,.2f}"

# Duck typing + stable calling code
def process_payments(payments, amount):
    for payment in payments:
        print(payment.pay(amount))

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"KES {self.amount:,.2f}"

# --- Test it like the Expected Output ---
if __name__ == "__main__":
    amount = 2500

    payments = [
        MpesaPayment(),
        CardPayment(),
        PayPalPayment(),
        BankTransferPayment()
    ]

    print("=== Coding Time Checkout ===")
    process_payments(payments, amount)

    # Grand total using Money class
    total = Money(0)
    for _ in payments:
        total = total + Money(amount)
    
    print(f"\nGrand Total: {total}")