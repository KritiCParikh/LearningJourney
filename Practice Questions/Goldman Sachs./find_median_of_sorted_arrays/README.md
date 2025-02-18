# **Question:**  
Given two sorted arrays, find the median of them.

---

## **Concept Name:**  
**Binary Search (Optimal Approach for Finding Median)**

---

## **Explanation:**  
The problem asks to find the median of two sorted arrays. The median is the middle element when the arrays are combined and sorted. If the combined length is odd, it's the middle element; if even, it's the average of the two middle elements.

To achieve this efficiently (in O(log(min(n, m))) time complexity), we use binary search to partition the arrays into two halves such that:
- The left half contains the same number of elements as the right half (or one more if the combined length is odd).
- The largest element on the left side is less than or equal to the smallest element on the right side.

### **Step-by-Step Approach:**
1. We start by ensuring that we are always binary searching on the smaller array (to minimize time complexity).
2. Partition both arrays in such a way that the left half contains elements less than or equal to those in the right half.
3. Calculate the median based on the partitioning:
   - If the combined length is odd, the median is the largest element in the left half.
   - If the combined length is even, the median is the average of the largest element in the left half and the smallest element in the right half.

---

## **Python Solution:**
```python
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        # Get max and min on the left and right of the partition
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]
        
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]
        
        # Check if the partition is correct
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # If total length is odd, the median is the max of the left elements
            if (m + n) % 2 == 1:
                return max(maxLeft1, maxLeft2)
            # If total length is even, the median is the average of the max of left and min of right
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
        elif maxLeft1 > minRight2:
            right = partition1 - 1
        else:
            left = partition1 + 1

# Example usage
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.5
```
## **Explanation of the Output:**
- For arrays [1, 3] and [2], the median is 2.0 because when merged, the array is [1, 2, 3], and the middle element is 2.
- For arrays [1, 2] and [3, 4], the median is 2.5 because when merged, the array is [1, 2, 3, 4], and the median is the average of 2 and 3, which is 2.5.
