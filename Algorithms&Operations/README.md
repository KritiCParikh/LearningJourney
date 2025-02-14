# Algorithms and Operations

Algorithms and operations are the heart of computer science, working hand-in-hand with data structures to solve problems efficiently. While data structures focus on organizing and storing data, algorithms provide step-by-step procedures for manipulating this data to achieve specific goals.

## Algorithms on Data Structures

Algorithms are precise, unambiguous sequences of instructions designed to solve a problem or perform a task. They are the recipes of the programming world, detailing how to accomplish various operations on data structures. Just as a recipe outlines the ingredients and steps to prepare a dish, an algorithm outlines the inputs, operations, and outputs required to achieve a desired outcome.

#### Example: Motorcycle Maintenance Scheduling

**Scenario**: We own a motorcycle and want to ensure it runs smoothly by performing regular maintenance. We can create an algorithm to manage our maintenance schedule based on usage patterns.

#### 1. Data Structure
**Maintenance Log**: A data structure to store maintenance records might look like this:

| Date       | Maintenance Type     | Mileage | Notes               |
|------------|----------------------|---------|---------------------|
| 2024-01-15 | Oil Change           | 5000    | Changed oil filter  |
| 2024-05-10 | Tire Inspection      | 10000   | Tires in good shape |
| 2024-09-01 | Brake Pad Replacement | 15000   | Replaced front pads |

#### 2. Algorithm
**Maintenance Scheduling Algorithm**:
a. **Input**: Current mileage, last maintenance date, and type of maintenance.
b. **Operations**:
   - Check current mileage against predefined intervals for maintenance (e.g., oil change every 3,000 miles, tire inspection every 5,000 miles).
   - If a maintenance task is due:
     - Schedule it for the next available date.
     - Record the date and type of maintenance in the Maintenance Log.
     - Notify the owner about the upcoming maintenance.
c. **Output**: An updated maintenance schedule with due tasks.

#### 3. Example of the Algorithm in Action
```plaintext
1. Current Mileage: 6000
2. Last Maintenance Date: 2024-01-15
3. Maintenance Due:
   - Oil Change (due at 9000 miles)
   - Tire Inspection (due at 10000 miles)
4. Notify owner: "Next maintenance due is an oil change at 9000 miles."
```
##### Summary

In this example, the data structure (Maintenance Log) organizes important maintenance records, while the algorithm provides a systematic way to manage and schedule motorcycle maintenance based on usage. This approach helps ensure that the motorcycle remains in optimal condition, enhancing its performance and longevity.

## Operations on Data Structures:
Operations are the basic actions performed on data structures to manipulate and manage the data they hold. Data structures support a variety of operations, which enable storing, modifying, and retrieving data effectively. Here’s a summary of key operations typically performed on data structures:

