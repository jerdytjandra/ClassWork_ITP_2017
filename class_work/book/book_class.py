class Book(object):
    def __init__(self, name, author, price, qty):
        self.name = name
        self.author = author
        self.price = price
        self.qty = qty

    def get_name(self):
        return self.name

    def get_authors(self):
        return self.author

    def get_price(self):
        return self.price

    def get_qty(self):
        return self.qty

    def set_price(self, amt):
        self.price = amt

    def set_qty(self, amt):
        self.qty = amt

    def to_string(self):
        print("\nBook:", self.name, "\n\tAuthor:", self.author, "\n\tPrice =", self.price)


from book.Author_class import Author

author1 = Author("C. S. Lewis", "-", "male")
author1.author_info()
