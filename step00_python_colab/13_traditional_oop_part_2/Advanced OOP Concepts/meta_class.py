# Custom class
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

# Class using the custom metaclass
class MyClass(metaclass=Meta):
    pass

# Output: Creating class: MyClass