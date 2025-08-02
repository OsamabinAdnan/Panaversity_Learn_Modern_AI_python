# **Decorators in Classes**

Decorators in Python are a powerful feature that allows you to modify or extend the behavior of functions or methods. When applied to classes, decorators can enhance or alter the behavior of the class or its methods. Additionally, Python provides specific property decorators (@property, @setter, and @deleter) to manage attribute access in a controlled way.

## **Class Decorators**
A class decorator is a function that takes a class as input and returns a modified or extended version of the class. It’s often used to add functionality, enforce constraints, or modify class behavior.

## **Property Decorators**
The @property decorator is used to define a method as a getter for a class attribute. It allows you to access the attribute like a property rather than a method. You can also define setter and deleter methods using the @setter and @deleter decorators, respectively.

## **Example: Using Decorators in Classes**
Let’s create examples to demonstrate class decorators and property decorators.

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"Decorator: Call {self.call_count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
say_hello("Bob")
```
```bash     
Decorator: Call 1 of say_hello
Hello, Alice!
Decorator: Call 2 of say_hello
Hello, Bob!
```
In this example, CountCalls is a class decorator that counts the number of times a function is called. The @CountCalls syntax above the say_hello function applies the CountCalls decorator to it. Each time say_hello is called, the `__call__` method of CountCalls is executed, incrementing the call_count and printing a message.

```python
# Define a class decorator
def add_greeting(cls):
    def greet(self):
        return f"Decorator: Hello from {self.__class__.__name__} | ", self.name
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
```
```bash     
('Decorator: Hello from Person | ', 'Alice')
```
## **Property Decorator Example**
The @property decorator lets you control how an attribute is accessed, set, or deleted in a class.
It allows you to add logic (like validation or calculations) while still making it look like a simple attribute.

### **1️⃣ Basic Getter (Read-Only Property)**
* Turns a method into a "getter" (like reading an attribute).
* No parentheses needed!

#### **Example: Get a value**
```python
class Person:
    def __init__(self, name):
        self._name = name  # Internal variable (convention: `_name`)

    @property
    def name(self):
        """Getter for name"""
        return self._name

# Usage
p = Person("Alice")
print(p.name)  # Like an attribute (no parentheses!)
```
```bash     
Alice
```
➡️ `name` acts like an attribute, but it's a method!

### **2️⃣ Setter (Change a Value with Validation)**
* @prop_name.setter lets you modify the attribute.
* Add checks before setting!

#### **Example: Set with validation**
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string!")
        self._name = new_name

# Usage
p = Person("Bob")
p.name = "Charlie"  # Works
print(p.name)  # Output: Charlie

#p.name = 123  # ❌ Error! (ValueError: Name must be a string!) # uncomment to see error
```
```bash     
Charlie
```
### **3️⃣ Deleter (Remove an Attribute)**

* @prop_name.deleter runs when you del obj.prop.
* Used for cleanup.

#### **Example: Delete safely**

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Deleting name!")
        del self._name

# Usage
p = Person("Dave")
print(p.name)  # Output: Dave

del p.name  # Runs deleter
#print(p.name)  # ❌ Error! (AttributeError: 'Person' has no attribute '_name') # uncomment to see error
```
```bash     
Dave
Deleting name!
```

### **4️⃣ Computed Property (Dynamic Value)**
* Calculate a value on the fly!

#### **Example: Get BMI from height & weight**

```python
class Person:
    def __init__(self, weight_kg, height_m):
        self.weight = weight_kg
        self.height = height_m

    @property
    def bmi(self):
        """Body Mass Index (weight / height²)"""
        return self.weight / (self.height ** 2)

