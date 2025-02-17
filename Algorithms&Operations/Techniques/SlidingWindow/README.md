# Sliding Window Technique

## Definition:
The **sliding window** technique is an optimization method used to create a "window" (a subarray or subsequence) of fixed size that "slides" over the input array or list. This method is particularly useful for problems that involve contiguous subarrays or subsequences, such as finding the maximum/minimum of a subarray or calculating sums.

## Steps:
1. **Initial Window:** Create an initial window of fixed size (or based on problem requirements).
2. **Slide the Window:** Move the window one element at a time, adding the new element at the end and removing the old one from the front.
3. **Update Result:** After each slide, update the result based on the problem's requirement (e.g., finding maximum, sum, etc.).

## Conditions:
- The problem should involve subarrays or subsequences of contiguous elements.
- A fixed-size (or dynamic-size) window is required that slides across the array/list.

## Applications:
1. **Maximum or Minimum in Subarray:** Finding the maximum or minimum in all subarrays of size `k`.
2. **Subarray Sum or Average:** Calculating the sum or average of all subarrays of size `k`.
3. **String Matching Problems:** Detecting substrings with a specific pattern.
4. **Dynamic Programming Problems:** Optimization problems where a sliding window reduces the state space.

## Real-life Examples:
1. **Social Media Feeds:** Analyzing a stream of posts where we look at the past 'k' posts for trend detection.
2. **Network Traffic:** Monitoring the last `k` data packets to detect traffic patterns or errors.
3. **Stock Prices:** Calculating the moving average of stock prices over a sliding time window.

## Implementation:
```python
def sliding_window(arr, k):
    # Initial window
    window_sum = sum(arr[:k])
    result = [window_sum]

    for i in range(k, len(arr)):
        # Slide the window: add new element, remove old
        window_sum += arr[i] - arr[i - k]
        result.append(window_sum)
    
    return result
```

## Edge Cases:
- **Empty Array:** Handle cases where the array is empty.
- **k > Length of Array:** If `k` exceeds the length of the array, there’s no valid subarray.
- **Array of Size 1:** When the array size is 1, the window size `k` will always equal the array size.

## Time Complexity:
- **O(n):** The sliding window technique goes through the list once. Each element is processed only twice (once when entering and once when exiting the window). Hence, the time complexity is linear.

## Space Complexity:
- **O(1):** The space complexity is constant, assuming we only need to store the window sum or a small set of variables. The space used does not grow with the size of the input.

## Mathematics Behind:
The sliding window technique optimizes brute-force solutions by reusing previous calculations. Instead of recalculating sums from scratch for each new subarray, it updates the sum by adding the new element at the end of the window and subtracting the old element that exits.

## Visualizations:
For an array like `[1, 3, 5, 7, 9, 11]` and a window size of 3:
1. **Step 1:** Initial window = `[1, 3, 5]` → sum = `9`
2. **Step 2:** Slide window → new window = `[3, 5, 7]` → sum = `15`
3. **Step 3:** Slide again → new window = `[5, 7, 9]` → sum = `21`

## Dynamic Programming and Sliding Window:
The sliding window technique often falls under **dynamic programming (DP)** because it optimizes problems that involve overlapping subproblems. It reuses results from previously solved subproblems, minimizing redundant calculations.

### Why Sliding Window is Considered DP:
Sliding window addresses problems where solutions to subarrays or subsequences overlap. This overlap is optimized by not recalculating the entire subarray sum or maximum for every window.  
This technique reduces the complexity from **O(n * k)** (brute force) to **O(n)**, making it more efficient.

## Comparisons with Similar Algorithms:
- **Brute Force:** A brute force solution would involve recalculating sums or other values from scratch for every subarray, leading to **O(n*k)** time complexity. Sliding window reduces this to **O(n)**.
  
- **Two Pointers:** Often combined with sliding window, two pointers refer to two indices that denote the start and end of the window. This approach makes sliding window more general and versatile.

## Pros:
- **Efficient:** Reduces time complexity from **O(n*k)** to **O(n)** for problems involving subarrays or contiguous subsequences.
- **Memory Efficient:** For fixed-size windows, space complexity is constant **O(1)**.
- **Versatile:** Applicable to a wide variety of problems, including those in string matching, network analysis, and moving averages.

