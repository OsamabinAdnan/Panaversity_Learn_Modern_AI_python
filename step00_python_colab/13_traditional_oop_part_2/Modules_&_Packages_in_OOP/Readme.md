# 15. Working with Modules and Packages in OOP

Organizing your code into modules and packages is essential for maintaining clean, scalable, and maintainable code, especially in large projects. In Python, a **module** is a single file containing Python code (e.g., classes, functions, variables), and a **package** is a directory containing multiple modules and an `__init__.py` file.

## Organizing Classes in Modules
- Group related classes into a single module.
- Use meaningful names for modules and classes.
- Avoid putting all classes in a single module (unless the project is very small).

## Importing Classes from Modules
- Use the `import` statement to import the entire module.
- Use `from module import ClassName` to import specific classes.
- Use `from module import *` to import all classes (not recommended for large projects).

## Example: Structuring a Python Project Using OOP
Let’s create a simple project to demonstrate how to organize classes into modules and import them.

### Directory Structure
```bash
my_project/
│
├── animals/
│   ├── __init__.py
│   ├── mammals.py
│   └── birds.py
│
├── vehicles/
│   ├── __init__.py
│   ├── cars.py
│   └── bikes.py
│
└── main.py
```


### Code for Each Module

**1. animals/mammals.py**
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"
```

**2. animals/birds.py**
```python
class Parrot:
    def speak(self):
        return "Squawk!"

class Sparrow:
    def speak(self):
        return "Chirp!"
```

**3. vehicles/cars.py:**
```python
class Car:
    def __init__(self, model):
        self.model = model

    def display(self):
        return f"Car: {self.model}"
```
     
**4. vehicles/bikes.py:**
```python
class Bike:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        return f"Bike: {self.brand}"
```

**5. animals/__init__.py:**
```python
from .mammals import Dog, Cat
from .birds import Parrot, Sparrow
```

**6. vehicles/__init__.py:**
```python
from .cars import Car
from .bikes import Bike
```

### **Code for main.py**

```python
from animals import Dog, Cat, Parrot, Sparrow
from vehicles import Car, Bike

# Create instances of animal classes
dog = Dog()
cat = Cat()
parrot = Parrot()
sparrow = Sparrow()

# Call methods from animal classes
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print(parrot.speak())  # Output: Squawk!
print(sparrow.speak())  # Output: Chirp!

# Create instances of vehicle classes
car = Car("Toyota Corolla")
bike = Bike("Harley Davidson")

# Call methods from vehicle classes
print(car.display())  # Output: Car: Toyota Corolla
print(bike.display())  # Output: Bike: Harley Davidson
```

### **Explanation of the Code**

1. **Module Organization:**

* Related classes are grouped into modules (mammals.py, birds.py, cars.py, bikes.py).
* The init.py files in the animals and vehicles directories make them packages and allow importing classes directly from the package.

2. **Importing Classes:**

* In main.py, classes are imported from their respective modules using from animals import Dog, Cat, Parrot, Sparrow and from vehicles import Car, Bike.
3. **Using Classes:**

* Instances of the classes are created, and their methods are called in main.py.

### **Output of the Code**
```bash
Woof!
Meow!
Squawk!
Chirp!
Car: Toyota Corolla
Bike: Harley Davidson
```
### **Key Takeaways**

* **Modules** organize related classes, functions, and variables into a single file.
* **Packages** are directories containing multiple modules and an __init__.py file.
* Use the import statement or from module import ClassName to import classes from modules.
* Organizing your project into modules and packages improves readability, maintainability, and scalability.

This example demonstrates how to structure a Python project using OOP principles effectively. 🚀