# Usage
p = Person(70, 1.75)  # 70kg, 1.75m
print(p.bmi)  # Output: 22.857...
```
```bash     
22.857142857142858
```
**➡️ No `bmi.setter` → You can't change `bmi` directly!**

## 📊 Property Decorators Summary Table

| Task            | Syntax                             | Example       |
|-----------------|-------------------------------------|---------------|
| Get a value     | `@property def x(self):`            | `print(obj.x)` |
| Set a value     | `@x.setter def x(self, value):`     | `obj.x = 10`   |
| Delete a value  | `@x.deleter def x(self):`           | `del obj.x`    |
| Computed value  | `@property def y(self): return ...` | `print(obj.y)` |
	
## **✅ When to Use @property**
* Add validation (e.g., check if age ≥ 0).
* Make read-only attributes (like bmi).
* Hide internal variables (use _name instead of name).
* Change how attributes work without breaking existing code.

#### **Final Example (Temperature Converter 🌡️)**

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Usage
temp = Temperature(0)  # 0°C
print(temp.fahrenheit)  # 32°F

temp.fahrenheit = 100  # Set in °F → auto-converts to °C
print(temp.celsius)    # 37.777...°C
```
```bash
32.0
37.77777777777778
```
**➡️ Smooth conversion between Celsius & Fahrenheit!**

## **🎯 Key Takeaway**

`@property` makes your code cleaner & safer by letting you control attribute access without changing how users interact with your class! 🚀

* Python decorators are a design pattern that allows you to modify the functionality of a function by wrapping it in another function.
* `Class decorators` modify or extend the behavior of a class.
* A decorator is a callable that returns a callable.
    1. `Callable:` In Python, "callable" refers to something that can be called like a function, using parentheses (). This includes functions themselves, but also objects that have a `__call__`() method defined4.
    2. `Decorator Takes a Callable:` A decorator's primary job is to accept a function (or another callable) as an argument. This is the function it will modify or enhance.
    3. `Decorator Returns a Callable:` After processing the input callable (usually by wrapping it with some added functionality), the decorator must return another callable. This is usually a modified version of the original function.

* Decorators seem better suited to modify the functionality of an entire object (including function objects) versus the functionality of an object method which in general will depend on instance attributes.

* Property decorators (@property, @setter, @deleter) allow you to manage attribute access in a controlled way.

* The @property decorator defines a getter method for an attribute.

* The @setter decorator defines a setter method for an attribute.

* The @deleter decorator defines a deleter method for an attribute.

**In essence, decorators are a way to modify or extend the behavior of functions or methods without changing their actual code. They achieve this by wrapping the original function within another function (the decorator).**

This example demonstrates how to use decorators in Python classes effectively. 🚀

## **What is Callable**

In Python, a `callable` is an object that can be called like a function. In other words, it's an object that can be invoked with parentheses `()` to execute some code.

**Examples of callables:**

1. **Functions:** These are the most obvious examples of callables. You can define a function using the def keyword and call it by its name followed by parentheses.

2. **Lambda functions:** These are small, anonymous functions that can be defined inline.

3. **Classes:** Yes, you can call a class like a function! When you do, it creates a new instance of the class.

4. **Methods:** These are functions that are part of a class.

5. **Instances of classes that implement `__call__`:** If a class defines a special method called `__call__`, instances of that class become callable.

**What makes an object callable?**

An object is callable if it has a `__call__` method. This method is a special method that's invoked when you call the object like a function.

**Example:**
```python
class MyClass:
    def __call__(self):
        print("I'm callable!")

obj = MyClass()
obj()  # Output: I'm callable!
```
```bash     
I'm callable!
```
In this example, `MyClass` defines a `__call__` method, so instances of MyClass become callable.

**Checking if an object is callable**

You can use the `callable()` function to check if an object is callable:

```python
def my_function():
    pass

print(callable(my_function))  # Output: True

class MyClass:
    def __call__(self):
        pass

obj = MyClass()
print(callable(obj))  # Output: True

print(callable("hello"))  # Output: False
```
```bash     
True
True
False
```
In this example, we define a function `my_function` and a class `MyClass` with a `__call__` method. We then create an instance of MyClass and check if each object is callable using `callable()`. The string "hello" is not callable, so callable("hello") returns False.

**Use cases for callables**

Callables have many use cases, such as:

* Creating higher-order functions that take other functions as arguments
* Implementing callbacks or event handlers
* Creating factories or constructors that return instances of classes
* Creating domain-specific languages (DSLs) or mini-languages
* I hope this helps! Let me know if you have any questions or need further clarification.