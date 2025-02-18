# **Question:**  
Given an array of positive integers and a target sum, find the minimum subarray whose sum is at least the target.

---

## **Concept Name:**  
**Sliding Window Approach**

---

## **Explanation:**  
The task is to find the smallest contiguous subarray with a sum greater than or equal to a given target. The sliding window technique is optimal for this kind of problem, where we expand the window to accumulate the sum and shrink the window from the left side when the sum is large enough.

### **Step-by-Step Approach:**
1. **Sliding Window:**
   - Start with two pointers, `left` and `right`, both at the beginning of the array.
   - Expand the window by moving the `right` pointer to include more elements and accumulate the sum of the current window.
   - When the sum of the window is greater than or equal to the target, try to shrink the window by moving the `left` pointer to the right while keeping the sum valid.
   - Track the minimum length of the window that satisfies the condition.

2. **Edge case:**
   - If no valid subarray is found, return 0 or an indication of no solution.

---

## **Python Solution:**
```python
def minSubArrayLen(target, nums):
    left, current_sum, min_len = 0, 0, float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # Shrink the window from the left as much as possible while the sum is valid
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

# Example usage
nums = [1, 2, 5, 6, 11, 2]
target = 12
print(minSubArrayLen(target, nums))  # Output: 2 (Subarray [11, 2])

```
## **Explanation of the Output:**
For the array [1, 2, 5, 6, 11, 2] and target sum 12, the minimum subarray whose sum is at least 12 is [11, 2], and its length is 2.

