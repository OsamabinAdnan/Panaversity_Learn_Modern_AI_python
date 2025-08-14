
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