| **Operation**           | **Purpose**                                                                 | **Applications**                                                | **Used In**                                      | **Considerations**                                                                                                                                                              |
|-------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Insertion**           | Adds a new element to the data structure.                                  | Building lists, queues, trees, etc.                             | Lists, arrays, linked lists, stacks, queues, trees, hash tables | Efficient in linked lists; array insertion may require shifting elements.                                                                                                       |
| **Deletion**            | Removes an element from the data structure.                                | Data processing, memory management                              | Arrays, linked lists, stacks, queues, trees, hash tables       | Arrays need shifting elements, while linked lists allow more flexible deletion.                                                                                                 |
| **Traversal**           | Visits each element for access or operations.                              | Displaying, searching, updating data                            | Arrays, linked lists, trees, graphs              | Linear traversal is simpler; trees and graphs may require DFS or BFS algorithms.                                                                                                |
| **Searching**           | Finds a particular element.                                                | Quick data retrieval, file searches                             | Arrays, lists, trees, hash tables                | Linear or binary search depends on data structure and search requirements.                                                                                                     |
| **Sorting**             | Arranges elements in a particular order.                                   | Enhances search efficiency, supports analysis                   | Arrays, lists, heaps                            | Different sorting algorithms (e.g., quicksort, mergesort) optimize for various cases.                                                                                          |
| **Access**              | Retrieves an element from a specific position.                             | Retrieving stored data                                          | Arrays, lists, hash tables                      | Arrays allow direct access, but linked lists may need traversal to reach a position.                                                                                            |
| **Updating**            | Modifies the value of an element.                                          | Dynamic data applications like record updates                   | Arrays, lists, hash tables                      | Directly updating is efficient; linked lists may require traversal to locate elements.                                                                                          |
| **Merging**             | Combines two or more data structures.                                      | Joining datasets, merging sorted lists                          | Arrays, lists, trees                            | Straightforward in arrays/lists; trees need special handling for structure preservation.                                                                                        |
| **Splitting**           | Divides a data structure into smaller parts.                               | Distributed processing, dividing tasks                          | Arrays, lists, trees, graphs                    | Splitting requires identifying division points, simpler in linear structures.                                                                                                   |
| **Searching (Keyed)**   | Finds elements based on unique key/identifier.                             | Database queries, dictionary lookups                            | Hash tables, dictionaries, maps                 | Keyed search is efficient, but hash collisions need management in hash tables.                                                                                                 |
| **Balancing**           | Maintains optimal structure for efficient operations.                      | Keeps structures efficient, especially in trees                 | Trees (e.g., AVL, Red-Black), heaps             | Adds overhead but improves search efficiency significantly.                                                                                                                     |
| **Hashing**             | Maps keys to specific locations for retrieval.                             | Cache storage, efficient lookup operations                      | Hash tables, maps                              | Hash functions should minimize collisions to ensure efficiency.                                                                                                                 |
| **Enqueue/Dequeue**     | Adds or removes elements in FIFO order.                                    | Task scheduling, buffering                                      | Queues, deques                                 | Enqueue adds to back, dequeue removes from front, circular queues add efficiency.                                                                                              |
| **Push/Pop**            | Adds or removes elements in LIFO order.                                    | Browser history, undo operations                                | Stacks                                         | Push adds to top, pop removes last-added item.                                                                                                                                |
| **Connecting/Linking**  | Establishes relationships between elements.                                | Graph node/edge linking, linked list node linking               | Graphs, linked lists                           | Linking enables non-linear relationships but can complicate traversal.                                                                                                         |
| **Min/Max Retrieval**   | Finds smallest or largest element.                                         | Priority-based applications, priority queues                    | Heaps, arrays, trees                           | Constant time retrieval in heaps; requires traversal in arrays.                                                                                                                |
| **Pathfinding**         | Identifies a route between connected elements.                             | Routing, AI navigation, network design                          | Graphs, trees                                  | Pathfinding algorithms (Dijkstra, A*) efficiently find routes in complex structures.                                                                                            |
| **Aggregating**         | Computes a single value from multiple elements (e.g., sum, average).       | Statistical analysis, reporting                                 | Arrays, lists, trees, graphs                   | Aggregating may require full traversal but can be optimized in trees.                                                                                                          |

## Complexity Analysis
Complexity analysis is a technique used to understand how efficient an algorithm is, in terms of both **time** (speed) and **space** (memory) as the size of input data grows. It helps determine if an algorithm can handle large datasets effectively.

**Why It Matters:**  
Just like we'd compare travel routes to find the quickest path, complexity analysis compares algorithms to find the most efficient solution for a problem. This is crucial in software development, as it directly impacts the performance and scalability of applications.

# Time Complexity
Time complexity is a measure of how the execution time of an algorithm increases as the input size grows. It quantifies the amount of time taken by an algorithm to run as a function of the length of the input.

## Asymptotic analysis
Asymptotic analysis refers to the mathematical method of describing the limiting behavior of a function as the input size approaches infinity. In algorithm analysis, it's used to describe how the runtime or space requirements of an algorithm grow as the input size increases.

