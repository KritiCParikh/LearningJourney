# Selection Sort Algorithm

## 1. Definition:
Selection Sort is a simple comparison-based sorting algorithm that divides the list into two parts: a sorted part and an unsorted part. It repeatedly selects the smallest (or largest, depending on sorting order) element from the unsorted part and swaps it with the first unsorted element. This process continues until the entire list is sorted.

## 2. Steps:
- **Step 1:** Start from the first element of the array.
- **Step 2:** Find the minimum element in the unsorted part of the array (from the current index to the end).
- **Step 3:** Swap the found minimum element with the first unsorted element.
- **Step 4:** Move the boundary of the unsorted array one step forward.
- **Step 5:** Repeat the process for the remaining unsorted array until it’s completely sorted.

## 3. Conditions:
- The array or list should be finite.
- Comparison of elements is required.

## 4. Applications:
- Suitable for small datasets where ease of implementation is more important than performance.
- Common in teaching sorting algorithms and for use in situations where auxiliary memory space is limited (in-place sort).
- Good for situations where memory is a constraint and you don’t mind the time complexity being less optimal.

## 5. Real-Life Examples:
- Sorting small lists of data in embedded systems with limited memory.
- Sorting cards manually (since it mimics human sorting behavior).

## 6. Implementation:
Here is a simple Python implementation of Selection Sort:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

## 7. Edge Cases:
- **Empty Array:** Selection sort doesn't need to perform any actions on an empty array.
- **Single-element Array:** The array is already sorted.
- **Array with All Identical Elements:** Selection sort will still iterate through the array but no actual swaps will occur.

## 8. Time Complexity:
- **Best Case:** O(n²) — even if the array is already sorted, selection sort will still go through the entire list.
- **Average Case:** O(n²) — for any general unsorted list.
- **Worst Case:** O(n²) — for a completely reversed list.

In all cases, selection sort performs the same number of comparisons.

## 9. Space Complexity:
- **Space Complexity:** O(1) — Selection sort is an in-place sorting algorithm, meaning it requires constant space.

## 10. Mathematics Behind Selection Sort:
- **Number of Comparisons:** In each iteration, there are `n - i` comparisons where `i` is the index of the current element being considered. The total comparisons across all iterations is the sum of the first `n - 1` integers:
  
T(n) = (n - 1) * n / 2 = O(n²)

- **Swaps:** In the worst case, there are at most `n - 1` swaps.

## 11. Visualizations:
Imagine sorting an unsorted list step-by-step, as each pass identifies the smallest element and places it in its correct position.

## 12. Comparisons with Similar Algorithms:
- **Bubble Sort:** Both have O(n²) time complexity, but Selection Sort is more efficient in terms of the number of swaps (O(n) swaps, versus O(n²) swaps in Bubble Sort).
- **Insertion Sort:** Insertion Sort tends to perform better in practice for nearly sorted data, but Selection Sort’s fewer swaps can be an advantage.
- **Merge Sort & Quick Sort:** These are more efficient (O(n log n) time complexity) and preferred for large datasets.

## 13. Pros and Cons:
- **Pros:**
  - Simple to implement.
  - Doesn’t require additional memory space (in-place).
  - Good for small arrays.
- **Cons:**
  - Inefficient for large datasets.
  - Constantly makes comparisons, even if the list is sorted or nearly sorted.

## 14. Best Use Cases:
- Small datasets or datasets with a small range of values.
- Situations where memory usage is a critical constraint and swapping elements is acceptable.

## 15. Further Optimizations:
- **Bi-directional Selection Sort (Cocktail Sort):** Selects both the smallest and largest elements in each pass, reducing the number of passes needed.
- **Adaptive Selection Sort:** Use algorithms like Insertion Sort once the array becomes nearly sorted to optimize further.

References: https://www.youtube.com/watch?v=g-PGLbMth_g
