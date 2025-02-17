# Tips for Two-Pointer Approach in Sorted Arrays

The two-pointer approach is a versatile and efficient technique often used to solve problems involving arrays or lists. It is particularly useful in situations where elements need to be compared, merged, or optimized in a linear scan. Below are some key use cases and explanations.

### Condition for Target Sum:
- If `nums[left] + nums[right] == target`, you've found the pair that matches the target sum.

### If the Current Sum is Too Low (`nums[left] + nums[right] < target`):
- **Move the Left Pointer Rightward**:
  - Since the array is sorted, `nums[left + 1] > nums[left]`, so increasing `left` will increase the sum.
  - This adjustment aims to bring the sum closer to the target.

### If the Current Sum is Too High (`nums[left] + nums[right] > target`):
- **Move the Right Pointer Leftward**:
  - Since the array is sorted, `nums[right - 1] < nums[right]`, so decreasing `right` will decrease the sum.
  - This adjustment brings the sum closer to the target by reducing it.

### Continue Adjusting Pointers:
- Repeat the process until either the target sum is found, or `left` and `right` pointers meet or cross.

## Why It Works
- The sorted order of the array ensures that moving the pointers this way always brings you closer to or hits the target sum.
- This approach optimally runs in **O(n)** time, as opposed to **O(n²)** with a nested loop approach.

## Example
For `nums = [1, 3, 5, 7, 9, 11]` and `target = 10`:
   - Start with `left = 0` and `right = 5`.
   - If `nums[left] + nums[right]` is greater or less than the target, adjust the pointers accordingly to zero in on the target sum efficiently.

This strategy is particularly effective for problems involving pairs and ranges in sorted arrays.

---
## Key Use Cases for the Two-Pointer Approach

## 1. **Sorted Arrays: Target Sum**
- **Condition for Target Sum**: 
  - If `nums[left] + nums[right] == target`, you've found the pair that matches the target sum.
- **When Sum is Too Low**: Move the left pointer to the right.
- **When Sum is Too High**: Move the right pointer to the left.
- **Why It Works**: The sorted order ensures that moving the pointers inward brings you closer to or hits the target sum.
- **Time Complexity**: O(n)

## 2. **Palindrome Checking**
- **Problem**: Check if a string or array is a palindrome.
- **Approach**: Use one pointer starting at the beginning and another at the end of the string/array. Move both pointers towards the center, ensuring each element matches.
- **Time Complexity**: O(n)

## 3. **Merging Two Sorted Arrays**
- **Problem**: Merge two sorted arrays into a single sorted array.
- **Approach**: Use two pointers—one for each array—comparing the elements and inserting the smaller element into the result array.
- **Time Complexity**: O(n + m), where n and m are the sizes of the two arrays.

## 4. **Subarrays with a Given Sum**
- **Problem**: Find subarrays that sum to a target value.
- **Approach**: Use two pointers to maintain a sliding window. Adjust the window size depending on whether the current sum is less than or greater than the target.
- **Time Complexity**: O(n)

## 5. **Removing Duplicates in Sorted Arrays**
- **Problem**: Remove duplicates in-place from a sorted array.
- **Approach**: Use one pointer to track unique elements and another pointer to iterate through the array, skipping duplicates.
- **Time Complexity**: O(n)

## 6. **Intersection of Two Sorted Arrays**
- **Problem**: Find the intersection of two sorted arrays.
- **Approach**: Use two pointers, one for each array. Move the pointers forward, comparing elements. If they match, add it to the result and move both pointers.
- **Time Complexity**: O(n + m)

## 7. **Container With Most Water**
- **Problem**: Given an array representing heights, find the container that can hold the most water.
- **Approach**: Place pointers at both ends of the array. Calculate the area between them and move the pointer pointing to the shorter height inward to maximize the area.
- **Time Complexity**: O(n)

## 8. **3-Sum Problem**
- **Problem**: Find all unique triplets in an array that sum to zero.
- **Approach**: Sort the array first. For each element, use two pointers to find pairs that sum to the negative of the current element.
- **Time Complexity**: O(n²)

## 9. **Sliding Window Maximum**
- **Problem**: Given an array and a sliding window size, find the maximum value in each window.
- **Approach**: Use two pointers to represent the window, updating the maximum value as the window slides across the array.
- **Time Complexity**: O(n)

## Benefits of the Two-Pointer Approach:
- **Time Efficiency**: Often reduces the time complexity from O(n²) to O(n) in problems that involve searching, comparing, or merging elements in arrays or lists.
- **Space Efficiency**: Typically uses O(1) space, as it only requires a few pointers to keep track of positions in the array.

References: https://www.youtube.com/watch?v=VEPCm3BCtik 
