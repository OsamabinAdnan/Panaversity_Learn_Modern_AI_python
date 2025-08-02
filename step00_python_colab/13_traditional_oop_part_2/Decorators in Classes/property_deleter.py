class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.deleter
    def name(self):
        print(f"Deleting name: {self._name}")
        del self._name

# Usage
p = Person('Bob')
print(p.name)
del p.name  # Output: Deleting name: Bob
# print(p.name)  # AttributeError: name