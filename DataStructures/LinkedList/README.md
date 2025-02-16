# Linked Lists

1. Linked Lists are a linear data structure where elements (nodes) are stored at random memory locations. Each node consists of:  
- **Data**: The value stored in the node.  
- **Pointer (Next)**: A reference to the next node in the sequence (for singly linked lists).  
- **Pointer (Prev)**: An additional reference to the previous node in **doubly linked lists**.  

---

## 2. Types of Linked Lists
### a. Singly Linked List (SLL)
Each node has:  
**Data** – Stores the value.  
**Next** – Points to the next node in the list.  

```
Head → [Data | Next] → [Data | Next] → NULL
```

```
python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the head
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the tail
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Delete head
    def delete_head(self):
        if self.head:
            self.head = self.head.next

    # Delete tail
    def delete_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next and second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    # Traverse and print the list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")

    # Search for an element
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

# Example usage of Singly Linked List
sll = SinglyLinkedList()
sll.insert_at_head(1)
sll.insert_at_tail(2)
sll.insert_at_tail(3)
sll.traverse()
sll.delete_head()
sll.traverse()
```

### b. Doubly Linked List (DLL)
Each node has:  
**Data** – Stores the value.  
**Prev** – Points to the previous node.  
**Next** – Points to the next node.  

```
NULL ← [Prev | Data | Next] ↔ [Prev | Data | Next] → NULL
```

```
python

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the head
    def insert_at_head(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    # Insert at the tail
    def insert_at_tail(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Delete head
    def delete_head(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    # Delete tail
    def delete_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    # Traverse and print the list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("NULL")

    # Search for an element
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

# Example usage of Doubly Linked List
dll = DoublyLinkedList()
dll.insert_at_head(1)
dll.insert_at_tail(2)
dll.insert_at_tail(3)
dll.traverse()
dll.delete_head()
dll.traverse()
```


### c. Circular Linked List (CLL)
The last node connects back to the head.  

---

## 3. Key Operations
| Operation          | Time Complexity (SLL) | Time Complexity (DLL) |
|-------------------|----------------------|----------------------|
| **Insert at Head** | O(1)                 | O(1)                 |
| **Insert at Tail** | O(n)                 | O(1)                 |
| **Delete Head**    | O(1)                 | O(1)                 |
| **Delete Tail**    | O(n)                 | O(1)                 |
| **Search Element** | O(n)                 | O(n)                 |

---
4. **Key Concepts & Common problems:**  
   - Reversal of a Linked List 
   - Detecting Cycles (Floyd’s Cycle Detection or Tortoise & Hare Algorithm)
   - Finding the Middle Element (Tortoise & Hare Algorithm)  
   - Merging Two Sorted Linked Lists
   - Removing Duplicates from a Linked List
   - Happy Number Detection

---

## 5. CRUD Operations
- **Create:** Insert a new node at the beginning, end, or middle.
- **Read:** Traverse and print the linked list.
- **Update:** Modify a node’s value.
- **Delete:** Remove a node from the list.


---

References: https://www.youtube.com/watch?v=11KwUOPj6Mw&list=PLVHgQku8Z9354TOeH6sygmoL_t2poSaxS&index=2