### Notations

#### Big O (O) - Upper Bound
Represents the worst-case scenario or upper bound of an algorithm's growth rate.
- **Purpose:** Most commonly used in practice for analyzing algorithms. This notation helps identify the maximum time the algorithm might need for a given input size.
- **Example:** `O(n)` means the algorithm's time complexity grows at most linearly with input size.

#### Big Theta (Θ) - Tight Bound
Represents both the upper and lower bounds of an algorithm's growth rate.
- **Purpose:** Describes the average-case or exact behavior of an algorithm. This is often less emphasized but useful when an average scenario is meaningful.
- **Example:** `Θ(n)` means the algorithm's time complexity grows exactly linearly with input size.

#### Big Omega (Ω) - Lower Bound
Represents the best-case scenario or lower bound of an algorithm's growth rate.
- **Purpose:** Less commonly used in practical analysis, but it helps understand the minimum time an algorithm will take.
- **Example:** `Ω(n)` means the algorithm's time complexity grows at least linearly with input size.

#### Why Worst-Case Matters
Worst-case analysis is essential in assessing the reliability and performance of algorithms in real-world applications. It ensures that developers have a predictable upper limit on the time the algorithm will take, which is critical for applications where response time and performance are important.

### Road Trip Analogy for Time Complexity Notations

Imagine we're planning a road trip from New York to Los Angeles:

#### Big O (O) - Upper Bound (Worst-Case Scenario)
- **Analogy:** The longest time it could possibly take us to complete the trip.
- **Real-world factors:**
  - Heavy traffic in every city
  - Multiple car breakdowns
  - Severe weather conditions
  - Extensive road construction
  - Getting lost several times
- **Example:** "We'll arrive in no more than 7 days (168 hours)."

#### Big Theta (Θ) - Tight Bound (Average-Case Scenario)
- **Analogy:** Our typical travel time under normal conditions.
- **Real-world factors:**
  - Average traffic
  - Normal weather
  - Usual rest stops
  - No major incidents
- **Example:** "The trip typically takes about 4-5 days (96-120 hours)."

#### Big Omega (Ω) - Lower Bound (Best-Case Scenario)
- **Analogy:** The minimum time it could take to reach our destination.
- **Real-world factors:**
  - No traffic at all
  - Perfect weather conditions
  - Non-stop driving (multiple drivers)
  - No construction or detours
  - Optimal route with no mistakes
- **Example:** "The fastest we could possibly make it is 2 days (48 hours)."

## Big O Notation

Big O Notation is the standard way to express algorithm complexity. It describes the upper bound of an algorithm's growth rate. 

