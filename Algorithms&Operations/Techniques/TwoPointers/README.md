# Tips for Two-Pointer Approach in Sorted Arrays

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


References: https://www.youtube.com/watch?v=VEPCm3BCtik 
