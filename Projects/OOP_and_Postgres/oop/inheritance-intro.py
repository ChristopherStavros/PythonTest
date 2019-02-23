class Decimal:
    def __init__(self, number, places):
        self.number = number
        self.places = places
    # def __repr__(self):
    #     return "%.2f" % self.number # 2 for decimal places, f for floating point

    def __repr__(self):
        return "%.{}f".format(self.places) % self.number

    def add(self):
        pass

class Currency(Decimal):
    def __init__(self, symbol, number, places):
        super().__init__(number, places)
        self.symbol = symbol

    def __repr__(self):
        return "{}{}".format(self.symbol, super().__repr__())

    def add_currency(self, currency):
        pass


print(Decimal(15.6789, 3))
print(Currency("$", 15.6789, 3))