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

# Types of Constructors in Python

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
## Parameterized Constructor
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
Reference: https://www.youtube.com/watch?v=q2SGW2VgwAM
