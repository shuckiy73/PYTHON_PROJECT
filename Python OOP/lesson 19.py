class Products:
    def __init__(self, products, bonuses=0):
        self.bonuses = bonuses
        self.products = products

    def get_products_price(self):
        return sum(self.products.values()) - self.bonuses

    def __str__(self):
        return f'Цена: {self.get_products_price()}. {self.products}'

    def __eq__(self, other):
        return self.get_products_price() == other.get_products_price()

    def __gt__(self, other):
        return self.get_products_price() > other.get_products_price()

    def __ge__(self, other):
        return self.get_products_price() >= other.get_products_price()


products1 = Products({'Молоко': 3, 'Сыр': 5})
products2 = Products({'Колбаса': 8})

print(products1 != products2)
# products1 != products2
# not (products1 == products2)
