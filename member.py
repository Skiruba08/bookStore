class Member:
    def __init__(self, name="", spent=0.0):
        """
        Initializes a new member with a name and the amount spent.
        """
        self.name = name
        self.spent = spent

    # Getter for name
    def get_name(self):
        return self.name

    # Setter for name
    def set_name(self, name):
        self.name = name

    # Getter for spent
    def get_spent(self):
        return self.spent

    # Setter for spent
    def set_spent(self, amount):
        self.spent += amount
