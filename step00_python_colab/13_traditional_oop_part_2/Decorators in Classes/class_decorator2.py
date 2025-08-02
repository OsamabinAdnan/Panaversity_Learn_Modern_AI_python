# Define a class decorator

def add_greeting(cls):
    def greet(self):
        return f"Decorator: Hello from {self.__class__.__name__} |", self.name
    cls.greet = greet
    return cls

# Apply the decorator to a class

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance of the decorated class
person = Person("Alice")
print(person.greet())  # Output: Hello from Person