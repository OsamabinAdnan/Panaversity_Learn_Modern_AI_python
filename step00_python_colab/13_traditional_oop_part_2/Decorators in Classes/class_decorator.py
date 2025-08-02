class CountCalls:
    def __init__(self, func):
        self.func = func
        self.call_count = 0
    
    def __call__(self, *args, **kwds):
        self.call_count += 1
        print(f"Decorator: Call {self.call_count} of {self.func.__name__}")
        return self.func(*args, **kwds)

@CountCalls
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Alice")
say_hello("Bob")
say_hello("Charlie")