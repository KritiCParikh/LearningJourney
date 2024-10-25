**Data Structure (DS)** refers to the way we store and organize data in a computer so that it can be used effectively. It is crucial for efficiently processing, retrieving, and storing data. Understanding data structures is fundamental to improving the performance of software applications and solving problems more effectively

#### Example: Motorcycles and Route Optimization
- **Data Structure:** Graphs  
  Example: When planning a motorcycle trip, a graph can represent various routes where nodes are locations and edges are roads with associated distances or travel times.  
- **Algorithm:** Dijkstra’s Algorithm  
  Example: This algorithm can find the shortest path from one location to another, helping riders choose the most efficient route for their journey.

# Data Type vs Data Structures

| **Data Type**                                                                                                                                 | **Data Structure**                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **Definition:** A data type is a classification that specifies which type of value a variable can hold and what operations can be performed on it. | **Definition:** A data structure is a way of organizing and storing data in a computer to enable efficient access and modification. |
| **Example:** <br> Integer (int): Represents whole numbers. <br> `age = 25  # age is an integer`                                            | **Example:** <br> Array: A collection of elements identified by an index. <br> `numbers = [1, 2, 3, 4, 5]  # 'numbers' is an array of integers` |

![image](https://github.com/KritiCParikh/LearningJourney/blob/main/images/2.png)

## 1. Primitive Data Types
Primitive data types are the most basic data types provided by a programming language. They are typically pre-defined and directly supported by the system, meaning they store a single value and cannot be decomposed into simpler elements.

   a. **Integer**  
      - **Definition:** A numeric data type used to represent whole numbers.  
      - **Real-Life Example:** Counting the number of items in a cart. If we have 3 racquets and 2 tennis balls, the total quantity of items (5) would be an integer.

   b. **Float**  
      - **Definition:** A data type used to represent decimal (floating-point) numbers.  
      - **Real-Life Example:** Measuring weights in a grocery store. If we buy 2.5 kg of sugar, the quantity is a float.

   c. **String**  
      - **Definition:** A sequence of characters, used to store text.  
      - **Real-Life Example:** The full name (like "Roger Federer") is a string because it is a sequence of characters.

   d. **Boolean**  
      - **Definition:** A data type that can hold one of two values: True or False.  
      - **Real-Life Example:** A light switch can either be ON (True) or OFF (False).
  
## 2.  Non-Primitive (Derived) Data Types
Non-primitive data types are more complex structures created by combining multiple primitive data types. They are typically not defined by the programming language itself but by the programmer, and they allow for the organization of multiple values.

## (i) Linear Data Structures
Linear data structures organize data in a sequential manner, where each element is connected to its previous and next element. This means that elements are stored in a single level or line.

### A. Static Data Structures
Static data structures have a fixed size and memory allocation that does not change during execution.

a. **Array**
- **Definition**: A collection of elements, typically of the same data type, stored at contiguous memory locations.
- **Real-Life Example**: Seats in a row of a movie theater. All seats are placed in a fixed, ordered sequence. Arrays are used less in Python compared to lists.

### B. Dynamic Data Structures
Dynamic data structures allow for flexible memory allocation, enabling the size to change during program execution.

b. **List**
- **Definition**: An ordered and mutable collection of items that can hold any data type.
- **Real-Life Example**: A grocery shopping list. You have a list of items you plan to buy, like `[milk, eggs, bread]`, and you can add/remove items as you shop.

c. **Stack**
- **Definition**: A collection of elements that follows the Last-In-First-Out (LIFO) principle.
- **Real-Life Example**: A stack of plates. The last plate you place on the stack is the first one you'll take off.

d. **Queue**
- **Definition**: A collection of elements that follows the First-In-First-Out (FIFO) principle.
- **Real-Life Example**: A queue at a ticket counter. The first person in line is the first person served.

e. **Tuple**
- **Definition**: An ordered and immutable collection of items, meaning you can't modify the items after creating it.
- **Real-Life Example**: Coordinates of a location. For example, `(40.7128, -74.0060)` for New York City is a fixed pair of latitude and longitude values.

## (ii) Non-Linear Data Structures
Non-linear data structures organize data in a hierarchical or interconnected manner, where each element can have multiple relationships with other elements. This allows for a more complex arrangement than a linear sequence.

a. **Set**
- **Definition**: An unordered collection of unique elements, where no duplicates are allowed.
- **Real-Life Example**: Collection of unique stamps. You can’t have two of the same stamp in your collection.

b. **Dictionary**
- **Definition**: A collection of key-value pairs, where each key maps to a specific value.
- **Real-Life Example**: A dictionary of words and definitions. The word (key) maps to its meaning (value), just like `{"apple": "a fruit", "car": "a vehicle"}`.

c. **Graph**
- **Definition**: A set of nodes connected by edges, used to represent relationships between elements.
- **Real-Life Example**: A social network. Each person is a node, and friendships or connections are edges linking them to other people.

d. **Tree**
- **Definition**: A hierarchical data structure with a root value and sub-nodes that form a branching structure.
- **Real-Life Example**: A family tree. The root (ancestor) branches out to children (descendants), forming hierarchical layers.

### Summary of Real-Life Comparisons

| Data Structure | Definition                                   | Real-Life Example                     |
|----------------|----------------------------------------------|---------------------------------------|
| Integer        | Whole numbers                                | Counting items in a cart             |
| Float          | Numbers with decimals                        | Measuring weight in kg                |
| String         | A sequence of characters                     | Your name                             |
| Boolean        | True/False values                           | Light switch (ON/OFF)                |
| List           | Ordered, mutable collection                  | Grocery shopping list                 |
| Tuple          | Ordered, immutable collection                | GPS coordinates                       |
| Array          | Mutable collection of elements (less common in Python) | Movie theater seats          |
| Stack          | Last-In-First-Out (LIFO) collection         | Stack of plates                       |
| Queue          | First-In-First-Out (FIFO) collection        | Queue at a ticket counter             |
| Set            | Unordered collection of unique elements      | Unique stamps in a collection         |
| Dictionary     | Key-value pairs                             | Word-definition dictionary            |
| Graph          | Nodes connected by edges                     | Social network connections            |
| Tree           | Hierarchical structure                       | Family tree                           |


References: https://www.youtube.com/watch?v=bum_19loj9A, 
