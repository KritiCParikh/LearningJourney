### Question:
Find the median of two sorted arrays of different sizes in O(n) time complexity.

### Concept Name:
**Merging Arrays (Two-Pointer Technique)**

### Explanation:
To find the median of two sorted arrays in linear time (O(n)), we can merge the two arrays while maintaining their sorted order. As we merge, we track the middle elements. When the total number of elements is odd, the median will be the middle element; if even, it will be the average of the two middle elements.

### Python Solution:

```python
def find_median_sorted_arrays(arr1, arr2):
    # Merging the two sorted arrays
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1 or arr2
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    # Find the median from the merged array
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2

# Example usage
arr1 = [1, 3, 8]
arr2 = [7, 9, 10, 11]
print(find_median_sorted_arrays(arr1, arr2))  # Output: 8

```
## **Explanation of the Output:**
- Merging Step: We use two pointers, i and j, to iterate through both arrays and merge them into a single sorted list.
- Median Calculation: After merging the arrays, the median is determined based on the total length of the merged array. If the length is odd, the median is the middle element; if even, it is the average of the two middle elements.

## **Example Input:**
arr1 = [1, 3, 8]

arr2 = [7, 9, 10, 11]


## **Output:**
8


