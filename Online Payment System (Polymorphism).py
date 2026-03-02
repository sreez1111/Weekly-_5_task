class Payment:
    def pay(self, amount):
        print("Processing payment of", amount)


class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class WalletPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Wallet")


# Creating objects
p1 = CreditCardPayment()
p2 = UPIPayment()
p3 = WalletPayment()

# Polymorphism in action
payments = [p1, p2, p3]

for payment in payments:
    payment.pay(1000)