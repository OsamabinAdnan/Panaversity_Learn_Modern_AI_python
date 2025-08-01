# Example with Diamond Inheritance

class X:
    def greet(self):
        return "Hello from X"

class Y(X):
    def greet(self):
        return "Hello from Y"

class Z(X):
    def greet(self):
        return "Hello from Z"

class W (Y, Z):
    pass

# Create an instance of W
w = W()

# Check the MRO of class W
print(W.mro())

# Call the greet method
print(w.greet())  # Output: Hello from Y