# **Method Resolution Order (MRO)**

**Method Resolution Order (MRO)** defines the order in which Python looks for methods and attributes in a class hierarchy, especially when **multiple inheritance** is involved. It ensures that the correct method or attribute is found and avoids ambiguity.

---

## 🔍 The `mro()` Method

The `mro()` method is a built-in Python method that returns a **list of classes** in the order they will be searched for attributes and methods. This represents the **linearization** of the class hierarchy.

---

## ⚙️ How Python Resolves Method Calls in Multiple Inheritance

Python uses the **C3 Linearization algorithm** to compute the MRO. This algorithm ensures:

- Subclasses come **before** their parent classes.
- The order of inheritance is **preserved**.
- No class is visited more than **once**.

---

## 🧪 Example: Understanding MRO in Python

### Class Hierarchy

```python
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

d = D()

# Print the MRO
print(D.mro())

# Call the greet method
print(d.greet())
```

**Explanation**

* D inherits from both B and C, which both inherit from A.
* Python will search for methods in this order: D → B → C → A → object.
* d.greet() checks D (not found), then B (found), and stops there.
