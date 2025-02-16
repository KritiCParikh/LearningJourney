# Queues

## 1. **Definition**
A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. In a queue, the element added first is the one that is removed first.

- **Enqueue**: Adding an item to the queue.
- **Dequeue**: Removing an item from the queue.
- **Front**: Refers to the front element of the queue (the first element that would be dequeued).
- **Rear**: Refers to the last element in the queue (the most recent element added).

### Types of Queues:
- **Simple Queue**: A standard FIFO queue.
- **Circular Queue**: A queue where the last element is connected back to the first element, allowing for efficient space utilization.
- **Priority Queue**: Elements are dequeued based on priority, rather than the order they were enqueued.
- **Double-Ended Queue (Deque)**: A queue that allows insertion and deletion of elements from both ends, providing more flexibility than a regular queue.

## 2. **Operations**
Queues support several basic operations:

- **Enqueue**: Add an element to the rear of the queue.
- **Dequeue**: Remove the element from the front of the queue.
- **Peek/Front**: View the front element without removing it.
- **IsEmpty**: Check if the queue is empty.
- **IsFull**: Check if the queue is full (for fixed-size queues).

## 3. **Implementation**

A queue can be implemented using:
- **Array**: A simple array structure where the front and rear indices are managed. The front indicates the first element of the queue, and rear indicates the last element added.
```
python

class QueueUsingArray:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.rear == self.size - 1:
            print("Queue Overflow! The queue is full.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item
            print(f"Enqueued {item}")
    
    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow! The queue is empty.")
        else:
            removed_item = self.queue[self.front]
            self.front += 1
            if self.front > self.rear:  # Reset if queue is empty
                self.front = self.rear = -1
            print(f"Dequeued {removed_item}")
    
    def peek(self):
        if self.front != -1:
            print(f"Front element is {self.queue[self.front]}")
        else:
            print("Queue is empty.")
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return self.rear == self.size - 1
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements:", self.queue[self.front:self.rear+1])

# Testing Array-based Queue
queue = QueueUsingArray(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)  # Should show Queue Overflow
queue.dequeue()
queue.peek()
queue.display()

```

- **Linked List**: A dynamic implementation that uses pointers to add or remove elements. In a linked list-based queue, we use a Node class that contains a value and a reference to the next node. The queue has two pointers: front (points to the first node) and rear (points to the last node).

```
python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued {item}")
    
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow! The queue is empty.")
        else:
            removed_item = self.front.value
            self.front = self.front.next
            if self.front is None:  # If the queue is empty, reset rear to None
                self.rear = None
            print(f"Dequeued {removed_item}")
    
    def peek(self):
        if self.front:
            print(f"Front element is {self.front.value}")
        else:
            print("Queue is empty.")
    
    def is_empty(self):
        return self.front is None
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self.front
            while current:
                print(current.value, end=" ")
                current = current.next
            print()

# Testing Linked List-based Queue
queue = QueueUsingLinkedList()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.dequeue()
queue.peek()
queue.display()

```
- **Two Stacks**: A queue can be implemented using two stacks, simulating the FIFO behavior of a queue. The two-stack implementation simulates the behavior of a queue. We use two stacks (stack1 and stack2). When enqueuing, we push elements to stack1. When dequeuing, we transfer elements from stack1 to stack2 if stack2 is empty. This simulates FIFO behavior.

```
python

class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)
        print(f"Enqueued {item}")
    
    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                print("Queue Underflow! The queue is empty.")
                return
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if self.stack2:
            removed_item = self.stack2.pop()
            print(f"Dequeued {removed_item}")
        else:
            print("Queue Underflow! The queue is empty.")
    
    def peek(self):
        if not self.stack2:
            if not self.stack1:
                print("Queue is empty.")
                return
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if self.stack2:
            print(f"Front element is {self.stack2[-1]}")
        else:
            print("Queue is empty.")
    
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            if self.stack2:
                print("Queue elements:", self.stack2[::-1] + self.stack1)
            else:
                print("Queue elements:", self.stack1[::-1])

# Testing Two Stacks-based Queue
queue = QueueUsingTwoStacks()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.dequeue()
queue.peek()
queue.display()

```

## 4. **FIFO (First In, First Out)**

The queue follows the FIFO principle:

- **First In**: The first element added to the queue will be the first one to be removed.
- **First Out**: The element that has been in the queue the longest will be the first to be removed when dequeued.

This makes it useful for scheduling tasks, handling requests in order, and many other real-world applications.

## 5. **Common Problems**

- **Queue Overflow**: Occurs when trying to enqueue an element in a full queue (for non-circular queues).
- **Queue Underflow**: Occurs when trying to dequeue an element from an empty queue.
- **Circular Queue Issues**: In circular queues, managing the front and rear pointers correctly to avoid errors when the queue is full or empty.

## 6. **CRUD Operations**

- **Create (Enqueue)**: Add an item to the rear of the queue.
- **Read**: Typically refers to accessing the front of the queue without removing it.
- **Update**: Not common in queues, as queues are used for adding and removing items.
- **Delete (Dequeue)**: Remove an item from the front of the queue.


References: https://www.youtube.com/watch?v=A3ZUpyrnCbM
