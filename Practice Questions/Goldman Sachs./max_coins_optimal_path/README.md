# **Question:**  
Given a grid of size m x n containing coins represented by 1 and empty cells represented by 0, find the optimal path to collect the most coins. You can only move north or east from any cell.

---

## **Example**  
**Input:**  
```python
grid = [
    [0, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 1, 0]
]
```
**Ouput:**
4

---
# **Explanation:**  
The optimal path is starting at (0,1) → (1,0) → (1,3) → (2,2) → (3,2).  
The path collects 4 coins.

---

## **Concept Name:**  
**Dynamic Programming (Grid Traversal)**  

---

## **Explanation:**  
- Use dynamic programming to store the maximum number of coins collected up to each point in the grid.  
- At each cell, the number of coins collected is the maximum of the coins collected from the north or east direction, plus the coins in the current cell.  
- Initialize the grid for storing the results, and fill it by considering the paths from the north and east.  
- The bottom-right cell of the grid will hold the maximum coins collected following the optimal path.

---

## **Python Solution:**  
```python
def max_coins(grid):
    m, n = len(grid), len(grid[0])
    
    # Create a dp table to store the maximum coins collected up to each cell
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the starting cell
    dp[0][0] = grid[0][0]
    
    # Fill the first row (can only come from the left)
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    
    # Fill the first column (can only come from above)
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # The bottom-right cell contains the result
    return dp[m-1][n-1]

# Example usage
grid = [
    [0, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 1, 0]
]

print(max_coins(grid))  # Output: 4
```
