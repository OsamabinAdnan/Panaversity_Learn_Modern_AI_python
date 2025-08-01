# Method Resolution Order (MRO)

class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass

# Create the instance of D
d = D()

# Check the MRO of class D
print(D.__mro__) # print(D.mro()) ==> we can write this way also

# Call the greet method on the instance of D
print(d.greet())