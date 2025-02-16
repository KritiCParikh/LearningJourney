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

## 2. **Operations**
Queues support several basic operations:

- **Enqueue**: Add an element to the rear of the queue.
- **Dequeue**: Remove the element from the front of the queue.
- **Peek/Front**: View the front element without removing it.
- **IsEmpty**: Check if the queue is empty.
- **IsFull**: Check if the queue is full (for fixed-size queues).

## 3. **Implementation**

A queue can be implemented using:
- **Array**: A simple array structure where the front and rear indices are managed.
- **Linked List**: A dynamic implementation that uses pointers to add or remove elements.
- **Two Stacks**: A queue can be implemented using two stacks, simulating the FIFO behavior of a queue.

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
