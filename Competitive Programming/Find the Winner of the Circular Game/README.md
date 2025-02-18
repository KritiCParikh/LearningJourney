## Problem Explanation

This problem is based on a variation of the **Josephus problem**. In this problem, `n` friends are sitting in a circle, and every `k`-th person is eliminated. The goal is to determine which person will be the last one remaining.

### Formula for Josephus Problem:

Given `n` people and every `k`-th person being eliminated, the position of the winner (0-based indexing) is determined by the formula:

Josephus(n, k) = (Josephus(n - 1, k) + k) % n


Where:
- `n` is the number of people.
- `k` is the counting step.

### Base Case:
When there is only one person left (i.e., `n = 1`), the winner is the 0th index (0-based).

### Approach:

To solve the problem iteratively:
1. Start with the base case, where the winner is 0 (0-based index) when there is only 1 person.
2. For each additional person (from 2 to `n`), calculate the winner's position using the above formula.
3. Finally, return the winner's position adjusted to 1-based indexing.

### Solution in Python:

```python
def findTheWinner(n, k):
    winner = 0  # Start with the base case where only 1 person is left
    for i in range(2, n + 1):
        winner = (winner + k) % i  # Update the winner's position
    return winner + 1  # Convert to 1-based indexing

# Test Cases
print(findTheWinner(5, 2))  # Output: 3
print(findTheWinner(6, 5))  # Output: 1
```

### Explanation of Code:

#### Initialization:
- `winner = 0` corresponds to the base case where there is only one person (the first person in 0-based indexing).

#### Loop:
- We iterate from 2 to `n`, and at each step, we calculate the position of the winner by considering the last eliminated person.

#### Winner Calculation:
- `(winner + k) % i` ensures that the counting wraps around the circle correctly.

#### Return:
- The final winner is returned in 1-based indexing, so we add 1 to the result.

### Time Complexity:
- The time complexity is **O(n)** because we iterate through the range from 2 to `n`, and each iteration is a constant-time operation.

### Space Complexity:
- The space complexity is **O(1)** because we only use a constant amount of space, regardless of the size of `n`.