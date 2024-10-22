# Classes and Objects in Python

- **Object-Oriented Programming (OOP)** allows us to model real-world objects in code.
- **Objects** are instances of classes, meaning they represent individual examples of the blueprint (class).
- **Classes** act as blueprints to create objects, defining their attributes (data) and methods (functions).

# Defining a Class
- Use the `class` keyword followed by the class name (capitalized by convention).

```python
class Motorbike:
    pass  # Placeholder for now
```

# Attributes and Methods

- **Attributes**: Characteristics of an object (e.g., a motorbike's `make`, `model`, `year`, `color`).
  
- **Methods**: Functions that define what the object can do (e.g., `drive()` and `stop()`).

```python
class Motorbike:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    def drive(self):
        print(f"{self.model} is driving")
        
    def stop(self):
        print(f"{self.model} is stopped")

```
# Constructor
In Python, a class is a blueprint for creating objects, and it can have a special method called a constructor. The constructor is defined by the __init__ method and is automatically called when a new instance (object) of the class is created. This method is used to initialize the object's attributes and set up any necessary state for the object.

## Types of Constructors

In Python, there are two main types of constructors:

## 1. Default Constructor
- A **default constructor** does not take any parameters other than `self`.
- If you do not define a constructor in your class, Python provides a default constructor automatically.
- This default onstructor does not initialize any instance attributes unless explicitly done inside the constructor body.

```python
class Dog:
    def __init__(self):  # Default constructor
        self.name = "Unknown"  # Default attribute value
        self.age = 0

my_dog = Dog()
print(my_dog.name)  # Output: Unknown
```
## 2. Parameterized Constructor
- A **parameterized constructor** takes one or more parameters in addition to `self`.
- This constructor allows you to pass values when creating an instance of the class, enabling the initialization of instance attributes with specific values.

### Example:
```python
class Dog:
    def __init__(self, name, age):  # Parameterized constructor
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

my_dog = Dog("Buddy", 5)  # Creating an instance with specific values
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5
```

# The `__init__()` Method

- `__init__()` is a special method, known as a **constructor**.
- It initializes the object's attributes when the object is created.
- **Self**: Refers to the specific object being created or used. It allows access to the object's attributes and methods within the class.

# Creating an Object

- To create an object from a class, use the class name and provide the necessary attributes:

```python
motorbike1 = Motorbike("Yamaha", "MT-07", 2024, "Black")
```

# Accessing Attributes and Methods

- You can access an object's attributes and methods using the dot (`.`) operator:

```python
print(motorbike1.make)  # Output: Yamaha
motorbike1.drive()       # Output: MT-07 is driving
motorbike1.stop()        # Output: MT-07 is stopped
```
# Self and Method Calls

- You don’t explicitly pass `self` when calling methods. Python automatically passes the object instance.

```python
motorbike1.drive()  # motorbike1 is passed as self
```
# Creating Multiple Objects

- You can create multiple objects from the same class blueprint.

```python
motorbike2 = Motorbike("Suzuki", "Hayabusa", 2023, "Silver")
motorbike2.drive()  # Output: Hayabusa is driving
```

## Class Variables vs. Instance Variables

### Class Attribute:
- **Definition**: A class attribute is a variable that is shared across all instances of the class. It is defined within the class but outside any instance methods.
- **Example**: `company_name` is a class attribute, and all instances of `Motorbike` will have access to this attribute. This means that if you were to change `company_name` to a different value, it would change for all instances.

### Instance Attributes:
- **Definition**: Instance attributes are variables that are specific to each instance of the class. They are defined within the `__init__` method (initializer) and are accessed through the `self` parameter.
- **Example**: `model`, `engine_capacity`, and `color` are instance attributes. Each instance of `Motorbike` can have different values for these attributes. For instance, `motorbike1` has the model "Street Glide" and an engine capacity of 1753cc, while `motorbike2` has the model "Iron 883" and an engine capacity of 883cc.

##### In programming, particularly in object-oriented programming (OOP), the terms **"variables"** and **"attributes"** are often used interchangeably, but they can have distinct meanings depending on the context.

#### Scope:
- Attributes (both class and instance) are associated with a class or an instance, while variables can exist independently.

#### Usage:
- Attributes represent the properties of an object and define its state, whereas variables are more general-purpose and can hold any type of data.

### Note 1: 
In a university setting, think of a Student class where each student has unique names, ages, and majors; these are known as instance attributes because they vary for each student object. For example, one student might be named "Alice" while another is "Bob." However, if we consider a database for a specific university, the university name, such as "University of Texas," remains the same for all students; hence, it's defined as a class attribute. This design choice saves memory, as it avoids duplicating the same university name for every student object, making the code more efficient and organized

### Note 2: 
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

# Classes and Objects with examples

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

Reference: https://www.youtube.com/watch?v=q2SGW2VgwAM
