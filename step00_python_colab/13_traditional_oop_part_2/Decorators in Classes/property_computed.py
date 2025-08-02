class Person:
    def __init__(self, weight_kg, height_m):
        self.weight = weight_kg
        self.height = height_m

    @property
    def bmi(self):
        """Body Mass Index (weight / height²)"""
        return self.weight / (self.height ** 2)

# Usage
p = Person(70, 1.75)  # 70kg, 1.75m
print(p.bmi)  # Output: 22.857...