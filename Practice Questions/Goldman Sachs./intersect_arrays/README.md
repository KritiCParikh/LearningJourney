# **Algorithm: Intersection of Two Arrays (With Duplicates)**

## **Problem Statement**
Given two arrays, find the intersection elements while maintaining their frequency.

### **Example**
#### **Input:**
```plaintext
arr1 = [1, 1, 2, 2, 2]
arr2 = [1, 1, 1, 2, 2, 3, 4, 5]
```

#### **Output:**
[1, 1, 2, 2]

```

### **Count occurrences:**
- Use a hashmap (`Counter`) to store the frequency of elements in `arr1`.
- Use another hashmap to store the frequency of elements in `arr2`.

### **Find common elements:**
- Iterate through the elements in `arr1`’s frequency map.
- If an element exists in `arr2`’s frequency map, take the **minimum count** from both maps.

### **Construct the result array:**
- Append the common element to the result array based on the minimum count.
- Return the result array.

---

## **Code Implementation (Python)**
```python
from collections import Counter

def intersect_arrays(arr1, arr2):
    # Step 1: Count occurrences in both arrays
    count1 = Counter(arr1)
    count2 = Counter(arr2)
    
    # Step 2: Find common elements with minimum count
    intersection = []
    for num in count1:
        if num in count2:
            intersection.extend([num] * min(count1[num], count2[num]))
    
    return intersection

# Example usage:
arr1 = [1, 1, 2, 2, 2]
arr2 = [1, 1, 1, 2, 2, 3, 4, 5]
print(intersect_arrays(arr1, arr2))  # Output: [1, 1, 2, 2]
```

## **Time Complexity Analysis**
- **Building frequency maps:** O(N + M), where N and M  are the lengths of `arr1` and `arr2`.
- **Finding the intersection:** O(N)(or O(M) if iterating over `arr2`).
- **Constructing the output:** O(K), where K is the number of common elements.
- **Overall Complexity:** O(N + M) (efficient solution).

---

## **Edge Cases Considered**
- **Arrays with no common elements:** Output `[]`
- **One or both arrays are empty:** Output `[]`
- **Arrays with duplicates and different frequencies**
- **Large input sizes for performance testing**


## **Explanation of the Output:**
For the array [1, 2, 5, 6, 11, 2] and target sum 12, the minimum subarray whose sum is at least 12 is [11, 2], and its length is 2.