![image](https://github.com/KritiCParikh/LearningJourney/blob/main/images/6.png)

Common notations include:

### O(1): Constant Time
The algorithm's execution time remains constant regardless of the input size.
- **Real-world example:** Checking if a light switch is on or off. No matter how big our house is (input size), it takes the same amount of time to check a single switch.

### O(log n): Logarithmic Time
The algorithm's execution time increases logarithmically as the input size grows.
- **Real-world example:** Finding a word in a dictionary. We can use a binary search approach, halving the section we're looking in each time, which is much faster than checking every page.

### O(n): Linear Time
The algorithm's execution time increases linearly with the input size.
- **Real-world example:** Reading a book. The time it takes to read a book is directly proportional to the number of pages (input size).

### O(n log n): Linearithmic Time
The algorithm's execution time is a product of linear and logarithmic factors.
- **Real-world example:** Sorting a deck of cards using an efficient method like merge sort. We divide the deck into smaller piles (logarithmic) and then compare and merge them (linear).

### O(n²): Quadratic Time
The algorithm's execution time is proportional to the square of the input size.
- **Real-world example:** Checking every pair of socks in a drawer to find matching pairs. If we have *n* socks, we need to compare each sock with every other sock, resulting in *n²* comparisons.

### O(2ⁿ): Exponential Time
The algorithm's execution time doubles with each additional input element.
- **Real-world example:** Trying to crack a password by brute force. Each additional character in the password doubles the number of possible combinations to check.

### O(n!): Factorial Time
The algorithm's execution time grows factorially with the input size.
- **Real-world example:** Solving the traveling salesman problem by checking every possible route. For *n* cities, there are *n!* possible routes to consider, which grows extremely quickly as *n* increases.

### Important Points to Calculate Big O Notation

1. **Different Steps Get Added:**
   - When an algorithm has multiple independent steps, their complexities are added together.
   - **Example**: If one step is \(O(n)\) and another is \(O(m)\), the total complexity is \(O(n + m)\).

2. **Drop Constants:**
   - In Big O notation, constants are ignored because they don't significantly affect the growth rate.
   - **Example**: \(O(2n)\) simplifies to \(O(n)\).

3. **Different Inputs Mean Different Variables:**
   - If an algorithm takes multiple inputs, each input should be represented by a different variable.
   - **Example**: If an algorithm processes two arrays of sizes \(n\) and \(m\), its complexity might be expressed as \(O(n + m)\).

4. **Drop Non-Dominant Terms:**
   - Focus on the term with the highest growth rate and drop others.
   - **Example**: \(O(n^2 + n)\) simplifies to \(O(n^2)\).

![image](https://github.com/KritiCParikh/LearningJourney/blob/main/images/5.png)

## Alternative Big O Notation Meme

This meme humorously reinterprets Big O notation, commonly used in computer science to describe algorithmic efficiency, by associating each complexity with relatable reactions.

| Big O Notation | Interpretation      | Reaction      | Insights      |
|-----------------|---------------------|---------------|---------------|
| O(1)            | Constant time       | O(yeah)       |  Fast and ideal; exciting; best.  |            
| O(log n)       | Logarithmic time    | O(nice)       |  Efficient; positive reaction; good.  |
| O(n)            | Linear time         | O(ok)         |  Acceptable; mild approval; fair. |
| O(n²)           | Quadratic time      | O(my)         |  Concern; not ideal for large inputs.|
| O(n log n)     | Log-linear time     | O(why?)       | Confusion; better than quadratic but worse than linear; bad.  |
| O(2ⁿ)           | Exponential time    | O(no)         | Dread; undesirable for large data. |
| O(n!)           | Factorial time      | O(mg!)        | Shock; impractical for large inputs; worst. |

![image](https://github.com/KritiCParikh/LearningJourney/blob/main/images/3.png)

# Summary of Time Complexities for Common Data Structures

| **Data Structure**          | **Access**                          | **Search**                          | **Insertion**                                         | **Deletion**                                         |
|-----------------------------|-------------------------------------|-------------------------------------|------------------------------------------------------|-----------------------------------------------------|
| **Array**                   | O(1)                               | O(n)                               | O(n)                                                | O(n)                                               |
| **Stack**                   | O(n)                               | O(n)                               | O(1) (Push)                                        | O(1) (Pop)                                        |
| **Queue**                   | O(n)                               | O(n)                               | O(1) (Enqueue)                                    | O(1) (Dequeue)                                    |
| **Singly Linked List**      | O(n)                               | O(n)                               | O(1) (at the beginning), O(n) (at the end or middle) | O(1) (at the beginning), O(n) (at the end or middle) |
| **Doubly Linked List**      | O(n)                               | O(n)                               | O(1)                                               | O(1)                                               |
| **Hash Table**              | N/A                                | O(1) average, O(n) worst case     | O(1) average, O(n) worst case                      | O(1) average, O(n) worst case                      |
| **Binary Search Tree (BST)**| O(log n) average, O(n) worst case | O(log n) average, O(n) worst case | O(log n) average, O(n) worst case                  | O(log n) average, O(n) worst case                  |
| **AVL Tree**                | O(log n)                           | O(log n)                           | O(log n)                                           | O(log n)                                           |
| **Red-Black Tree**          | O(log n)                           | O(log n)                           | O(log n)                                           | O(log n)                                           |

These time complexities represent the average or typical case for each operation. The actual performance may vary depending on specific implementations and use cases.


## Space Complexity
Space complexity is the amount of memory space required by an algorithm to solve a computational problem, expressed as a function of the input size.

### Example
Think of packing for a trip. If we need an outfit for every possible activity, our luggage quickly fills up (high space complexity). If we can reuse outfits (low space complexity), we pack more efficiently.

### Components

- **Input Space**: Memory used by the input data.
- **Auxiliary Space**: Extra or temporary space used by the algorithm.
- **Total Space Complexity** = Input Space + Auxiliary Space

### Types of Space Complexity

#### Constant Space - O(1)
- **Description**: Fixed amount of memory used, regardless of the input size.
- **Example**: Simple calculations or accessing a single element in an array.

#### Linear Space - O(n)
- **Description**: Memory usage grows linearly with the input size.
- **Example**: Creating a new array of size n to store results.

#### Logarithmic Space - O(log n)
- **Description**: Memory usage grows logarithmically with the input size.
- **Example**: Some divide-and-conquer algorithms, like binary search, may use log space for recursive calls.

#### Linearithmic Space - O(n log n)
- **Description**: Memory usage grows in proportion to n times the logarithm of n.
- **Example**: Algorithms like merge sort can require O(n log n) space for auxiliary storage during sorting.

#### Quadratic Space - O(n²)
- **Description**: Memory usage grows quadratically with the input size.
- **Example**: Creating a 2D array of size n x n.

#### Cubic Space - O(n³)
- **Description**: Memory usage grows cubically with the input size.
- **Example**: Used in some algorithms dealing with 3D matrices or multi-dimensional data structures.

#### Exponential Space - O(2^n)
- **Description**: Memory usage doubles with each increase in input size.
- **Example**: Recursive algorithms that generate all subsets of a set or explore all possible configurations.

#### Factorial Space - O(n!)
- **Description**: Memory usage grows factorially with the input size.
- **Example**: Algorithms that generate all permutations of a set require O(n!) space to store each permutation.

# Algorithmic Techniques
![image](https://github.com/KritiCParikh/LearningJourney/blob/main/images/4.png)

## A. General Algorithmic Techniques

### 1. Brute Force
A straightforward method of solving problems by checking all possible solutions until the correct one is found.

**Example:**
- a. Finding a lost key by systematically searching every room in the house, checking under every cushion and in every drawer until it's found.
- b. Cracking a 4-digit PIN by trying all 10,000 possible combinations from 0000 to 9999.

**Types**
- **Exhaustive Search:** Systematically enumerating all potential candidates for the solution.
- **Generate and Test:** Creating possible solutions and checking their validity.
- **Iterative Brute Force:** Solving problems by trying all possibilities in a loop.


### 2. Divide and Conquer
Breaking down a large problem into smaller sub-problems, solving them independently, and combining the results.

**Example:**
- a. Organizing a large community cleanup. We divide the town into sectors, assign teams to clean each sector independently, and then combine their efforts for a clean town.
- b. Merge Sort algorithm, which recursively divides an array in half, sorts each half, and then merges the sorted halves.

**Types**
- **Binary Search:** Efficiently finding an item in a sorted list by repeatedly dividing the search interval in half.
- **Merge Sort:** Sorting by dividing the list, sorting the halves, and then merging them.
- **Quick Sort:** Sorting by selecting a 'pivot' element and partitioning the other elements into two sub-arrays.
- **Strassen's Matrix Multiplication:** Efficiently multiplying large matrices by breaking them into sub-matrices.

### 3. Dynamic Programming (DP)
Breaking down a problem into overlapping sub-problems and solving each just once, storing the results for future use.

**Example:**
- a. Planning the most scenic route for a road trip. We calculate the best routes between major cities once, then use these calculations to determine the best overall route, avoiding recalculating the same city-to-city routes multiple times.
- b. Calculating Fibonacci numbers: Instead of recalculating Fib(n−1) and Fib(n−2) for each Fib(n), dynamic programming stores these values, significantly reducing computation time.

**Types**
- **Top-down (Memoization):** Solving the problem recursively and caching the results.
- **Bottom-up (Tabulation):** Solving the problem iteratively by building up from the base case.

### 4. Greedy Approach
Making the best immediate choice at each step, hoping to reach the global optimal solution at the end.

**Example:** Filling a piggy bank with coins, always choosing to put in the highest value coin that will fit, to maximize the total amount saved.

**Types**
- **Selection Sort:** Repeatedly selecting the smallest element from the unsorted portion.
- **Huffman Coding:** Creating optimal prefix codes for data compression.
- **Dijkstra's Algorithm:** Finding the shortest path in a weighted graph.
- **Kruskal's Algorithm:** Finding a minimum spanning tree for a weighted graph.


### 5. Backtracking
A technique for solving problems incrementally, trying partial solutions and abandoning them if they do not lead to a valid solution.

**Example:** Solving a crossword puzzle by filling in words, erasing and trying new words when we reach a point where no word fits.

**Types**
- **Depth-First Search (DFS):** Exploring as far as possible along each branch before backtracking.
- **N-Queens Problem:** Placing N chess queens on an N×N chessboard so that no two queens threaten each other.
- **Sudoku Solver:** Filling a 9×9 grid with digits so each column, row, and 3×3 section contain all digits from 1 to 9.
- **Hamiltonian Cycle Problem:** Finding a cycle that visits every vertex exactly once in a graph.

### 6. Branch and Bound
A method for solving optimization problems by dividing the search space into smaller sections and using bounds to eliminate regions from consideration.

**Example:** House hunting within a budget. We divide the city into neighborhoods, set price limits, and eliminate entire areas that are over our budget without visiting every single house.

**Types**
- **Traveling Salesman Problem:** Finding the shortest possible route that visits each city exactly once and returns to the origin city.
- **0/1 Knapsack Problem:** Selecting items to maximize value while staying within a weight limit.
- **Job Assignment Problem:** Assigning jobs to workers to minimize total cost.


### 7. Recursion
A method where a function calls itself to solve smaller instances of the same problem, often with a base case to stop the recursion.

**Example:** Understanding a family tree. To know about our ancestors, we ask our parents about their parents, who in turn asked their parents, and so on, until we reach someone who doesn't know their parents' history.

**Types**
- **Linear Recursion:** A function calls itself once in its body.
- **Tail Recursion:** The recursive call is the last operation in the function.
- **Binary Recursion:** A function calls itself twice in its body.
- **Nested Recursion:** A function passes the result of a recursive call as an argument to another recursive call.


### 8. Heuristic Approaches
Techniques designed for solving problems faster when classic methods are too slow, often using rule-of-thumb strategies.

**Example:** Choosing a restaurant in a new city. Instead of trying every restaurant, we might use heuristics like "busy restaurants are usually good" or "places with good online reviews are worth trying."

**Types**
- **Hill Climbing:** Iteratively making small changes to improve a solution.
- **Simulated Annealing:** Probabilistically accepting worse solutions to escape local optima.
- **Genetic Algorithms:** Evolving a population of solutions using principles inspired by natural selection.
- **A* Search Algorithm:** Finding the shortest path using an estimate of the remaining distance.

### 9. Randomized Algorithms
Uses randomness to make decisions, often leading to faster average-case performance.

**Example:** Conducting a political poll. Instead of asking every citizen, we randomly select a smaller group to survey, which can provide a good estimate of overall opinion.

**Types**
- **Las Vegas Algorithms:** Always produce the correct result, with running time varying randomly.
- **Monte Carlo Algorithms:** May produce an incorrect result with a small probability.
- **Randomized Quicksort:** Using a random pivot for partitioning in quicksort.
- **Karger's Algorithm:** Finding the minimum cut of a graph using random contractions.

## B. Algorithms and Techniques for Data Structures

### Primitive Data Types
- **Integer, Float, Boolean**
  - Basic arithmetic operations: Fundamental mathematical calculations
  - Comparison operations: Evaluating relative values
  - Bitwise operations (for integers): Manipulating individual bits
  - Type conversion operations: Changing data types

#### String
- **String operations**
  - String concatenation: Combining strings
  - Substring search (KMP, Boyer-Moore): Efficiently finding patterns in text
  - String matching (Rabin-Karp): Identifying substrings using hashing
  - String reversal: Inverting character order
  - Regular expression matching: Pattern matching using regex

### Non-Primitive Data Types

#### Tuple
- Indexing and slicing: Accessing elements or ranges
- Tuple packing and unpacking: Creating or separating tuples

#### Array
- Linear search: Sequentially checking each element
- Binary search (for sorted arrays): Efficiently finding elements by halving search space
- Array reversal: Inverting element order
- Array rotation: Shifting elements circularly
- In-place operations: Modifying array without extra space
- Two pointers techniques: Using two indices to solve problems
- Sliding window techniques: Processing subarrays efficiently
- Kadane's algorithm: Finding maximum subarray sum
- Dutch National Flag algorithm: Three-way partitioning
- Tabulation in dynamic programming: Solving complex problems by breaking them down
- Prefix and Suffix Sum technique: Precomputing cumulative sums for quick range queries

#### List
- Insertion and deletion at any position: Modifying list elements
- Linear search: Sequentially finding elements
- List comprehension: Concise way to create lists

#### Linked List
- Insertion/Deletion (at beginning, end, or middle): Modifying list structure
- Traversal: Visiting all nodes
- Reversal: Inverting node order
- Cycle detection (Floyd's Cycle-Finding Algorithm): Finding loops in linked lists
- Merging two sorted linked lists: Combining ordered lists
- Two pointers for finding middle element: Efficient middle node detection

#### Stack
- Push/Pop/Peek operations: Basic stack manipulations
- Infix to postfix conversion: Changing expression notation
- Postfix expression evaluation: Calculating expression results
- Parenthesis matching: Checking for balanced brackets
- Implementing function call stack: Simulating program execution
- Implement queue using stacks: Stack-based queue implementation

#### Queue
- Enqueue/Dequeue operations: Basic queue manipulations
- Front and Rear operations: Accessing queue ends
- Implementing Breadth-First Search: Level-order graph traversal
- Implement stack using queues: Queue-based stack implementation
- Sliding window maximum using deque: Efficient max-value tracking
- Circular buffer implementation: Fixed-size queue with wraparound

#### Set
- Union, Intersection, Difference operations: Set theory operations
- Subset and Superset checks: Verifying set relationships
- Element addition and removal: Modifying set contents

#### Dictionary (Hash Table)
- Insertion, deletion, and lookup operations: Basic hash table manipulations
- Hash function design: Creating efficient key-to-index mappings
- Collision resolution: Handling key conflicts
- Resizing and rehashing: Maintaining performance as size changes
- Two Sum problem: Finding pairs with a given sum
- Perfect hashing: Collision-free hash table design

#### Graph
- Depth-First Search (DFS): Exploring as far as possible along branches
- Breadth-First Search (BFS): Exploring all neighbor nodes first
- Shortest path algorithms (e.g., Dijkstra's, Bellman-Ford): Finding optimal routes between nodes
- Minimum Spanning Tree algorithms: Finding connecting subgraphs with minimum weight
- Topological Sorting: Ordering nodes based on dependencies
- Strongly Connected Components: Finding mutually reachable node groups
- Floyd-Warshall algorithm: All-pairs shortest path
- A* search algorithm: Informed search in weighted graphs
- Maximum flow algorithms: Optimizing network flow

#### Tree
- Tree traversals: Visiting nodes in specific orders
- Level-order traversal: Visiting nodes level by level
- Insertion and deletion in Binary Search Tree: Maintaining ordered tree structure while adding or removing nodes
- Balancing algorithms: Keeping tree height minimal
- Trie operations: Efficient string storage and retrieval
- Lowest Common Ancestor: Finding shared ancestors of nodes
- Segment Trees: Range query and update operations
- Fenwick Trees: Efficient prefix sum computations
- B-trees and B+ trees: Self-balancing tree data structures

#### Heap
- Heapify operation: Creating a heap from an array
- Insertion and deletion: Maintaining heap property
- Heap Sort: Sorting using heap data structure
- Priority Queue implementation: Efficient highest-priority element access
- K-way merge using heaps: Combining multiple sorted sequences

### Additional Techniques  
These techniques are widely applicable across various data structures and problem types, enhancing efficiency and problem-solving capabilities.  

#### 1. Sliding Window  
- **Fixed-size window** – Processes fixed-length subarrays efficiently.  
- **Variable-size window** – Adjusts the subarray size dynamically based on conditions.  

#### 2. Sorting Algorithms  

###### - Comparison-based Sorting  

###### Simple Sorting Algorithms  
- **Bubble Sort** – Repeatedly swaps adjacent elements if they are in the wrong order.  
- **Selection Sort** – Selects the smallest element and swaps it into its correct position.  
- **Insertion Sort** – Builds a sorted array by inserting elements one by one into their correct position.  

###### Efficient Sorting Algorithms  
- **Merge Sort** – A divide-and-conquer algorithm that splits the array, sorts each half, and merges them.  
- **Quick Sort** – Selects a pivot, partitions the array, and recursively sorts subarrays.  
- **Heap Sort** – Utilizes a binary heap to repeatedly extract the minimum or maximum element.  

###### - Non-comparison Sorting  
- **Counting Sort** – Counts occurrences of each element and places them in the correct position.  
- **Radix Sort** – Sorts numbers digit by digit using a stable sorting algorithm like Counting Sort.  
- **Bucket Sort** – Distributes elements into multiple buckets and sorts each bucket individually.  

###### Hybrid Sorting Algorithms  
- **Timsort** – A hybrid of Merge Sort and Insertion Sort, optimized for real-world data.  
- **Introsort** – A combination of Quick Sort, Heap Sort, and Insertion Sort, switching strategies based on recursion depth.  

#### 3. Two Pointers  
- **Opposite directional** – Pointers moving towards each other.  
- **Same directional** – Pointers moving in the same direction.  
- **Fast and slow pointers** – Detecting cycles or finding middle elements.  

#### 4. Bit Manipulation  
- **Bit masking** – Selecting specific bits.  
- **Bit shifting** – Moving bits left or right.  
- **XOR manipulation** – Using XOR for various bit operations.  

#### 5. Amortized Analysis  
- **Aggregate method** – Analyzing total cost over a sequence of operations.  
- **Accounting method** – Assigning costs to individual operations.  
- **Potential method** – Using a potential function to analyze cost.  
- **Application in data structures** – Analyzing operations like dynamic array resizing.  


References: https://www.wscubetech.com/resources/dsa/space-complexity, https://stackoverflow.com/questions/22398733/time-complexity-of-data-structures; https://www.youtube.com/watch?v=v4cd1O4zkGw, https://www.youtube.com/watch?v=fW_OS3LGB9Q, https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/, https://www.youtube.com/watch?v=kp3fCihUXEg
