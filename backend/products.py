class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self, discount_rate=0):
        return self.price * (1 - discount_rate)

# 20% discount
class DigitalProduct(Product):
    def get_discounted_price(self, discount_rate=0):
        base_price = super().get_discounted_price(discount_rate)
        return base_price * 0.80