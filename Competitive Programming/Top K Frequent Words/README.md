# Top K Frequent Words

- LeetCode: 692
- Question: https://leetcode.com/problems/top-k-frequent-words/description/
- Company: Goldman Sachs.

## Problem Statement

Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.

The answer should be sorted by frequency from highest to lowest. If multiple words have the same frequency, sort them in **lexicographical order**.

---


### Approach:
1. **Count Word Frequencies**: Use `Counter` from the `collections` module to count occurrences of each word.
2. **Sort by Frequency & Lexicographical Order**:
   - Sort words first by frequency (descending).
   - If two words have the same frequency, sort them lexicographically (ascending).
3. **Return the Top `k` Words**.

---

### Code Implementation:

```python
from collections import Counter

def topKFrequent(words, k):
    # Count the frequency of each word
    freq_map = Counter(words)
    
    # Sort words: first by frequency (descending), then by lexicographical order (ascending)
    sorted_words = sorted(freq_map.keys(), key=lambda word: (-freq_map[word], word))
    
    # Return top k words
    return sorted_words[:k]

# Example Test Cases
words1 = ["i","love","leetcode","i","love","coding"]
k1 = 2
print(topKFrequent(words1, k1))  # Output: ["i", "love"]

words2 = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k2 = 4
print(topKFrequent(words2, k2))  # Output: ["the", "is", "sunny", "day"]
```

# Explanation

## Step 1: Count Frequencies
```python
from collections import Counter
freq_map = Counter(words)
```
#### Example Output:
Counter({'the': 4, 'is': 3, 'sunny': 2, 'day': 1})

## Step 2: Sorting
```python
sorted_words = sorted(freq_map.keys(), key=lambda word: (-freq_map[word], word))
```
## Sorting Key:
- freq_map[word]: Sort by highest frequency first.
- word: Sort lexicographically in case of ties.

## Result
["the", "is", "sunny", "day"]

#### Step 3: Return the Top k Elements
return sorted_words[:k]

- Extracts the top k most frequent words.
---
# Complexity Analysis:

| **Operation**         | **Time Complexity** |
|----------------------|---------------------|
| Counting Frequencies  | `O(n)`              |
| Sorting              | `O(n log n)` (due to sorting `n` unique words) |
| Slicing the List     | `O(k)`              |
| **Overall Complexity** | `O(n log n)`       |

---

## Follow-up (Optimized Approach: `O(n log k)`)

Instead of sorting the entire list, we can use a **min-heap of size `k`**:

- Insert elements into a heap with **negative frequency** as priority.
- This maintains a heap of size `k` in **O(n log k)** time.

---

### Optimized Code Using Min-Heap:

```python
import heapq
from collections import Counter

def topKFrequent(words, k):
    freq_map = Counter(words)
    
    # Min-heap with (-freq, word) so that heap orders by highest frequency first
    heap = [(-freq, word) for word, freq in freq_map.items()]
    heapq.heapify(heap)  # O(n)
    
    # Extract k elements (O(k log n))
    return [heapq.heappop(heap)[1] for _ in range(k)]
```

## Why is this better?

- **Heap Operations:** `O(n log k)` instead of `O(n log n)`.
- **More efficient for large inputs**.

---

## Summary:

| **Approach**  | **Time Complexity** | **Space Complexity** |
|---------------|---------------------|----------------------|
| **Sorting**   | `O(n log n)`        | `O(n)`               |
| **Min-Heap**  | `O(n log k)`        | `O(n)`               |

Both approaches work, but **heap-based implementation is optimal when `k` is much smaller than `n`**.


