class PremiumMember:
    def __init__(self, name="", premium_price=0.0, payment_type=""):
        """
        Initializes a new premium member with a name, premium price, and payment type.
        """
        self.name = name
        self.premium_price = premium_price
        self.payment_type = payment_type
        self.spent = 0.0

    # Getter for name
    def get_name(self):
        return self.name

    # Setter for name
    def set_name(self, name):
        self.name = name

    # Getter for premium price
    def get_premium_price(self):
        return self.premium_price

    # Setter for premium price
    def set_premium_price(self, price):
        self.premium_price += price

    # Getter for payment type
    def get_payment_type(self):
        return self.payment_type

    # Setter for payment type
    def set_payment_type(self, payment_type):
        self.payment_type = payment_type

    # Getter for spent
    def get_spent(self):
        return self.spent

    # Setter for spent
    def set_spent(self, amount):
        self.spent += amount

    # toString equivalent in Python (__str__)
    def __str__(self):
        return f"{self.name} paid {self.premium_price}, and is now a premium member :)"
