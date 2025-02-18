### Question:
Find the minimum element in a sorted and rotated array.

### Concept Name:
**Binary Search (Modified for Rotated Array)**

### Explanation:
In a rotated sorted array, the smallest element will be the only element that is smaller than its previous element. By using binary search, you can efficiently find the minimum element. The idea is to compare the middle element with the rightmost element to determine whether the minimum element lies in the left half or the right half of the array. This allows us to reduce the search space and find the minimum element in logarithmic time.

### Python Solution:

```python
def find_min(arr):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is the minimum element
        if mid > 0 and arr[mid] < arr[mid - 1]:
            return arr[mid]
        elif arr[mid] >= arr[left]:
            # If mid is greater than or equal to left, then the minimum is on the right
            left = mid + 1
        else:
            # Otherwise, the minimum is on the left
            right = mid - 1
    
    return arr[0]  # If no minimum found, return the first element (in case array is not rotated)

# Example usage
arr = [5, 6, 7, 9, 10, 1, 2, 3]
print(find_min(arr))  # Output: 1

```
## **Explanation of the Output:**
- left, right = 0, len(arr) - 1: Initializes the binary search range.
- mid = (left + right) // 2: Calculates the middle index.
- if mid > 0 and arr[mid] < arr[mid - 1]: Checks if the middle element is the minimum.
- elif arr[mid] >= arr[left]: If the left half is sorted, the minimum element lies in the right half.
- else: If the right half is sorted, the minimum element lies in the left half.

## **Example Log File Input:**
[5, 6, 7, 9, 10, 1, 2, 3]


## **Output:**
1

