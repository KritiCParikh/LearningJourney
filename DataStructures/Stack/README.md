# Stacks

## 1. Definition:
A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. This means that the last element added is the first one to be removed.

---

## 2. Operations:

### a. **Push**:
Adds an element to the top of the stack.  
**Example**: `stack.push(5)` (adds the value 5 to the stack)

### b. **Pop**:
Removes and returns the element from the top of the stack.  
**Example**: `stack.pop()` (removes the top element from the stack)

### c. **Peek (Top)**:
Returns the top element of the stack without removing it.  
**Example**: `stack.peek()` (shows the top element)

### d. **IsEmpty**:
Checks if the stack is empty.  
**Example**: `stack.isEmpty()` (returns true if the stack is empty)

### e. **Size**:
Returns the number of elements in the stack.  
**Example**: `stack.size()` (returns the number of elements in the stack)

---

## 3. Implementations:

### a. **Array-based Implementation**:
- An array is used where a pointer or index keeps track of the top element of the stack.
- Constant time complexity (O(1)) for both **push** and **pop** operations.

```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None
```

### b. **Linked List-based Implementation:n**:
- A linked list is used where each node contains an element and a reference to the next node.
- Each new element is added at the beginning (top) of the linked list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            return None
        popped_item = self.top.data
        self.top = self.top.next
        return popped_item
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
```


## 4. Tower of Hanoi (Game-related problem):

The **Tower of Hanoi** is a classic problem that involves moving disks of different sizes from one peg to another, following a few rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the top disk from one stack and placing it on another stack.
3. No disk may be placed on top of a smaller disk.

This problem can be solved recursively using stacks, where each recursive call can be treated as a move involving pushing and popping disks from stacks.

---

## 5. LIFO (Last In, First Out):

The **Last In, First Out (LIFO)** principle means that the most recently added element is the first to be removed. This contrasts with **FIFO (First In, First Out)**, which is used in queues, where the first element added is the first to be removed.

In the case of a stack:

- **Push** adds an item to the "top" (most recent).
- **Pop** removes the item from the "top" (most recent).

---

6. **Common problems:**  
  - Balanced Parentheses
  - Reverse a Stack
  - Tower of Hanoi
  - Sort a Stack
  - Stock Span Problem
  - Next Greater Element


References: https://www.youtube.com/watch?v=fEaLAs3lzo0&list=PLVHgQku8Z9354TOeH6sygmoL_t2poSaxS&index=3

