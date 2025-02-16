# -*- coding: utf-8 -*-
"""Tower of Hanoi

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XJBRltSdVnAyNILUZiRBNOuOgLirSXTw

Problem: Solve the Tower of Hanoi puzzle using stacks.

Solution: Use recursion and stacks to move disks between pegs while adhering to the rules. (No code provided here due to complexity, but it follows recursive stack operations.)

- Time Complexity: O(2^n)

- Space Complexity: O(n)

- Explanation: The recursive approach has two recursive calls at each level and makes 2^n moves, which results in an exponential time complexity. The space complexity is O(n) due to the recursion stack.
"""

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, source, destination)

n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'B', 'C')