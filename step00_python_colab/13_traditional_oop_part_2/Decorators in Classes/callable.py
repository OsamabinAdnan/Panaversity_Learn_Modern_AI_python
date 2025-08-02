# Class callable
class MyClass:
    def __call__(self):
        print("I'm callable from class!")

obj = MyClass()
obj() # Output: I'm callable from class!

# Object callable

def my_function():
    pass

print(callable(my_function)) # Output: True

class MyClass:
    def __call__(self):
        pass

obj = MyClass()
print(callable(obj)) # Output: True

print(callable("Hello")) # Output: False
