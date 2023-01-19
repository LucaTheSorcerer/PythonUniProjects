class BadName(Exception):
    pass

class Shop:
    def __init__(self, products : list[str]):
        self.products = products

    def buy(self, price):
        products_list = []
        for product in self.products:
            print(len(product))
            if len(product)*2 > price:
                raise BadName("Incorrect")

            products_list.append(f"{product} - {price}")

        return products_list


class BetterShop(Shop):
    def __init__(self, products):
        super().__init__(products)
        self.total = 0

    def buy(self, price):
        try:
            correct = super().buy(price)
            print(correct)
            self.total += price
        except BadName:
            self.total = -1


    def __sub__(self, other):
        empty_list = []
        for product in self.products:
            if product in self.products and product in other.products:
                empty_list.append(product)

        return empty_list

def main():
    s1 = Shop(['Lapte', 'Apa', 'Ciocolata'])

    print(s1.buy(40))

    s2 = BetterShop(['Lapte', 'Apa', 'Ciocolata'])
    s3 = BetterShop(['Mamaliga', 'Paste', 'Calorifer'])
    s4 = BetterShop(['Apa', 'Paste', 'Calorifer'])

    print(s2.buy(40))
    print(s3.buy(40))
    print(s3-s4)


main()