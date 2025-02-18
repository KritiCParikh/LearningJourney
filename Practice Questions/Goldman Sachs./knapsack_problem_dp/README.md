# **Question:**  
Solve the 0/1 Knapsack problem using Dynamic Programming (DP).

---

## **Concept Name:**  
**Dynamic Programming (DP) - 0/1 Knapsack Problem**

---

## **Explanation:**  
The 0/1 Knapsack problem involves selecting a subset of items, each with a weight and value, to maximize the total value without exceeding a given weight capacity. The challenge is to determine the maximum value we can achieve for a given capacity using a dynamic programming approach.

### **Dynamic Programming Approach:**
1. **State Definition:**  
   Let `dp[i][w]` represent the maximum value we can obtain by considering the first `i` items and a knapsack capacity `w`.

2. **Recurrence Relation:**  
   - If we don't include the item `i`, the value is `dp[i-1][w]`.
   - If we include the item `i`, the value is `dp[i-1][w - weight[i]] + value[i]` (provided the weight of item `i` is less than or equal to `w`).
   - The recurrence becomes:
     ```  
     dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight[i]] + value[i])
     ```
3. **Base Case:**  
   - For `dp[0][w]` (i.e., considering 0 items), the value is 0 for all capacities `w`.

4. **Result:**  
   The result is found in `dp[n][W]`, where `n` is the total number of items and `W` is the knapsack capacity.

---

## **Python Solution:**
```python
def knapsack(weights, values, W, n):
    # Create a 2D DP array
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]

# Example usage
weights = [1, 2, 3, 8, 4, 5]  # Weights of items
values = [20, 5, 10, 40, 15, 25]  # Corresponding values
W = 10  # Maximum weight capacity of the knapsack
n = len(weights)  # Number of items

print(knapsack(weights, values, W, n))  # Output: 60


```
## **Explanation of the Output:**
For the weights [1, 2, 3, 8, 4, 5] and values [20, 5, 10, 40, 15, 25], and a knapsack capacity of 10, the maximum value that can be obtained is 60. This is achieved by selecting the items with weights 3, 4, and 5, which give a total value of 60.