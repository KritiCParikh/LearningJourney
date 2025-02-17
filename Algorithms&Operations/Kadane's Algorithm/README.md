# Kadane's Algorithm – Maximum Subarray Sum

### **Definition**
Kadane’s Algorithm is an efficient algorithm used to solve the **Maximum Subarray Problem**. It finds the contiguous subarray within a one-dimensional numeric array which has the largest sum. This algorithm operates in linear time and is a prime example of a **Dynamic Programming** approach.

### **Steps**
1. **Initialize two variables**:
   - `current_sum`: Keeps track of the maximum sum of the subarray ending at the current index.
   - `max_sum`: Tracks the maximum sum found so far across all subarrays.
   
2. **Iterate through the array**:
   - For each element, update `current_sum` to be the maximum of:
     - The current element itself (starting a new subarray), or
     - The sum of the current element plus `current_sum` (extending the existing subarray).
   
3. **Update `max_sum`** to be the maximum of `max_sum` and `current_sum` after each iteration.

4. **Return `max_sum`** as the result.

### **Conditions**
- The input array must contain at least one element. If the array is empty, the problem is undefined.
- Kadane’s algorithm works even with arrays that contain negative numbers, as it will reset `current_sum` to the current element if adding the element causes a decrease in the sum.
  
### **Applications**
- **Financial Analysis**: For finding the maximum profit from a series of stock prices over time.
- **Signal Processing**: Identifying the most significant subarray in a signal for maximum power.
- **Image Processing**: Finding regions of interest that provide the most valuable data from an image matrix.
- **Machine Learning**: Used in feature selection for time series problems.

### **Real-Life Examples**
1. **Stock Market**: Given a series of stock price changes (both positive and negative), Kadane's algorithm can find the most profitable subsequence of buy-sell actions.
2. **Daily Temperature Analysis**: Find the longest warm spell by identifying the subarray with the highest temperature sums in a week/month.
3. **Game Scores**: Calculate the maximum sum of consecutive game scores to determine the peak performance streak.

### **Implementation**

```python
def kadane(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

### **Edge Cases**

- **Single Element Array**: If the array has only one element, the answer is that element.
- **All Negative Elements**: Kadane’s algorithm will still work by picking the largest negative number as the maximum subarray.
- **All Positive Elements**: The entire array will be the subarray with the maximum sum.
- **Array with Zeros**: Zeros can be part of the optimal subarray or might be discarded, depending on the surrounding elements.

### **Time Complexity**
- **O(n)**: The algorithm only iterates through the array once, making it linear in terms of time complexity, where **n** is the number of elements in the array.

### **Space Complexity**
- **O(1)**: Only two variables (`current_sum` and `max_sum`) are required to store intermediate results, resulting in constant space complexity.

### **Mathematics Behind This**
Kadane’s algorithm uses the recurrence relation:

current_sum(i)=max(arr[i],current_sum(i−1)+arr[i])

This relation ensures that at each step, the algorithm chooses between starting a new subarray or extending the existing one based on which option yields a higher sum. This is the core of **dynamic programming**.

### **Visualizations**
Imagine an array `A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`. Initially, `current_sum = -2` and `max_sum = -2`. As we move through the array:

- At index 1: `current_sum = 1` → `max_sum = 1`.
- At index 2: `current_sum = -2` → `max_sum = 1`.
- Continue this process, and we get `max_sum = 6`.

### **Comparisons with Similar Algorithms**
- **Brute Force Approach**: Checking all possible subarrays would take **O(n^2)** time, as it requires nested loops to evaluate each subarray.
- **Divide and Conquer**: This approach, although more efficient than brute force (**O(n log n)**), is still slower than Kadane’s algorithm, which is linear.

Kadane’s algorithm is more efficient for this problem than other methods because it uses **dynamic programming** to eliminate unnecessary recalculations, reducing the time complexity.

### **Pros and Cons**
**Pros**:
- **Optimal Time Complexity**: O(n), making it extremely efficient for large datasets.
- **Simple and Elegant**: The algorithm’s logic is straightforward and easy to implement.
- **Works with Negative Numbers**: It’s designed to handle negative numbers, which may be a challenge for other algorithms.

**Cons**:
- **Limited to Contiguous Subarrays**: Kadane's algorithm only works for problems involving contiguous subarrays; it’s not applicable for non-contiguous subarrays.
- **Can’t Handle Multiple Maximum Subarrays**: It only returns the sum of the single subarray with the largest sum, not the actual subarray or multiple maximum subarrays.

### **Best Use Cases**
- **Stock Price Analysis**: Find the most profitable window of time to buy and sell stocks.
- **Performance Tracking**: Track the maximum continuous performance or success streak.
- **Profit Maximization in Operations**: Maximize profits in business scenarios where the values change over time.

### **Further Optimizations**
While Kadane’s algorithm is optimal in terms of time complexity, one possible optimization would involve tracking the subarray itself, not just the sum. To achieve this, we can modify the algorithm to store the start and end indices of the subarray with the maximum sum.

Example: Along with `current_sum` and `max_sum`, track the start and end indices for the subarray, allowing you to return not just the sum but the actual subarray as well.


References: https://www.youtube.com/watch?v=NUWAXbSlsws
