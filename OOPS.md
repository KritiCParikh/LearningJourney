## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods and model real-world entities. It helps organize code, making it easier to manage, understand, and reuse.

OOP (Object-Oriented Programming) promotes code reusability, modularity, and scalability, making it easier to manage and understand complex software systems. It increases code reusability and reduces redundancy. Initially, the code was written in a procedural style, then functions were introduced, and finally, the OOP concept was adopted.

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

```python
# Creating objects of the Motorbike class
motorbike1 = Motorbike("Street Glide", 1753, "Vivid Black")  
motorbike2 = Motorbike("Iron 883", 883, "River Rock Gray")

# Accessing properties and methods of the objects
print(motorbike1.display_info())  # Output: Harley-Davidson Street Glide - 1753cc, Color: Vivid Black
print(motorbike2.display_info())  # Output: Harley-Davidson Iron 883 - 883cc, Color: River Rock Gray
```
## Explanation

### Class as a Motorbike Company:
The `Motorbike` class represents Harley-Davidson, a renowned motorbike company. The class attribute `company_name` reflects the brand, while the instance attributes (like `model`, `engine_capacity`, and `color`) define the specifics of each motorbike model.

### Object as Specific Motorbike Models:
Each instance of the `Motorbike` class (like `motorbike1` for the Street Glide and `motorbike2` for the Iron 883) represents a specific model produced by Harley-Davidson. Each model has its own unique attributes (e.g., engine capacity and color) while sharing the structure defined by the class.

## Class Variables vs. Instance Variables

### Class Attribute:
- **Definition**: A class attribute is a variable that is shared across all instances of the class. It is defined within the class but outside any instance methods.
- **Example**: `company_name` is a class attribute, and all instances of `Motorbike` will have access to this attribute. This means that if you were to change `company_name` to a different value, it would change for all instances.

### Instance Attributes:
- **Definition**: Instance attributes are variables that are specific to each instance of the class. They are defined within the `__init__` method (initializer) and are accessed through the `self` parameter.
- **Example**: `model`, `engine_capacity`, and `color` are instance attributes. Each instance of `Motorbike` can have different values for these attributes. For instance, `motorbike1` has the model "Street Glide" and an engine capacity of 1753cc, while `motorbike2` has the model "Iron 883" and an engine capacity of 883cc.

# Core Concepts of OOP

- **Encapsulation**
- **Abstraction**
- **Inheritance**
- **Polymorphism**

# 1. Encapsulation

**Explanation**: 
Encapsulation is the practice of hiding the internal details of a class and providing a public interface to interact with the object. It involves:

- Making data members private.
- Providing public methods (getters and setters) to access and modify the data.
- Controlling access to internal data and methods.

**Benefits** include improved security, data hiding, and modularity.

**Real World Explanation**: 
Think of encapsulation as putting your motorbike’s engine, wheels, and seat inside a protective cover. You can ride the bike without needing to know how each part works. Encapsulation keeps the details hidden and only allows you to interact with what you need.

**Example**: In the `Motorbike` class, attributes like `model`, `engine_capacity`, and `color` are kept private. This means you can't change them directly from outside the class. Instead, you use methods (like `display_info()`) to interact with them.

```python
class Motorbike:
    def __init__(self, model, engine_capacity, color):
        self.__model = model           # Private attribute
        self.__engine_capacity = engine_capacity  # Private attribute
        self.__color = color           # Private attribute

    # Public method to get motorbike details
    def display_info(self):
        return f"{self.__model} - {self.__engine_capacity}cc, Color: {self.__color}"

motorbike1 = Motorbike("Street Glide", 1753, "Vivid Black")
print(motorbike1.display_info())  # Output: Street Glide - 1753cc, Color: Vivid Black.
```
#### Attributes are marked as private using double underscores (__). The display_info() method provides controlled access to the private attributes.

## 2. Abstraction

### Explanation:
Abstraction involves simplifying complex systems by modeling classes based on the essential properties and behaviors. It:
- Hides complex implementation details
- Exposes only relevant features of an object
- Allows focus on what an object does rather than how it does it
- Abstraction is often implemented using abstract classes and interfaces

### Real-world Explanation:
**Simple Explanation**: Abstraction is like a car's dashboard. You see the speedometer, fuel gauge, and buttons, but you don’t need to know how the engine works. Abstraction simplifies complex systems by showing only the essentials.

### Example:
In our motorbike example, we can change the color of the motorbike without knowing the details of how that change is managed. The `set_color()` method allows us to interact with the bike without worrying about its internal workings.

```python
class Motorbike:
    def __init__(self, model, engine_capacity, color):
        self.__model = model
        self.__engine_capacity = engine_capacity
        self.__color = color

    # Public method to set new color
    def set_color(self, color):
        self.__color = color

    # Public method to get motorbike details
    def display_info(self):
        return f"{self.__model} - {self.__engine_capacity}cc, Color: {self.__color}"

motorbike1 = Motorbike("Street Glide", 1753, "Vivid Black")
motorbike1.set_color("Midnight Blue")  # Changing color using an abstracted method
print(motorbike1.display_info())  # Output: Street Glide - 1753cc, Color: Midnight Blue
```
#### This example correctly illustrates abstraction by:
- **Hiding internal details**: The attributes are private (denoted by double underscores).
- **Providing public methods**: `set_color()` and `display_info()` allow interaction with the object without exposing its internals.
- **Simplifying interaction**: Users can change the color without knowing how it's implemented internally.












## Summary

- Classes are blueprints for creating objects.
- Objects are instances of classes.
- Encapsulation keeps data safe from outside interference.
- Inheritance allows for extending classes.
- Polymorphism allows for different classes to be treated as instances of the same class.
- Abstraction hides complex details and exposes only what is necessary.
