class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 1.8) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) / 1.8

# Usage
temp = Temperature(25)
print(f"{temp.celsius} °C")
print(f"{temp.fahrenheit} °F")

temp.fahrenheit = 100
print(f"{temp.celsius} °C")
print(f"{temp.fahrenheit} °F")