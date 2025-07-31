class Bakery:
    type = "cake" # Class variable

    def __init__(self, flavor, price):
        self.flavor = flavor # Instance variable
        self.price = price # Instance variable
    
    def update_cake_count(cls, count):
        cls.cake_count = count
    
# Accessing
print("Bakery.type:",Bakery.type)  # Output: cake

cake1 = Bakery("Chocolate", 20.00)
cake2 = Bakery("Vanilla", 18.00)

print("Cake 1 flavor:",cake1.flavor)  # Output: Chocolate
print("Cake 2 price:",cake2.price)  # Output: 18.00

# Modifying
Bakery.type = "pastry"
print("Cake 1 type:",cake1.type)  # Output: pastry

cake1.type = "cupcake"
print("Cake 1 type:",cake1.type) # Output: cupcake
print("Cake 2 type:",cake2.type)  # Output: pastry