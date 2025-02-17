# Heap Sort

### 1. **Definition:**
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It works by first building a max heap (or min heap) from the input data and then repeatedly extracting the maximum (or minimum) element from the heap and placing it into the sorted array.

### 2. **Steps:**
1. **Build a Max Heap:** Rearrange the input array into a max heap, where the largest element is at the root of the tree.
2. **Swap the Root with the Last Element:** Swap the root of the heap (maximum element) with the last element of the heap.
3. **Heapify the Reduced Heap:** After the swap, heapify the reduced heap to restore the heap property.
4. **Repeat:** Repeat steps 2 and 3 for the remaining elements until the heap is empty, and the array is sorted.

### 3. **Conditions:**
- The algorithm requires a complete binary tree (heap), where each parent node is greater (for max heap) or smaller (for min heap) than its children.
- The time complexity of the heap sort algorithm depends on the number of elements in the array.

### 4. **Applications:**
- **Priority Queues:** Since heaps allow for efficient extraction of the maximum or minimum element, Heap Sort is useful for implementing priority queues.
- **Memory-efficient Sorting:** It is useful when you want to perform sorting in-place without additional memory for data structures.
- **Scheduling Algorithms:** Used in scheduling tasks based on priority.
- **Data Stream Sorting:** In real-time systems where data comes in a continuous stream.

### 5. **Real-life Examples:**
- **CPU Scheduling:** Prioritizing tasks that need to be executed by the CPU.
- **Event Simulation:** Sorting and prioritizing events in a simulation, such as in discrete event simulation systems.
- **Task Scheduling in Operating Systems:** Organizing tasks with different priorities to manage execution time.

### 6. **Implementation:**
```python
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
```

### 7. **Edge Cases:**
- **Empty Array:** If the array has zero elements, heap sort will not process any elements.
- **Single Element:** A single-element array is already sorted.
- **Array with Duplicate Elements:** Heap sort can handle arrays with duplicate elements.
- **Array Sorted in Reverse Order:** Heap sort will still work efficiently even if the array is in reverse order.
- **Large Inputs:** Heap sort can handle large datasets but will require significant time and memory resources for heapify operations.

### 8. **Time Complexity:**
- **Build Heap:** O(n)
- **Heapify Operation:** O(log n) per element.
- **Overall Time Complexity:** O(n log n) for sorting.

### 9. **Space Complexity:**
Heap Sort operates in-place, meaning it does not require extra space other than the input array.
- **Space Complexity:** O(1)

### 10. **Mathematics Behind Heap Sort:**
Heap Sort relies on the concept of binary trees and the heap property (max heap or min heap).
- **Heap Property:** For a max heap, each parent node is greater than or equal to its child nodes.
- **Heapify Process:** The process of moving elements down the tree to maintain the heap property.

### 11. **Visualizations:**
Heap Sort can be visualized as a binary tree where:
- At each iteration, the largest element (root) is moved to the last position of the heap.
- The heap is then adjusted to maintain the heap property by performing a heapify operation.

For example, consider this array: `[4, 10, 3, 5, 1]`
- **Build the heap:** `[10, 5, 3, 4, 1]` - The first step is to build a max-heap from the unsorted list. In a max-heap, each parent node is greater than or equal to its child nodes.
- **Swap root with last element:** `[1, 5, 3, 4, 10]` - We swap the root (the largest element, `10`) with the last element in the list (`1`). This places the largest element in its correct final position.
- **Heapify:** `[5, 4, 3, 1, 10]` - We need to restore the heap property because the root is no longer the largest element. We heapify the root (currently `1`). The largest child of `1` is `5`, so we swap `1` with `5`.
- **Repeat until sorted:** `[1, 3, 4, 5, 10]`

### 12. **Comparisons with Similar Algorithms:**
- **Merge Sort:** Heap Sort and Merge Sort both have a time complexity of O(nlogn). However, Merge Sort uses additional space, whereas Heap Sort works in-place.
- **Quick Sort:** Quick Sort generally has a better average case performance but can degrade to O(n^2) in the worst case, unlike Heap Sort which is O(nlogn) in both average and worst cases.
- **Insertion Sort:** Insertion Sort is more efficient for small datasets or nearly sorted arrays, but Heap Sort is more efficient for larger datasets with a guaranteed O(nlogn) time complexity.

### 13. **Pros and Cons:**
- **Pros:**
  - In-place sorting (no additional memory required).
  - Time complexity is O(nlogn) for both worst and average cases.
  - Efficient for large datasets.
  
- **Cons:**
  - Not stable (relative order of equal elements may not be preserved).
  - Slower in practice compared to algorithms like Quick Sort due to more overhead in comparisons and swaps.
  - Not adaptive (doesn't take advantage of partially sorted data).

### 14. **Best Use Cases:**
- **Large datasets:** When sorting large data sets, Heap Sort ensures guaranteed O(nlogn) performance.
- **Priority Queues:** It is perfect for applications requiring efficient retrieval of the maximum or minimum element.

### 15. **Further Optimizations:**
- **Binary Heap Optimizations:** Using a Fibonacci heap can optimize certain operations, reducing the time complexity for some applications.
- **Parallel Heap Sort:** Parallelizing heapify operations can improve performance on multi-core systems for large datasets.


References: https://www.youtube.com/watch?v=2DmK_H7IdTo&list=PL9xmBV_5YoZOZSbGAXAPIq1BeUf4j20pl&index=6
