class BookStore:
    def __init__(self):
        """
        Initialize the BookStore with inventories and members.
        """
        self.books = []
        self.dvds = []
        self.cds = []
        self.members = []
        self.premium_members = []

        # Add items to inventory
        # Books inventory
        book1 = Book("It ends with us", 5.45)
        self.books.append(book1)
        book2 = Book("Verity", 5.45)
        self.books.append(book2)
        book3 = Book("Ugly love", 5.45)
        self.books.append(book3)

        # CDs inventory
        cd1 = CD("Superhero(Heroes & Villains)", 12.99)
        self.cds.append(cd1)
        cd2 = CD("Savage Mode II", 12.99)
        self.cds.append(cd2)
        cd3 = CD("Not All Heroes Wear Capes", 12.99)
        self.cds.append(cd3)

        # DVDs inventory
        dvd1 = DVD("Get Out", 10.99)
        self.dvds.append(dvd1)
        dvd2 = DVD("US", 10.99)
        self.dvds.append(dvd2)
        dvd3 = DVD("Nope", 10.99)
        self.dvds.append(dvd3)

        # Add regular members
        mem1 = Member("John", 3.45)
        self.members.append(mem1)
        mem2 = Member("Sally", 3.45)
        self.members.append(mem2)

        # Add premium members
        p_mem1 = PremiumMember("Sherin", 2.45, "credit")
        self.premium_members.append(p_mem1)
        p_mem2 = PremiumMember("Shawn", 2.45, "debit")
        self.premium_members.append(p_mem2)

    # Getters for the inventories
    def get_books(self):
        return self.books

    def get_dvds(self):
        return self.dvds

    def get_cds(self):
        return self.cds

    # Display methods
    def display_books(self):
        if not self.books:
            print("No books in inventory.")
        else:
            print("BOOKS IN INVENTORY:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book.get_name()} - ${book.get_price()}")

    def display_dvds(self):
        if not self.dvds:
            print("No DVDs in inventory.")
        else:
            print("DVDS IN INVENTORY:")
            for idx, dvd in enumerate(self.dvds, 1):
                print(f"{idx}. {dvd.get_name()} - ${dvd.get_price()}")

    def display_cds(self):
        if not self.cds:
            print("No CDs in inventory.")
        else:
            print("CDS IN INVENTORY:")
            for idx, cd in enumerate(self.cds, 1):
                print(f"{idx}. {cd.get_name()} - ${cd.get_price()}")

    def display_members(self):
        if not self.members:
            print("No members found.")
        else:
            print("Members:")
            for idx, member in enumerate(self.members, 1):
                print(f"{idx}. {member.get_name()}")

    def display_premium_members(self):
        if not self.premium_members:
            print("No premium members found.")
        else:
            print("Premium Members:")
            for idx, premium_member in enumerate(self.premium_members, 1):
                print(f"{idx}. {premium_member.get_name()}")

    # Add new items
    def add_book(self, name, price):
        new_book = Book(name, price)
        self.books.append(new_book)

    def add_dvd(self, name, price):
        new_dvd = DVD(name, price)
        self.dvds.append(new_dvd)

    def add_cd(self, name, price):
        new_cd = CD(name, price)
        self.cds.append(new_cd)

    # Remove items
    def remove_book(self, name, price):
        self.books = [book for book in self.books if not (book.get_name() == name and book.get_price() == price)]

    def remove_dvd(self, name, price):
        self.dvds = [dvd for dvd in self.dvds if not (dvd.get_name() == name and dvd.get_price() == price)]

    def remove_cd(self, name, price):
        self.cds = [cd for cd in self.cds if not (cd.get_name() == name and cd.get_price() == price)]

    # Add members
    def add_premium_member(self, name, premium_price, payment_type):
        new_premium_member = PremiumMember(name, premium_price, payment_type)
        self.premium_members.append(new_premium_member)
        print(new_premium_member)

    # Purchase methods
    def purchase_book(self, book_choice, mem_choice, mem_type):
        if mem_type == 1:  # Regular membership
            selected_book = self.get_books()[book_choice - 1]
            selected_member = self.get_members()[mem_choice - 1]
            selected_member.set_spent(selected_book.get_price())
            self.books.remove(selected_book)
            print(f"{selected_book.get_name()} sold to {selected_member.get_name()}")

        elif mem_type == 2:  # Premium membership
            selected_book = self.get_books()[book_choice - 1]
            selected_premium_member = self.get_premium_members()[mem_choice - 1]
            selected_premium_member.set_spent(selected_book.get_price())
            self.books.remove(selected_book)
            print(f"{selected_book.get_name()} sold to {selected_premium_member.get_name()}")

        return "No more books, sorry :("

    def purchase_dvd(self, dvd_choice, mem_choice, mem_type):
        if mem_type == 1:
            selected_dvd = self.get_dvds()[dvd_choice - 1]
            selected_member = self.get_members()[mem_choice - 1]
            selected_member.set_spent(selected_dvd.get_price())
            self.dvds.remove(selected_dvd)
            print(f"{selected_dvd.get_name()} sold to {selected_member.get_name()}")

        elif mem_type == 2:
            selected_dvd = self.get_dvds()[dvd_choice - 1]
            selected_premium_member = self.get_premium_members()[mem_choice - 1]
            selected_premium_member.set_spent(selected_dvd.get_price())
            self.dvds.remove(selected_dvd)
            print(f"{selected_dvd.get_name()} sold to {selected_premium_member.get_name()}")

        return "No more DVDs, sorry :("

    def purchase_cd(self, cd_choice, mem_choice, mem_type):
        if mem_type == 1:
            selected_cd = self.get_cds()[cd_choice - 1]
            selected_member = self.get_members()[mem_choice - 1]
            selected_member.set_spent(selected_cd.get_price())
            self.cds.remove(selected_cd)
            print(f"{selected_cd.get_name()} sold to {selected_member.get_name()}")

        elif mem_type == 2:
            selected_cd = self.get_cds()[cd_choice - 1]
            selected_premium_member = self.get_premium_members()[mem_choice - 1]
            selected_premium_member.set_spent(selected_cd.get_price())
            self.cds.remove(selected_cd)
            print(f"{selected_cd.get_name()} sold to {selected_premium_member.get_name()}")

        return "No more CDs, sorry :("

    # Getters for members
    def get_members(self):
        return self.members

    def get_premium_members(self):
        return self.premium_members
