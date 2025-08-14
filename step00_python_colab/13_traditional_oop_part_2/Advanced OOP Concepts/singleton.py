class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Create instances of the Singleton class
singleton1 = Singleton()
singleton2 = Singleton()

# Check if both instances are the same
print(singleton1 is singleton2)  # Output: True
print(id(singleton1) == id(singleton2))  # Output: True