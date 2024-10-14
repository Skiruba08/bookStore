class Book:
    def __init__(self, name=None, price=0.0):
        """
        Initializes the Book object.

        :param name: The book's name (default is None)
        :param price: The book's price (default is 0.0)
        """
        self.name = name
        self.price = price

    def get_name(self):
        """
        Gets the name of the book.

        :return: The name of the book
        """
        return self.name

    def set_name(self, name):
        """
        Sets the name of the book.

        :param name: The name to set for the book
        """
        self.name = name

    def get_price(self):
        """
        Gets the price of the book.

        :return: The price of the book
        """
        return self.price

    def set_price(self, price):
        """
        Sets the price of the book.

        :param price: The price to set for the book
        """
        self.price = price
