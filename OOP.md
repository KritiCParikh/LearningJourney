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

##### In programming, particularly in object-oriented programming (OOP), the terms **"variables"** and **"attributes"** are often used interchangeably, but they can have distinct meanings depending on the context.

##### Note: 
In a university setting, think of a Student class where each student has unique names, ages, and majors; these are known as instance attributes because they vary for each student object. For example, one student might be named "Alice" while another is "Bob." However, if we consider a database for a specific university, the university name, such as "University of Texas," remains the same for all students; hence, it's defined as a class attribute. This design choice saves memory, as it avoids duplicating the same university name for every student object, making the code more efficient and organized.

#### Scope:
- Attributes (both class and instance) are associated with a class or an instance, while variables can exist independently.

##### Usage:
- Attributes represent the properties of an object and define its state, whereas variables are more general-purpose and can hold any type of data.

### Note: 
In Python, **object (or instance) attributes** take precedence over **class attributes** when accessing attribute values. When an attribute is accessed on an object, Python first checks if that attribute exists as an instance attribute for that specific object. If it does, Python uses that value. If the instance attribute does not exist, Python then looks for a class attribute with the same name in the class to which the object belongs. This hierarchy ensures that individual instances can have their own unique values while still benefiting from shared class-level attributes.

```python
class Student:
    university_name = "University of Texas"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

# Creating an instance of the Student class
student1 = Student("Alice")
student2 = Student("Bob")

# Accessing the class attribute through the instance
print(student1.university_name)  # Output: University of Texas
print(student2.university_name)  # Output: University of Texas

# Let's add an instance attribute with the same name
student1.university_name = "Texas A&M"  # Instance attribute takes precedence

# Now, when we access the university_name for student1, it will show the instance attribute
print(student1.university_name)  # Output: Texas A&M
print(student2.university_name)  # Output: University of Texas (still uses the class attribute)
```

# Core Concepts of OOP

- **Encapsulation**
- **Abstraction**
- **Inheritance**
- **Polymorphism**

## 1. Encapsulation

**Explanation**: 
Encapsulation is the practice of hiding the internal details of a class and providing a public interface to interact with the object. It involves:

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
Abstraction involves simplifying complex systems by modeling classes based on the essential properties and behaviors. It: 

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
