from example1 import Shirt

shirt_one = Shirt("red", "M", "long_sleeved", 45)
shirt_two = Shirt("orange", "S", "short_sleeved", 30)

print(shirt_one.price)
print(shirt_one.color)

shirt_two.change_price(45)
print(shirt_two.price)

"""
   The direct manipulation of attributes should be avoided, since changing attributes 
   directly instead of using a method can be tedious and unnecessary work.
   We can use Get and Set method i.e. get_price and set_price instead of change_price
   This stimulates the situation like in another programming languages.
   eg:
   class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self._price = shirt_price

    def get_price(self):
      return self._price

    def set_price(self, new_price):
      self._price = new_price
      
    shirt_one = Shirt('yellow', 'M', 'long-sleeve', 15)
    print(shirt_one.get_price())
    shirt_one.set_price(10)

"""
shirt_one.color = "yellow"
shirt_one.size = "L"
shirt_one.price = 43
