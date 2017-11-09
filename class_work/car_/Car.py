class car(object):
    def __init__(self, type, price):
        self.type = type
        self.price = price

    def print_info(self):
        print("Type = ", self.type, "\nPrice = ", self.price)
