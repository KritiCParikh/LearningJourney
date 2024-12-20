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
Encapsulation is like a car's engine compartment. The complex components (engine, battery, fluids) are bundled together and hidden under the hood. We interact with these components through controlled interfaces (ignition, gas pedal, dashboard indicators) without directly accessing the internals.

**Example**: In the `Motorbike` class, attributes like `model`, `engine_capacity`, and `color` are kept private. This means we can't change them directly from outside the class. Instead, we use methods (like `display_info()`) to interact with them.

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
Abstraction = Something that is unclear/ abstruse/ obscure. 
It involves simplifying complex systems by modeling classes based on the essential properties and behaviors. Hiding the implementation details of a class and only showing the essential features to the user.
It: 

- Hides complex implementation details
- Exposes only relevant features of an object
- Allows focus on what an object does rather than how it does it
- Abstraction is often implemented using abstract classes and interfaces

**Real World Explanation**:
Abstraction is like a car's dashboard. We see the speedometer, fuel gauge, and buttons, but we don’t need to know how the engine works. Abstraction simplifies complex systems by showing only the essentials. Also, Abstraction is like using a smartphone's camera app. We press a button to take a photo, and the app handles all the complex processes (focusing, adjusting exposure, processing the image) without we needing to know the details of how these processes work.

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
Inheritance allows a class to inherit properties and methods from another class. 
It:

- Enables code reuse
- Creates class hierarchies
- Extends the functionality of existing classes

A class that inherits is called a **subclass** or **child class**, while the class being inherited from is the **superclass** or **parent class**.

**Real World Explanation**:
Inheritance is like a family tree. Just as children inherit traits from their parents, classes can inherit properties and behaviors from other classes. This saves time because we don’t have to rewrite the same code.

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

### Types of Inheritance:

a. **Single Inheritance**: 
   A class inherits from a single parent class.
   
   **Example**: 
   ```python
   class HarleyDavidson(Motorbike):
       pass
   ```
b. **Multiple Inheritance**:  
A class can inherit from more than one parent class.

**Example**:  
```python
class HybridBike(Motorbike, ElectricVehicle):
    pass
```
c. **Multilevel Inheritanc**e:  
Multilevel inheritance is a type of inheritance where a class derives from another class, which is itself derived from a further class. This forms a **chain of inheritance**, with properties and methods cascading down through multiple levels of the class hierarchy.

In simpler terms, if Class C inherits from Class B, and Class B inherits from Class A, then Class C indirectly inherits the properties and methods of Class A through Class B.

**Example**: 
```python
class MotorVehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Motorbike(MotorVehicle):
    def __init__(self, model, engine_capacity, color):
        super().__init__("Motorbike")
        self.model = model
        self.engine_capacity = engine_capacity
        self.color = color

class HarleyDavidson(Motorbike):
    company_name = "Harley-Davidson"

    def display_info(self):
        return f"{self.company_name} {self.model} - {self.engine_capacity}cc, Color: {self.color}"

hd_motorbike = HarleyDavidson("Street Glide", 1753, "Vivid Black")
print(hd_motorbike.display_info())  # Output: Harley-Davidson Street Glide - 1753cc, Color: Vivid Black
```

d. **Hierarchical Inheritance**:
Multiple classes inherit from the same parent class, where more than one derived class are created from a single base. 

**Example**: 
```python
class Motorbike:
    pass

class HarleyDavidson(Motorbike):
    pass

class Kawasaki(Motorbike):
    pass
```
e. **Hybrid Inheritance**: 
Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

**Example**:
```python
class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1.")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()  # Output: This function is in school.
object.func2()  # Output: This function is in student 1.
```

##### Super Constructor

In Python, the `super()` function allows us to call a method from a parent class. It is commonly used in the context of constructors to ensure that the parent class is initialized properly when creating an instance of a subclass. This helps in maintaining the inheritance chain and ensures that all necessary initializations are performed.

#### Key Points:
- `super()` provides a way to refer to the parent class without explicitly naming it, making our code more maintainable and flexible.
- It can be used to call methods from a parent class, including the constructor (`__init__` method).

#### Example:

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Vehicle created: {self.brand} {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, year):
        # Call the constructor of the parent class
        super().__init__(brand, model)
        self.year = year
        print(f"Car created: {self.brand} {self.model} {self.year}")
```


## 4. Polymorphism

**Explanation**:  
"Poly" = Many, "Morphism" = Forms/ Shapes.
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

# Operator Overloading

Operator overloading is a specific type of polymorphism that allows us to define custom behavior for operators (like +, -, *, etc.) when they are applied to instances of user-defined classes. This enables the same operator to have different meanings depending on the context.

## Operator Overloading with the + Operator

The behavior of the + operator can differ based on the types of the operands involved:

#### Numbers:
For numeric types (integers, floats), the + operator performs arithmetic addition.

```python
a = 5
b = 10
result = a + b  # result is 15
```
#### Strings

For strings, the + operator concatenates them.

```python
str1 = "Hello, "
str2 = "World!"
result = str1 + str2  # result is "Hello, World!"
```

#### Lists

For lists, the + operator combines two lists.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2  # result is [1, 2, 3, 4, 5, 6]
```
In each case, the + operator behaves differently based on the data types of its operands. This is an example of operator overloading in Python.

# Operators and Dunder Functions

Python provides special methods, often referred to as "dunder" methods (double underscore), that allow us to define the behavior of operators for custom classes. These methods are called when the corresponding operator is used.

# Common Operators and Their Methods

| Operator | Method                        |
|----------|-------------------------------|
| +        | `__add__(self, other)`        |
| -        | `__sub__(self, other)`        |
| *        | `__mul__(self, other)`        |
| /        | `__truediv__(self, other)`    |
| ==       | `__eq__(self, other)`         |
| !=       | `__ne__(self, other)`         |
| <        | `__lt__(self, other)`         |
| <=       | `__le__(self, other)`         |
| >        | `__gt__(self, other)`         |
| >=       | `__ge__(self, other)`         |

### Example: Complex Numbers

Python does not have a built-in class for complex numbers in the way that allows us to overload operators directly. Therefore, we can create a custom `Complex` class to represent complex numbers and implement operator overloading for them.

```python
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

# Example Usage
num1 = Complex(2, 4)
num1.showNumber()  # Output: 2 i + 4 j

num2 = Complex(3, 5)
num2.showNumber()  # Output: 3 i + 5 j

num3 = num1 + num2  # Calls num1.__add__(num2)
num3.showNumber()  # Output: 5 i + 9 j
```

## Summary

- Classes are blueprints for creating objects.
- Objects are instances of classes.
- Encapsulation keeps data safe from outside interference.
- Abstraction hides complex details and exposes only what is necessary.
- Inheritance allows for extending classes.
- Polymorphism allows for different classes to be treated as instances of the same class.

![image](https://github.com/KritiCParikh/LearningJourney/blob/main/images/1_.png)

References: Apna College, https://www.geeksforgeeks.org/types-of-inheritance-python/, https://www.youtube.com/watch?v=Ei2zOVYIyKE 
