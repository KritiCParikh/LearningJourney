## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods and model real-world entities. It helps organize code, making it easier to manage, understand, and reuse.

OOP (Object-Oriented Programming) promotes code reusability, modularity, and scalability, making it easier to manage and understand complex software systems. It increases code reusability and reduces redundancy. Initially, the code was written in a procedural style, then functions were introduced, and finally, the OOP concept was adopted.

# Core Concepts of OOP

- **Encapsulation**
- **Abstraction**
- **Inheritance**
- **Polymorphism**

## 1. Encapsulation

**Explanation**: 
Encapsulation is the practice of hiding the internal details of a class and providing a public interface to interact with the object. A 'capsule' that consists of data and related functions i.e. wrapping data and functions into a single unit (object).
It involves:

- Making data members private.
- Providing public methods (getters and setters) to access and modify the data.
- Controlling access to internal data and methods.

It include improved security, data hiding, and modularity.

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

**Explanation**:
Abstraction = Something that is unclear/ abstruse/ obscure
It involves simplifying complex systems by modeling classes based on the essential properties and behaviors. Hiding the implementation details of a class and only showing the essential features to the user.
It: 

- Hides complex implementation details
- Exposes only relevant features of an object
- Allows focus on what an object does rather than how it does it
- Abstraction is often implemented using abstract classes and interfaces

**Real World Explanation**:
Abstraction is like a car's dashboard. You see the speedometer, fuel gauge, and buttons, but you don’t need to know how the engine works. Abstraction simplifies complex systems by showing only the essentials.

**Example**: In our motorbike example, we can change the color of the motorbike without knowing the details of how that change is managed. The `set_color()` method allows us to interact with the bike without worrying about its internal workings.

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

## 3. Inheritance

**Explanation**:
Inheritance allows a class to inherit properties and methods from another class. It:

- Enables code reuse
- Creates class hierarchies
- Extends the functionality of existing classes

A class that inherits is called a **subclass** or **child class**, while the class being inherited from is the **superclass** or **parent class**.

**Real World Explanation**:
Inheritance is like a family tree. Just as children inherit traits from their parents, classes can inherit properties and behaviors from other classes. This saves time because you don’t have to rewrite the same code.

**Example**: In our motorbike example, the `HarleyDavidson` and `Kawasaki` classes inherit from the `Motorbike` class. They get all the basic features of a motorbike and can add their specific details.

```python
class Motorbike:
    def __init__(self, model, engine_capacity, color):
        self.model = model
        self.engine_capacity = engine_capacity
        self.color = color

    def display_info(self):
        return f"{self.model} - {self.engine_capacity}cc, Color: {self.color}"

# Subclass for Harley-Davidson
class HarleyDavidson(Motorbike):
    company_name = "Harley-Davidson"

    def display_info(self):
        return f"{self.company_name} {self.model} - {self.engine_capacity}cc, Color: {self.color}"

# Subclass for Kawasaki
class Kawasaki(Motorbike):
    company_name = "Kawasaki"

    def display_info(self):
        return f"{self.company_name} {self.model} - {self.engine_capacity}cc, Color: {self.color}"

hd_motorbike = HarleyDavidson("Street Glide", 1753, "Vivid Black")
kawasaki_motorbike = Kawasaki("Ninja 650", 649, "Lime Green")

print(hd_motorbike.display_info())  # Output: Harley-Davidson Street Glide - 1753cc, Color: Vivid Black
print(kawasaki_motorbike.display_info())  # Output: Kawasaki Ninja 650 - 649cc, Color: Lime Green
```
#### This example correctly illustrates inheritance by:
- **Creating a base class**: The `Motorbike` class contains common attributes and methods.
- **Defining subclasses**: The `HarleyDavidson` and `Kawasaki` classes inherit from `Motorbike`, gaining its attributes and methods.
- **Overriding methods [a form of polymorphism]**: Each subclass provides its own implementation of the `display_info()` method to include company-specific information.
- **Using polymorphism**: When `display_info()` is called on objects of these subclasses, their specific versions are executed instead of the one in the `Motorbike` class.

## 4. Polymorphism

**Explanation**:  
"Poly" = Many, "Morphism" = Forms, i.e. Many forms.
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It:

- Enables flexibility in code
- Supports method overriding and overloading
- Allows for dynamic method resolution at runtime

Polymorphism means “many shapes.” It allows methods to do different things based on which object calls them.

**Real World Explanation**:  
- Polymorphism means “many shapes.” It allows methods to do different things based on which object calls them. Imagine different types of bikes having the same button that starts the engine, but each bike has its unique sound when it starts.
- Think of polymorphism like a universal remote control. Just as a single remote can operate different devices (TV, DVD player, etc.) differently, polymorphism allows different classes to define the same method name but with different behaviors.

**Example**: In our motorbike example, both the `HarleyDavidson` and `Kawasaki` classes have a `display_info()` method. When we call this method on different objects, it shows the specific details of that object, even though the method name is the same.

```python
class Motorbike:
    def __init__(self, model, engine_capacity, color):
        self.model = model
        self.engine_capacity = engine_capacity
        self.color = color

    def display_info(self):
        return f"{self.model} - {self.engine_capacity}cc, Color: {self.color}"

# Subclass for Harley-Davidson
class HarleyDavidson(Motorbike):
    company_name = "Harley-Davidson"

    def display_info(self):
        return f"{self.company_name} {self.model} - {self.engine_capacity}cc, Color: {self.color}"

# Subclass for Kawasaki
class Kawasaki(Motorbike):
    company_name = "Kawasaki"

    def display_info(self):
        return f"{self.company_name} {self.model} - {self.engine_capacity}cc, Color: {self.color}"

# Polymorphism in action
def display_motorbike_info(motorbike):
    print(motorbike.display_info())

hd_motorbike = HarleyDavidson("Street Glide", 1753, "Vivid Black")
kawasaki_motorbike = Kawasaki("Ninja 650", 649, "Lime Green")

display_motorbike_info(hd_motorbike)        # Output: Harley-Davidson Street Glide - 1753cc, Color: Vivid Black
display_motorbike_info(kawasaki_motorbike)   # Output: Kawasaki Ninja 650 - 649cc, Color: Lime Green
```
This example illustrates polymorphism by:

- **Using a single function** `display_motorbike_info()` that can work with different types of motorbike objects.
- **Calling the same method** `display_info()` on different objects (`HarleyDavidson` and `Kawasaki`).
- **Showing how the same method call** produces different outputs based on the specific object type.

## Summary

- Classes are blueprints for creating objects.
- Objects are instances of classes.
- Encapsulation keeps data safe from outside interference.
- Inheritance allows for extending classes.
- Polymorphism allows for different classes to be treated as instances of the same class.
- Abstraction hides complex details and exposes only what is necessary.

Reference: Apna College
