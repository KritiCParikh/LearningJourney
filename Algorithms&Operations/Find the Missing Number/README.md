### **Find the Missing Number**

**Purpose**:  
The purpose of this algorithm is to find the missing number in an array of `n-1` elements, where the elements range from `1` to `n`. There is exactly one number missing from the array.

### **How It Works**:
1. **Calculate the sum of all numbers from 1 to n**:  
   The formula to calculate the sum of numbers from `1` to `n` is:
Total Sum = n * (n + 1) / 2

2. **Subtract the sum of elements in the array from the total sum**:  
   Once you have the total sum, subtract the sum of the elements in the given array. The difference will be the missing number.

### **Algorithm**:
```python
def find_missing_number(arr, n):
    total_sum = (n * (n + 1)) // 2  # Sum of all numbers from 1 to n
    array_sum = sum(arr)  # Sum of elements in the array
    return total_sum - array_sum  # The missing number
```

### Time Complexity:
- **O(n)**: The algorithm requires a single pass through the array to compute the sum of its elements. Therefore, the time complexity is linear.

### Space Complexity:
- **O(1)**: The algorithm only requires a constant amount of space to store the sums, regardless of the size of the input array.

### Edge Cases:
- **Array with one element missing at the beginning**: The algorithm will work without modification.
- **Array with the missing element at the end**: The algorithm still works, as the sum will be correctly calculated.
- **All elements present**: If the array contains all elements from 1 to n-1, the sum will indicate that the last number `n` is missing.

### Example:
If the array is `[1, 2, 4, 5, 6]` and `n = 6`:

- Total sum:
(6 * (6 + 1)) / 2 = 21

- Array sum:
1 + 2 + 4 + 5 + 6 = 18

- Missing number:
21 - 18 = 3

Thus, the missing number is **3**.

### Applications:
- **Data Analysis**: This can be used in scenarios where you are given a range of numbers, but one is missing, such as tracking elements in a dataset.
- **Error Detection**: When processing sequences of numbers or identifiers, this method can quickly identify missing elements in a list or series.

### Best Use Cases:
- When given a large range of numbers, and you're asked to find one missing element.
- Used in cases like missing integers in a list or when ensuring completeness of sequential data.


References: https://www.youtube.com/watch?v=WnPLSRLSANE
