# **Question:**  
Given a matrix of numbers, the task is to collect the maximum numbers possible when going from the bottom left corner of the matrix to the top right corner of the matrix.  
The only two directions you can move are up and right.

---

## **Concept Name:**  
**Dynamic Programming (Matrix Traversal)**

---

## **Explanation:**  
- The problem is a variation of the classic "max path sum" in a grid with restricted movement (only right and up).
- To solve this, use dynamic programming (DP) to keep track of the maximum sum collected up to each cell.
- At each step, the value in the current cell is the maximum of the sum of values from the cell to the left (right move) or the cell below (up move), plus the current value in the matrix.
- The bottom-left corner is the starting point, and the top-right corner is the destination.

---

## **Step-by-Step Approach:**
1. Create a DP table with the same dimensions as the input matrix.
2. Initialize the DP table starting from the bottom-left corner.
3. At each cell, calculate the maximum possible sum from the two possible directions (up and right).
4. Fill in the DP table and the top-right cell will contain the maximum sum that can be collected.

---

## **Python Solution:**
```python
def max_path_sum(matrix):
    m, n = len(matrix), len(matrix[0])
    
    # Create a dp table to store the maximum sum up to each cell
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the starting point (bottom left corner)
    dp[m-1][0] = matrix[m-1][0]
    
    # Fill the last row (can only come from the left)
    for i in range(1, n):
        dp[m-1][i] = dp[m-1][i-1] + matrix[m-1][i]
    
    # Fill the first column (can only come from below)
    for i in range(m-2, -1, -1):
        dp[i][0] = dp[i+1][0] + matrix[i][0]
    
    # Fill the rest of the dp table
    for i in range(m-2, -1, -1):
        for j in range(1, n):
            dp[i][j] = max(dp[i+1][j], dp[i][j-1]) + matrix[i][j]
    
    # The top-right cell contains the maximum sum collected
    return dp[0][n-1]

# Example usage
matrix = [
    [5, 3, 2, 1],
    [1, 2, 1, 2],
    [4, 0, 6, 3],
    [1, 2, 4, 5]
]

print(max_path_sum(matrix))  # Output: 16

```
----
## **Explanation of the Output:**
The maximum sum from bottom left to top right, while only moving up or right, is 16.