## Cons:
- **Not Applicable for All Problems:** The problem must involve contiguous subarrays or subsequences.
- **Hard to Apply for Dynamic Window Sizes:** Some problems require adjusting window sizes based on conditions, making the sliding window technique more complex.

## Best Use Cases:
- Finding the maximum sum of a subarray of fixed size.
- Detecting patterns in substrings (e.g., anagram problems).
- Solving problems related to sliding sequences like stock price analysis or network traffic monitoring.

## Further Optimizations:
- **Dynamic Sliding Window Size:** In some problems, the window size might change based on certain conditions (e.g., when a threshold is met). This can be handled by adjusting the window pointers dynamically.
- **Advanced Data Structures:** For problems requiring additional operations (e.g., tracking the maximum/minimum in a window), advanced data structures like **deques** or **heaps** can be used for better performance.

## Common Sliding Window Problems:

1. **Maximum/Minimum Sum of Subarray of Size `k`:**
   - **Problem:** Find the maximum (or minimum) sum of a subarray of size `k` within a given array.
   - **Example:** Given an array `[1, 2, 3, 4, 5]` and `k = 3`, find the subarray of size `3` with the maximum sum.
   
2. **Longest Substring with K Distinct Characters:**
   - **Problem:** Given a string, find the length of the longest substring with exactly `k` distinct characters.
   - **Example:** For the string `"eceba"` and `k = 2`, the longest substring with 2 distinct characters is `"ece"`.

3. **Find All Anagrams in a String:**
   - **Problem:** Given a string and a pattern, find all occurrences of anagrams of the pattern within the string.
   - **Example:** For the string `"cbaebabacd"` and the pattern `"abc"`, the anagrams are at indices `0` and `6`.

4. **Maximum Product Subarray:**
   - **Problem:** Given an integer array, find the contiguous subarray within the array that has the largest product.
   - **Example:** For the array `[2, 3, -2, 4]`, the maximum product subarray is `[2, 3]`.

5. **Subarray with Sum Equals K:**
   - **Problem:** Find all contiguous subarrays that sum up to a given number `k`.
   - **Example:** Given an array `[1, 1, 1, 1]` and `k = 2`, the subarrays are `[1, 1]` at indices `0,1` and `1,2`.

6. **Longest Subarray with Sum Less Than or Equal to K:**
   - **Problem:** Given an array and a number `k`, find the longest subarray where the sum of its elements is less than or equal to `k`.
   - **Example:** For the array `[1, 2, 3, 4, 5]` and `k = 10`, the longest subarray is `[1, 2, 3, 4]`.

7. **Sliding Window Maximum:**
   - **Problem:** Given an array of integers, find the maximum element in every sliding window of size `k`.
   - **Example:** For the array `[1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the maximums in each window are `[3, 3, 5, 5, 6, 7]`.

8. **Longest Substring Without Repeating Characters:**
   - **Problem:** Given a string, find the length of the longest substring without repeating characters.
   - **Example:** For the string `"abcabcbb"`, the longest substring without repeating characters is `"abc"`, with a length of `3`.

9. **Max Consecutive Ones in a Binary Array:**
   - **Problem:** Given a binary array, find the maximum number of consecutive 1’s in the array.
   - **Example:** For the array `[1,1,0,1,1,1]`, the maximum number of consecutive 1’s is `3`.

10. **Minimum Window Substring:**
    - **Problem:** Given two strings `s` and `t`, find the minimum window in `s` which will contain all the characters in `t`.
    - **Example:** For `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window is `"BANC"`.

11. **Subarray with Sum Divisible by 3:**
    - **Problem:** Find all subarrays whose sum is divisible by 3.
    - **Example:** For the array `[3, 6, 2, 5, 1, 7]`, find the subarrays where the sum is divisible by 3. The subarray `[3, 6, 2]` has a sum of `11`, which is divisible by 3.




References: https://youtu.be/SaI2PHJNNVU?si=zYMYc455KpFkvL_Z
