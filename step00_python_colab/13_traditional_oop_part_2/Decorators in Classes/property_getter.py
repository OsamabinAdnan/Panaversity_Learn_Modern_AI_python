class Person:
    def __init__(self, name):
        self._name = name  # Internal variable (convention: `_name`)
    
    @property
    def name(self):
        """Get the person's name."""
        return self._name

# Usage
p = Person('John')
print(p.name)