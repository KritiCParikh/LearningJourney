# Trees

### 1. **Definition of a Tree**

A **Tree** is a hierarchical data structure that consists of nodes connected by edges. It is one of the most widely used data structures for organizing and storing data, where each element (node) in the tree can have multiple child nodes, but only one parent node, except for the root node which has no parent.

**Key Characteristics:**
- **Root:** The topmost node in the tree.
- **Nodes:** The individual elements of the tree.
- **Edges:** The connections between nodes.
- **Leaf Nodes:** Nodes with no children.
- **Parent and Child:** In a tree, each node (except the root) has exactly one parent, and a node can have multiple child nodes.

---

### 2. **Types of Trees**

## a. Binary Trees
- **Definition:** A binary tree is a tree in which each node has at most two children, referred to as the **left** and **right** child. It’s the simplest form of a tree.
- **Properties:**
  - No ordering of the nodes.
  - Can be unbalanced (leading to performance issues if not managed properly).

---

## b. Binary Search Trees (BST)
- **Definition:** A binary search tree is a binary tree with the additional property that for each node:
  - **Left Subtree:** All nodes have values **less** than the parent node.
  - **Right Subtree:** All nodes have values **greater** than the parent node.
- **Properties:**
  - Efficient search, insertion, and deletion.
  - **Average Time Complexity:** O(log n) for search, insert, delete (if balanced).
  - **Worst-case Time Complexity:** O(n) (if unbalanced, like a linked list).
- **Use Cases:** Efficient searching (e.g., for dictionaries, sets), sorting (in-order traversal).

---

## c. AVL Trees (Self-Balancing BST)
- **Definition:** An AVL tree is a self-balancing binary search tree where the difference between the heights of the left and right subtrees of any node is at most **1**. If the tree becomes unbalanced after an insertion or deletion, rotations are performed to restore balance.
- **Properties:**
  - **Balance Factor:** The balance factor of a node is the difference in height between its left and right subtrees. The allowed balance factor is -1, 0, or 1.
  - **Rotations:** AVL trees use rotations (left and right) to balance the tree after insertions and deletions.
  - **Time Complexity:** Search, Insert, and Delete operations all have **O(log n)** time complexity.
- **Use Cases:** Databases, file systems, applications that require frequent insertions and deletions while maintaining sorted order.

---

## d. Red-Black Trees
- **Definition:** A red-black tree is another type of self-balancing binary search tree with an extra property that each node is either **red** or **black**. It ensures balance by enforcing the following rules:
  1. The root is always black.
  2. Red nodes cannot have red children (no two red nodes can be adjacent).
  3. Every path from a node to its descendant leaves must have the same number of black nodes.
  4. All leaf nodes (NIL) are black.
- **Properties:**
  - **Height Bound:** The height of the tree is guaranteed to be **O(log n)**.
  - **Insertions and Deletions:** Red-Black Trees ensure that operations remain balanced even after insertions and deletions.
- **Use Cases:** Implementations of associative containers in C++ (STL) and Java (TreeMap, TreeSet).

---

## e. Segment Trees
- **Definition:** A segment tree is a binary tree used to store intervals or segments. It allows efficient querying and updating of intervals, making it very useful for problems involving range queries, such as finding the sum, minimum, or maximum over a range.
- **Properties:**
  - **Time Complexity for Querying:** O(log n) for range queries.
  - **Time Complexity for Updates:** O(log n) for updating a segment.
- **Use Cases:** Range sum queries, range minimum/maximum queries, interval overlapping problems.
- **Example:** Finding the sum of elements in a given range in an array, or the minimum/maximum in a range.

---

## f. Fenwick Trees (Binary Indexed Trees)
- **Definition:** A Fenwick Tree (or Binary Indexed Tree, BIT) is a data structure that provides efficient methods for performing cumulative frequency tables or prefix sum queries and updates. It is similar to a segment tree but more space-efficient.
- **Properties:**
  - **Time Complexity for Querying:** O(log n).
  - **Time Complexity for Updates:** O(log n).
  - **Space Complexity:** O(n).
