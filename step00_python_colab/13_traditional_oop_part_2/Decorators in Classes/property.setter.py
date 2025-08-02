
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self._name = new_name

# Usage
p = Person('Bob')
print(p.name)
p.name = "Charlie"
print(p.name)  # Output: Charlie