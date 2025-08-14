# **Advanced OOP Concepts**

In this section, we’ll explore some advanced Object-Oriented Programming (OOP) concepts in Python, including metaclasses, design patterns (Singleton and Factory), and how to implement them.

## **1. Metaclasses**
A metaclass is the class of a class. It defines how a class behaves. In Python, the default metaclass is type. You can create custom metaclasses to control class creation and behavior.

## **2. Singleton Design Pattern**
The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. This is useful when you need to manage shared resources, such as a database connection or configuration settings.

## **3. Factory Design Pattern**
The Factory pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. It promotes loose coupling and flexibility.

## **To know more about Design Pattern please visit:**

[The Catalog of Python Design Pattern Examples](https://refactoring.guru/design-patterns/python)

[Gang of Four design patterns in Python](https://github.com/tuvo1106/python_design_patterns)

[Gang of Four (GOF) Design Patterns](https://www.geeksforgeeks.org/system-design/gang-of-four-gof-design-patterns/)

### **Example: Implementing Advanced OOP Concepts in Python**
Let’s create examples to demonstrate metaclasses, the Singleton pattern, and the Factory pattern.

### **Metaclass Example**

```python
# Custom metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

# Class using the custom metaclass
class MyClass(metaclass=Meta):
    pass

# Output: Creating class: MyClass
```

```bash
Creating class: MyClass
```

### **Singleton Design Pattern Example**
```python
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
```
```bash
True
True
```

### **Factory Design Pattern Example**

```python
# Product interface
class Animal:
    def speak(self):
        pass

# Concrete products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Factory class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

# Use the factory to create animals
dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")

# Call the speak method
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
```
```bash     
Woof!
Meow!
```
## **Explanation of the Code**

### **1. Metaclass:**

* The Meta metaclass overrides the __new__ method to print a message when a class is created.
* The MyClass class uses Meta as its metaclass.

### **2. Singleton Pattern:**

* The Singleton class ensures that only one instance is created by overriding the new method.
* Multiple instances of Singleton refer to the same object.

### **3. Factory Pattern:**

* The Animal class defines the interface for all animal products.
* The Dog and Cat classes are concrete implementations of Animal.
* The AnimalFactory class provides a method (create_animal) to create instances of Dog or Cat based on the input.

## **Key Takeaways**

* **Metaclasses** control the behavior of class creation. You can use them to customize how classes are created and initialized.

* The **Singleton pattern** ensures that a class has only one instance and provides a global point of access to it.

* The **Factory pattern** provides a way to create objects without specifying the exact class of the object that will be created.

* These advanced OOP concepts are useful for managing complex systems and promoting code reusability and flexibility.

This example demonstrates how to implement advanced OOP concepts in Python effectively. 🚀