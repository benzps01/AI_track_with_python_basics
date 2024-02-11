"""
    Short example on Class, attributes and methods
"""


class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


new_shirt = Shirt("red", "S", "short sleeve", 15)
print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

new_shirt.change_price(10)
print(new_shirt.price)

print(new_shirt.discount(0.2))

tshirt_collection = []
shirt_one = Shirt("orange", "M", "short_sleeve", 25)
shirt_two = Shirt("red", "S", "short_sleeve", 15)
shirt_three = Shirt("purple", "XL", "short_sleeve", 10)

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)

for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].color)