- **Use Cases:** Range sum queries, cumulative frequency tables, maintaining prefix sums.

---

## g. Other Trees

### **Trie (Prefix Tree)**
- **Definition:** A trie is a tree used to store strings where each node represents a single character of the string. It’s useful for fast lookup and prefix-based queries.
- **Use Cases:** Autocompletion, spell-checking, IP routing, prefix matching.

### **B-Trees**
- **Definition:** A generalization of binary search trees where nodes can have more than two children. B-Trees are commonly used in databases and file systems for efficient storage and retrieval of data.
- **Properties:** B-trees are self-balancing and maintain sorted order, allowing for efficient range queries and updates.
- **Use Cases:** Databases, file systems.

---

## h. Time Complexity for Common Operations

| **Operation**            | **Binary Tree** | **BST**        | **AVL Tree** | **Red-Black Tree** | **Segment Tree** | **Fenwick Tree** |
|--------------------------|-----------------|----------------|--------------|---------------------|------------------|------------------|
| **Search**               | O(n)            | O(log n)       | O(log n)     | O(log n)            | O(log n)         | O(log n)         |
| **Insert**               | O(n)            | O(log n)       | O(log n)     | O(log n)            | O(log n)         | O(log n)         |
| **Delete**               | O(n)            | O(log n)       | O(log n)     | O(log n)            | O(log n)         | O(log n)         |
| **Update**               | O(n)            | O(log n)       | O(log n)     | O(log n)            | O(log n)         | O(log n)         |
| **Query (Range)**        | O(n)            | O(n)           | O(n)         | O(n)                | O(log n)         | O(log n)         |

---

## i. Applications of Different Tree Types

- **Binary Trees:** Simple hierarchical structures where order isn't important. Used for basic organizational structures.
- **Binary Search Trees:** Efficient searching, sorting, and dynamic set implementations.
- **AVL Trees:** Used where insertions and deletions are frequent, and balance is required to ensure fast operations.
- **Red-Black Trees:** Preferred when frequent insertions and deletions occur while ensuring balance in practical applications.
- **Segment Trees:** Efficient solutions for range queries and range updates.
- **Fenwick Trees:** Efficient for maintaining cumulative sums or frequency counts with updates.
- **Tries:** Optimized for fast searching and prefix-based operations.


---

### 3. **Operations on Trees**

1. **Traversal:** 
   - **In-order Traversal (LNR):** Visit left subtree, node, right subtree (used in BST to get sorted order).
   - **Pre-order Traversal (NLR):** Visit node, left subtree, right subtree.
   - **Post-order Traversal (LRN):** Visit left subtree, right subtree, node.
   - **Level-order Traversal:** Visit nodes level by level from top to bottom.

2. **Insertion:**
   - **Binary Tree:** Insert at the first available child node (usually left to right).
   - **BST:** Insert nodes in a way that maintains the ordering property.

3. **Deletion:**
   - **Leaf Node Deletion:** Simply remove the node.
   - **Node with One Child:** Replace the node with its single child.
   - **Node with Two Children:** Replace the node with its in-order successor or predecessor.

4. **Searching:**
   - **Binary Search Tree:** Search for a node by comparing values and traversing left or right based on the comparison.

5. **Balancing (in AVL or Red-Black Trees):**
   - Reorganize the tree to ensure that it remains balanced after insertions or deletions.

---

### 4. **Implementation of a Tree (Binary Tree Example)**

Here’s a simple implementation in Python for a **Binary Tree**:

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left:
                self._insert(root.left, key)
            else:
                root.left = Node(key)
        else:
            if root.right:
                self._insert(root.right, key)
            else:
                root.right = Node(key)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.value, end=" ")
            self.in_order(root.right)

# Example usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)

