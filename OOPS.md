## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods and model real-world entities. It helps organize code, making it easier to manage, understand, and reuse.

# Classes and Objects

**Class:** A blueprint for creating objects. It defines properties (attributes) and behaviors (methods).

**Object:** An **instance** of a class. It can hold data and perform actions defined in the class.

```python
class Dog:
    # Class Attribute
    species = "Canine"

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name  # Instance Attribute
        self.age = age    # Instance Attribute

# Creating an object of the class
my_dog = Dog("Buddy", 5)
print(my_dog.name)  # Output: Buddy
```
