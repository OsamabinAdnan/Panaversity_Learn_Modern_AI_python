# 11. Class and Static Variables in Python

Class and static variables are used to store data that is related to the **class itself**, rather than to individual **instances** of the class. They allow data and behavior to be shared across all instances of a class.

---

## 🔄 Difference Between Class and Static Variables

Although often used interchangeably in Python, the term **class variable** is more commonly used. These variables are defined inside the class but **outside any methods**.

- **Class Variables**:  
  Associated with the class and shared among all instances. Defined inside the class but outside any method.
  
- **Instance Variables**:  
  Unique to each object (instance) of the class.

---

## 🔓 Accessing and 🔧 Modifying Class Variables

- **Accessing**:
  - Using the class name: `ClassName.variable_name`
  - Or through an instance: `instance_name.variable_name`

- **Modifying**:
  - If modified via an instance, it creates a **new instance variable** that shadows the class variable.
  - To truly modify the class variable, use the **class name**.

---

## 🧪 Example: Working with Class and Static Variables

```python
class Bakery:
    type = "cake"  # Class variable

    def __init__(self, flavor, price):
        self.flavor = flavor  # Instance variable
        self.price = price    # Instance variable

    def update_cake_count(cls, count):
        cls.cake_count = count

# Accessing
print(Bakery.type)

cake1 = Bakery("Chocolate", 25.00)
cake2 = Bakery("Vanilla", 22.00)

print(cake1.flavor)
print(cake2.price)

# Modifying
Bakery.type = "pastry"
print(cake1.type)

cake1.type = "cookie"  # This creates an instance variable
print(cake1.type)
print(cake2.type)
```

## 🧾 Key Differences Summarized

| Feature      | Class Variable                             | Instance Variable                          |
|--------------|---------------------------------------------|---------------------------------------------|
| **Scope**    | Shared by all instances of the class        | Unique to each instance                     |
| **Creation** | Created when the class is defined           | Created when an object is instantiated      |
| **Access**   | Via class name or instance                  | Via instance only                           |
| **Modify**   | Modified using the class name               | Modified through the instance               |

### **Use Cases**
- **Class Variables**: Maintain values common to all instances, like configuration settings or counters.
- **Instance Variables**: Store data unique to each object, like user input or specific attributes.

---