tree.in_order(tree.root)  # Output: 2 3 4 5 7
```

### 5. **Common Problems Involving Trees**

- **Find the Height of a Tree:**
  - The height of a tree is the number of edges on the longest path from the root to a leaf node.

- **Check if a Binary Tree is Balanced:**
  - A tree is balanced if for every node, the height of its left and right subtrees differ by at most 1.

- **Lowest Common Ancestor (LCA):**
  - Given two nodes in a tree, find the lowest common ancestor (the node farthest from the root that is an ancestor of both nodes).

- **Level Order Traversal:**
  - Traverse the tree level by level.

- **Convert Binary Search Tree to a Doubly Linked List:**
  - Flatten a binary search tree into a doubly linked list while preserving the BST properties.

---

### 6. **CRUD (Create, Read, Update, Delete) Operations on Trees**

- **Create:** Trees are created by initializing a root node, then adding children nodes using insertion operations.
- **Read:** Trees are read using traversal techniques like in-order, pre-order, post-order, or level-order traversal.
- **Update:** Nodes can be updated by searching for the node, then modifying its value.
- **Delete:** Nodes are deleted based on their position (leaf, one child, or two children) and by adjusting the tree structure accordingly.

---

### 7. **Additional Concepts and Topics**

- **Binary Search Tree (BST) Properties:**
  - The left child’s value is always less than the parent node’s value.
  - The right child’s value is always greater than the parent node’s value.

- **Balanced vs. Unbalanced Trees:**
  - **Balanced Trees:** Keep operations like insertion, deletion, and search at optimal time complexity (e.g., AVL Tree, Red-Black Tree).
  - **Unbalanced Trees:** May degrade performance (e.g., a skewed binary tree has worst-case time complexity).

- **Self-balancing Trees:**
  - Automatically adjust the height of subtrees during insertions and deletions to maintain optimal performance.

- **Tree Traversal:**
  - Traversing a tree means visiting all its nodes in some order. There are several traversal methods:

  - **In-Order Traversal (Left, Root, Right):**
    - Visits nodes in ascending order for a BST.
    - **Recursive pattern:** Traverse left subtree → Visit root → Traverse right subtree.

  - **Pre-Order Traversal (Root, Left, Right):**
    - Used for creating a copy of the tree or prefix notation.
    - **Recursive pattern:** Visit root → Traverse left subtree → Traverse right subtree.

  - **Post-Order Traversal (Left, Right, Root):**
    - Used for deletion of the tree or postfix notation.
    - **Recursive pattern:** Traverse left subtree → Traverse right subtree → Visit root.

---

### 8. Conclusion:

When choosing the right type of tree, it's important to consider the specific use case and performance requirements:

- **Binary Search Trees (BST)** are ideal for general-purpose searches, insertions, and deletions if the data remains balanced.
- **AVL Trees** and **Red-Black Trees** are great choices when ensuring balance is crucial to maintaining optimal search performance, as they offer better time complexity (O(log n)) compared to regular BSTs.
- **B-Trees** should be preferred for external data storage, especially in large datasets where disk I/O efficiency is a concern. Their structure is optimized for fewer read/write operations, making them ideal for databases.
- **Trie Trees** are perfect for applications that involve string matching or prefix searches, such as spell checkers or autocomplete systems.
- **Segment Trees** excel in handling range queries efficiently, making them suitable for problems in computational geometry or situations where you need to retrieve or update data over a range.

To summarize, the choice of tree largely depends on the specific problem you're tackling. For general data structures, **Binary Search Trees** or **Self-Balancing Trees** (like AVL or Red-Black Trees) offer a solid foundation. However, when performance or specialized functionality is needed (like in search engines or range-based queries), **Other Trees** like **Tries** or **Segment Trees** provide unique and optimized solutions. Always consider your dataset’s size, update frequency, and type of queries to make an informed decision about which tree structure will work best for your scenario.

---

References: https://www.youtube.com/watch?v=oSWTXtMglKE, https://www.youtube.com/watch?v=cf_TpRNWlxc&list=PL03of0rPCur_NZ9Rr4w1a5RDMU2qegBQl&index=5
