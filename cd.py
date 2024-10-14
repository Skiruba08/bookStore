class CD:
    def __init__(self, name=None, price=0.0):
        """
        Initializes the CD object.

        :param name: The CD's name (default is None)
        :param price: The CD's price (default is 0.0)
        """
        self.name = name
        self.price = price

    def get_name(self):
        """
        Gets the name of the CD.

        :return: The name of the CD
        """
        return self.name

    def set_name(self, name):
        """
        Sets the name of the CD.

        :param name: The name to set for the CD
        """
        self.name = name

    def get_price(self):
        """
        Gets the price of the CD.

        :return: The price of the CD
        """
        return self.price

    def set_price(self, price):
        """
        Sets the price of the CD.

        :param price: The price to set for the CD
        """
        self.price = price
