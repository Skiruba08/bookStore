import sys

class Main:
    def __init__(self):
        self.bookStore = BookStore()

    def menu(self):
        choice = 0
        while 0 <= choice <= 5:
            print("WELCOME TO THE BOOKSTORE!!!")
            print("\t 1. Make a purchase")
            print("\t 2. Register a new premium member")
            print("\t 3. Add a product")
            print("\t 4. Remove a product")
            print("\t 5. Exit")

            try:
                num = int(input("Enter your choice: "))
                if num == 1:
                    self.purchase()
                elif num == 2:
                    self.register_premium_member()
                elif num == 3:
                    self.add_product()
                elif num == 4:
                    self.remove_product()
                elif num == 5:
                    print("Goodbye!")
                    sys.exit(0)
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def register_premium_member(self):
        premium_price = 5
        print("Would you like to pay the premium price of $5?")
        print("\t 1. Yes")
        print("\t 2. No")

        premium_choice = int(input("Enter your choice: "))
        if premium_choice == 1:
            pre_name = input("Enter name: ")
            pre_pay_type = input("Enter Payment Type: ")
            self.bookStore.add_premium_member(pre_name, premium_price, pre_pay_type)

    def add_product(self):
        print("What type of product would you like to add?")
        print("\t 1. Book")
        print("\t 2. DVD")
        print("\t 3. CD")
        
        product_type = int(input("Enter product type: "))
        
        try:
            if product_type == 1:
                self.add_book()
            elif product_type == 2:
                self.add_dvd()
            elif product_type == 3:
                self.add_cd()
            else:
                print("Please enter a valid number between 1-3.")
        except ValueError:
            print("Please enter a valid number.")

    def add_book(self):
        book_name = input("Enter Name: ")
        error_price = False
        while not error_price:
            try:
                book_price = float(input("Enter price: "))
                self.bookStore.add_book(book_name, book_price)
                print(f"{book_name} successfully added to the bookstore!")
                error_price = True
            except ValueError:
                print("Please enter a valid number for the price.")
                
    def add_dvd(self):
        dvd_name = input("Enter Name: ")
        error_price = False
        while not error_price:
            try:
                dvd_price = float(input("Enter price: "))
                self.bookStore.add_dvd(dvd_name, dvd_price)
                print(f"{dvd_name} successfully added to the bookstore!")
                error_price = True
            except ValueError:
                print("Please enter a valid number for the price.")

    def add_cd(self):
        cd_name = input("Enter Name: ")
        error_price = False
        while not error_price:
            try:
                cd_price = float(input("Enter price: "))
                self.bookStore.add_cd(cd_name, cd_price)
                print(f"{cd_name} successfully added to the bookstore!")
                error_price = True
            except ValueError:
                print("Please enter a valid number for the price.")

    def remove_product(self):
        print("What type of product would you like to remove?")
        print("\t 1. Book")
        print("\t 2. DVD")
        print("\t 3. CD")
        
        product_type = int(input("Enter product type: "))

        if product_type == 1:
            self.remove_book()
        elif product_type == 2:
            self.remove_dvd()
        elif product_type == 3:
            self.remove_cd()

    def remove_book(self):
        book_name = input("Enter Name: ")
        try:
            book_price = float(input("Enter price: "))
            self.bookStore.remove_book(book_name, book_price)
            print(f"{book_name} successfully removed from bookstore!")
        except ValueError:
            print("Please enter a valid number for the price.")

    def remove_dvd(self):
        dvd_name = input("Enter Name: ")
        try:
            dvd_price = float(input("Enter price: "))
            self.bookStore.remove_dvd(dvd_name, dvd_price)
            print(f"{dvd_name} successfully removed from bookstore!")
        except ValueError:
            print("Please enter a valid number for the price.")

    def remove_cd(self):
        cd_name = input("Enter Name: ")
        try:
            cd_price = float(input("Enter price: "))
            self.bookStore.remove_cd(cd_name, cd_price)
            print(f"{cd_name} successfully removed from bookstore!")
        except ValueError:
            print("Please enter a valid number for the price.")

    def purchase(self):
        print("Pick an item type:")
        print("1. Books")
        print("2. DVDs")
        print("3. CDs")
        choice = int(input("Enter choice: "))

        if choice == 1:
            self.purchase_book()
        elif choice == 2:
            self.purchase_dvd()
        elif choice == 3:
            self.purchase_cd()

    def purchase_book(self):
        print("Available Books:")
        self.bookStore.display_books()
        book_choice = int(input("Select a book: "))
        self.purchase_item(book_choice, "book")

    def purchase_dvd(self):
        print("Available DVDs:")
        self.bookStore.display_dvds()
        dvd_choice = int(input("Select a DVD: "))
        self.purchase_item(dvd_choice, "dvd")

    def purchase_cd(self):
        print("Available CDs:")
        self.bookStore.display_cds()
        cd_choice = int(input("Select a CD: "))
        self.purchase_item(cd_choice, "cd")

    def purchase_item(self, item_choice, item_type):
        print("Pick type of member:")
        print("\t 1. Regular member")
        print("\t 2. Premium member")
        mem_type = int(input("Enter choice: "))
        if mem_type == 1:
            self.bookStore.display_members()
        else:
            self.bookStore.display_premium_members()

        mem_choice = int(input("Select member: "))
        if item_type == "book":
            self.bookStore.purchase_book(item_choice, mem_choice, mem_type)
        elif item_type == "dvd":
            self.bookStore.purchase_dvd(item_choice, mem_choice, mem_type)
        elif item_type == "cd":
            self.bookStore.purchase_cd(item_choice, mem_choice, mem_type)


# Example usage
if __name__ == "__main__":
    app = Main()
    app.menu()
