# **Binary Search**

## **Definition**
Binary Search is an efficient algorithm to find the position of a target element in a **sorted array**. Instead of scanning elements one by one, it repeatedly divides the search space in half until the target is found or the search space is exhausted.

---

## **Steps**
1. Start with the **middle element** of the array.
2. If the **target is smaller**, search in the **left half** of the array.
3. If the **target is larger**, search in the **right half** of the array.
4. Repeat steps 1-3 until the element is found or the search space becomes empty.

---

## **Conditions**
- The array must be **sorted**.
- It works well with **random access data structures** (like arrays, but not linked lists).
- Time complexity depends on the number of divisions (logarithmic behavior).

[🔗 Video Explanation](https://www.youtube.com/watch?v=eVuPCG5eIr4)

---

## **Applications**
- Searching in **large datasets** (e.g., phone books, sorted lists).
- Used in **database indexing**.
- Helps in **algorithm optimizations** like **searching in infinite space**.
- Applied in **computer graphics**, **AI**, and **data compression**.

### **Real-Life Example**
Think of **looking for a word in a dictionary**:
- Open the dictionary **in the middle**.
- If the word comes before the page you opened, look in the **left half**.
- If the word comes after, look in the **right half**.
- Keep narrowing down until you find the word.

---

## **Implementation - Code / Basic Template**
```
python
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

## **Edge Cases**
- **Empty Array** → Should return `-1`.
- **Single Element Array** → Should check if it's the target.
- **Target Not in Array** → Should return `-1`.
- **Even vs Odd Length Arrays** → Middle selection should be handled properly.
- **Duplicate Values** → Can return the first occurrence but may need adjustments for all occurrences.

---

## **Time Complexity**
Binary Search works by **halving** the search space at each step.

- **Worst-case**: **O(log n)**
- **Best-case**: **O(1)** (if the middle element is the target)
- **Average-case**: **O(log n)**  

[🔗 Time Complexity Explanation](https://youtube.com/shorts/ks8_koF96M0?si=TfQK7W56vp2q4S7e)

---

## **Mathematics Behind This**
At each step, the problem size reduces by half.

- Initial size: **n**
- After 1 step: **n/2**
- After 2 steps: **n/4**
- After k steps: **n / 2^k**  
  (Stops when `n / 2^k = 1`)

Solving for k:
\[
k = \log_2 n
\]
This proves that **Binary Search runs in O(log n) time**.

---

## **Space Complexity**
- **O(1)** for the iterative approach (no extra memory used).
- **O(log n)** for the recursive approach (due to recursive stack calls).

---

## **Visualizations**
### **Graph Representation**  
![image](https://github.com/KritiCParikh/LearningJourney/blob/main/images/7.png)

### **Example Walkthrough**
```plaintext
Array = [1, 3, 5, 7, 9, 11, 13, 15], Target = 7

Step 1: mid = (0+7)/2 = 3 → array[3] = 7 ✅ Found!

## **Comparisons with Similar Algorithms**
| **Algorithm**            | **Time Complexity**  | **Sorted Required?** | **Best Use Case**                   |
|-------------------------|---------------------|---------------------|--------------------------------------|
| **Binary Search**       | O(log n)           | ✅ Yes              | Searching in sorted arrays         |
| **Linear Search**       | O(n)               | ❌ No               | Small or unsorted datasets         |
| **Jump Search**         | O(√n)              | ✅ Yes              | Large, sorted datasets             |
| **Interpolation Search**| O(log log n) (best)| ✅ Yes              | Uniformly distributed data         |

---

## **Pros and Cons**
### ✅ **Pros**
- **Fast (O(log n))** for large datasets.
- **Works well for sorted data**.
- **Low memory usage** in iterative form.

### ❌ **Cons**
- **Requires sorted data**.
- **Not efficient for small datasets**.
- **Not useful for dynamic data (requires re-sorting).**

---

## **Best Use Cases**
- **Database Indexing** (e.g., searching in SQL databases).
- **Competitive Programming** (used in many problems).
- **Dictionary Lookup** (finding words quickly).
- **Networking Algorithms** (e.g., searching for IP addresses).
- **AI and Machine Learning** (feature selection, decision trees).

---

## **Further Optimizations**
- **Exponential Search**: Speeds up searches in unknown-sized arrays.
- **Fibonacci Search**: Works better for non-random access models.
- **Ternary Search**: Divides the search space into three parts instead of two.
