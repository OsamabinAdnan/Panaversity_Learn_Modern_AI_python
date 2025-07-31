# Composition and Aggregation in Object-Oriented Programming

Composition and aggregation are both ways to relate classes in object-oriented programming, focusing on how objects **contain** or **interact** with each other.

---

## 🔧 What is Composition? (Strong Relationship)

- Composition is a **"has-a"** relationship where one object **contains** another.
- The **contained object's lifecycle depends on the container** object.
- If the container is destroyed, so is the contained object.
- It's a **strong relationship**, like a **car and its engine** — the car cannot function without the engine.

✅ **Example Use Case**: Building complex objects by combining simpler ones.

---

## 🧩 What is Aggregation? (Weak Relationship)

- Aggregation is also a **"is-a"** relationship but represents a **weaker** association than composition.
- The contained object can **exist independently** of the container.
- It's like a **university and its departments** — the departments can still exist even if the university ceases to exist.

✅ **Example Use Case**: Objects interacting with one another without owning them.

---

## 🆚 Difference Between Composition and Inheritance

| Feature       | Composition                     | Inheritance                     |
|---------------|----------------------------------|----------------------------------|
| **Relation**  | "Has-a"                          | "Is-a"                           |
| **Flexibility** | High — components can be changed easily | Lower — changes ripple through the hierarchy |
| **Coupling**  | Loose — easier to maintain       | Tight — can lead to fragile code |
| **Reuse**     | Combines behaviors by using objects | Reuses code via class hierarchy  |

🔎 **Conclusion**:  
While inheritance has its place, **composition** is generally preferred due to better flexibility and lower coupling.

---

## 🧪 Example: Implementing Composition and Aggregation

### 🧱 Composition Example

```python
class Engine:
    def start(self):
        return "Engine starting"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car *has-a* Engine, and owns it

    def start(self):
        return f"Car starting: {self.engine.start()}"
```

In this example:

* Car and Engine demonstrate composition. The Car class creates and owns an instance of the Engine class. If the Car object is destroyed, the Engine object is also destroyed.

* University and Department demonstrate aggregation. The University class contains a list of Department objects, but the Department objects can exist independently of the University object. The university does not exclusively own the Department.