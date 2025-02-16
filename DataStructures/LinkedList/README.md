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

### b. Doubly Linked List (DLL)
Each node has:  
**Data** – Stores the value.  
**Prev** – Points to the previous node.  
**Next** – Points to the next node.  

```
NULL ← [Prev | Data | Next] ↔ [Prev | Data | Next] → NULL
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

---

## 5. CRUD Operations
- **Create:** Insert a new node at the beginning, end, or middle.
- **Read:** Traverse and print the linked list.
- **Update:** Modify a node’s value.
- **Delete:** Remove a node from the list.

References: https://www.youtube.com/watch?v=11KwUOPj6Mw&list=PLVHgQku8Z9354TOeH6sygmoL_t2poSaxS&index=2
