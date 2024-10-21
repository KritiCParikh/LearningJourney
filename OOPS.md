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
# Real Motorbike Examples

## Class: Motorbike Company

In this scenario, the class represents a motorbike company. We'll create a class named `Motorbike`, which defines the general attributes and methods that all motorbikes produced by this company will have.

### Python Code

```python
class Motorbike:
    # Class Attribute
    company_name = "Harley-Davidson"  # Example Company

    # Initializer / Instance Attributes
    def __init__(self, model, engine_capacity, color):
        self.model = model  # Instance Attribute (e.g., "Street 750")
        self.engine_capacity = engine_capacity  # Instance Attribute (e.g., 750cc)
        self.color = color  # Instance Attribute (e.g., "Black")

    # Method to display details about the motorbike
    def display_info(self):
        return f"{self.company_name} {self.model} - {self.engine_capacity}cc, Color: {self.color}"
```
## Object: Specific Motorbike Models

Now, let's create objects that represent specific models from Harley-Davidson, such as the Street 750 and Sportster 1200. Each object can have its own unique characteristics but will share the general structure defined in the `Motorbike` class.

### Python Code

```python
# Creating objects of the Motorbike class
motorbike1 = Motorbike("Street Glide", 1753, "Vivid Black")  
motorbike2 = Motorbike("Iron 883", 883, "River Rock Gray")

# Accessing properties and methods of the objects
print(motorbike1.display_info())  # Output: Harley-Davidson Street Glide - 1753cc, Color: Vivid Black
print(motorbike2.display_info())  # Output: Harley-Davidson Iron 883 - 883cc, Color: River Rock Gray

## Explanation

### Class as a Motorbike Company:
The `Motorbike` class represents Harley-Davidson, a renowned motorbike company. The class attribute `company_name` reflects the brand, while the instance attributes (like `model`, `engine_capacity`, and `color`) define the specifics of each motorbike model.

### Object as Specific Motorbike Models:
Each instance of the `Motorbike` class (like `motorbike1` for the Street Glide and `motorbike2` for the Iron 883) represents a specific model produced by Harley-Davidson. Each model has its own unique attributes (e.g., engine capacity and color) while sharing the structure defined by the class.

