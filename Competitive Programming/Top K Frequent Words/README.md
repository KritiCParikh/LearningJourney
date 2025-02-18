# Top K Frequent Words

- LeetCode: 692
- Question: https://leetcode.com/problems/top-k-frequent-words/description/
- Company: Goldman Sachs.

## Problem Statement

Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.

The answer should be sorted by frequency from highest to lowest. If multiple words have the same frequency, sort them in **lexicographical order**.

---

### Example 1:
#### **Input:**
words = ["i","love","leetcode","i","love","coding"], k = 2

#### **Output:**
["i","love"]

#### **Explanation:**
- "i" and "love" are the two most frequent words.
- Since "i" comes before "love" in alphabetical order, it appears first.

### Example 2:
#### **Input:**
words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4

#### **Output:**
["the","is","sunny","day"]


#### **Explanation:**
- "the" appears 4 times, "is" appears 3 times, "sunny" appears 2 times, and "day" appears 1 time.
- Sorted by frequency, then lexicographically.

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

