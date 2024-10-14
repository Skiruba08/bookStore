class DVD:
    def __init__(self, name="", price=0.0):
        """
        Constructor to initialize the DVD's name and price.
        Default constructor with no arguments.
        """
        self.name = name
        self.price = price

    def get_name(self):
        """
        This method gets the name of the DVD.
        :return: The name of the DVD.
        """
        return self.name

    def set_name(self, name):
        """
        This method sets the name of the DVD.
        :param name: The name of the DVD.
        """
        self.name = name

    def get_price(self):
        """
        This method gets the price of the DVD.
        :return: The price of the DVD.
        """
        return self.price

    def set_price(self, price):
        """
        This method sets the price of the DVD.
        :param price: The price of the DVD.
        """
        self.price = price
