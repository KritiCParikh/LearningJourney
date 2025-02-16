Definition: Efficiently finds the position of a target element in a sorted array.

Steps:
- Start with the middle element of the array.
- If the target is smaller, search in the left half; if larger, search in the right half.
- Repeat the process until the element is found or the search space is exhausted.

Conditions: https://www.youtube.com/watch?v=eVuPCG5eIr4

Applications:

Real-Life Example:

Implementation_Code/ Basic_Template:
```
function binarySearch(array, target):
    left = 0
    right = length of array - 1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] == target:
            return mid
        else if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

Edge_Cases:

Time Complexity: O(log n) [https://youtube.com/shorts/ks8_koF96M0?si=TfQK7W56vp2q4S7e]

The_Mathematics_Behind_this:

Space_Complexity:

Visualizations:

Comparisons_with_Similar_Algorithms:

Pros_and_Cons:

Best_Use_Cases:

Further_Optimizations:

References:
