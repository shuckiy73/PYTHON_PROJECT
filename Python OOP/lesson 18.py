class Products:
    def __init__(self, products, bonuses=0):
        self.bonuses = bonuses
        self.products = products

    def get_products_price(self):
        return sum(self.products.values()) - self.bonuses

    def __add__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses + other)
        elif isinstance(other, Products):
            new_products = {}
            for product, price in self.products.items():
                if product not in new_products:
                    new_products[product] = price
            for product, price in other.products.items():
                if product not in new_products:
                    new_products[product] = price
            return Products(new_products)

    def __radd__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses + other)

    def __sub__(self, other):
        if isinstance(other, str):  # Check if the other is a product name
            new_products = self.products.copy()
            new_products.pop(other, None)  # Remove the product if it exists
            return Products(new_products, self.bonuses)
        elif isinstance(other, int):  # Check if the other is an integer (for bonus deduction)
            return Products(self.products, self.bonuses - other)

    def __rsub__(self, other):
        if isinstance(other, str):  # Check if the other is a product name
            new_products = self.products.copy()
            new_products.pop(other, None)  # Remove the product if it exists
            return Products(new_products, self.bonuses)
        elif isinstance(other, int):  # Check if the other is an integer (for bonus deduction)
            return Products(self.products, other - self.bonuses)


products1 = Products({'Молоко': 3, 'Сыр': 5})
print(f'Цена: {products1.get_products_price()}. {products1.products}')
products2 = Products({'Кефир': 2})
products3 = products1 + products2
print(f'Цена: {products3.get_products_price()}. {products3.products}')
products4 = products3 + 2
products5 = 1 + products4
products5 += 1
print(f'Цена: {products5.get_products_price()}. {products5.products}')


products1 = Products({'Молоко': 3, 'Сыр': 5}, bonuses=2)
products1 -= 'Молоко'  # Remove 'Молоко' from the cart
print(f'Цена: {products1.get_products_price()}. {products1.products}')

products1 -= 1  # Subtract 1 from the bonuses
print(f'Цена: {products1.get_products_price()}. {products1.products}')
