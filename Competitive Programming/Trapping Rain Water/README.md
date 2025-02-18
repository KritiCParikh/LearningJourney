# Trapping Rain Water

- LeetCode: 42
- Question: https://leetcode.com/problems/trapping-rain-water/description/
- Company: Goldman Sachs.
---

# **Question:**  
Given an array representing the elevation map, where the width of each bar is 1, calculate how much water it can trap after raining.

---

## **Concept Name:**  
**Two-pointer Approach (Optimal Solution)**

---

## **Explanation:**  
The problem involves finding how much water can be trapped between the bars after it rains. The trapped water depends on the heights of the bars and the distance between them.

### **Step-by-Step Approach:**
1. **Two-pointer technique:**
   - Use two pointers, one starting at the beginning of the array and the other at the end.
   - Move the pointers inward, calculating the trapped water at each step.
   - Maintain two variables, `left_max` and `right_max`, to store the maximum height seen so far from the left and right, respectively.
   
2. **Water trapping condition:**
   - At each step, if the bar at the left pointer is shorter than the bar at the right pointer, calculate the water trapped at the left pointer based on the `left_max` height.
   - If the bar at the right pointer is shorter, calculate the water trapped at the right pointer based on the `right_max` height.
   - Continue moving the pointers inward until they meet.
   
3. **Result:**  
   The sum of the trapped water at each position gives the total amount of water trapped.

---

## **Python Solution:**
```python
def trap(height):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1
    
    return water_trapped

# Example usage
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))  # Output: 6

```
## **Explanation of the Output:**
- For the elevation map [0,1,0,2,1,0,1,3,2,1,2,1], the water can be trapped in the following positions:

* Between indices 2 and 3, with 1 unit of water.
* Between indices 4 and 5, with 1 unit of water.
* Between indices 5 and 6, with 2 units of water.
* Between indices 8 and 9, with 2 units of water.
Thus, the total amount of water trapped is 6.
