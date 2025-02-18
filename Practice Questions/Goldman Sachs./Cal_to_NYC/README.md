### Question:
You are an avid rock collector who lives in Southern California. Some rare and desirable rocks just became available in New York, so you are planning a cross-country road trip. There are several other rare rocks that you could pick up along the way. You have been given a grid filled with numbers, representing the number of rare rocks available in various cities across the country. Your objective is to find the optimal path from So_Cal to New_York that would allow you to accumulate the most rocks along the way.

**Note**: You can only travel either north (up) or east (right).

### Parts of the Problem:
- **(a)** Find the optimal path from Southern California to New York that allows you to accumulate the maximum number of rocks.
- **(b)** Consider adding some additional tests to ensure the solution works for other edge cases.
- **(c)** Implement the function `optimalPath()` to find the solution.
- **(d)** Example:
    ```plaintext
    ^ {{0, 0, 0, 0, 5}, 
    New_York (finish) N {0, 1, 1, 1, 0}, 
    So_Cal (start) {2, 0, 0, 0, 0}} S v
    ```
    The total for this example would be 10 (2+0+1+1+1+0+5).

### Concept Name:
**Dynamic Programming (Max Path Sum in Grid)**

### Explanation:
This problem can be solved using dynamic programming. The idea is to create a new matrix `dp` where each cell stores the maximum number of rocks that can be collected from the start to that point. You can only move either east (right) or north (up), so the value at each cell will be the maximum of the value from the cell to the left (east) or the cell below (north) plus the number of rocks at that position.

- **Base Case**: The number of rocks at the starting position is just the value of the starting position itself.
- **Recursive Relation**: For each other cell, the value will be the maximum of the two possible moves (up or right) plus the current cell's value.

### Python Solution:

```python
def optimalPath(grid):
    rows, cols = len(grid), len(grid[0])

    # Create a dp array to store the maximum number of rocks collected to each cell
    dp = [[0] * cols for _ in range(rows)]
    
    # Initialize the start position (bottom left corner, i.e., So_Cal)
    dp[0][0] = grid[0][0]
    
    # Fill the first row (only move east)
    for col in range(1, cols):
        dp[0][col] = dp[0][col-1] + grid[0][col]
    
    # Fill the first column (only move north)
    for row in range(1, rows):
        dp[row][0] = dp[row-1][0] + grid[row][0]
    
    # Fill the rest of the dp table
    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = max(dp[row-1][col], dp[row][col-1]) + grid[row][col]
    
    # The bottom-right cell will have the maximum number of rocks collected
    return dp[rows-1][cols-1]

# Example usage
grid = [
    [2, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 5]
]

print(optimalPath(grid))  # Output: 10

```
## **Explanation of the Output:**
1. Grid Initialization: The dp matrix is created to store the maximum number of rocks that can be collected at each cell.
2. First Row Initialization: Since you can only move east, the first row is filled by accumulating values from left to right.
3. First Column Initialization: Similarly, the first column is filled by accumulating values from top to bottom, as you can only move north.
4. Filling the dp Table: For each cell, the value is the maximum of the value from the left (east) or from below (north), plus the number of rocks at that cell.
5. Result: The bottom-right corner (dp[rows-1][cols-1]) will contain the total number of rocks collected on the optimal path.

## **Example Input:**
grid = [
    [2, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 5]
]



## **Output:**
10



