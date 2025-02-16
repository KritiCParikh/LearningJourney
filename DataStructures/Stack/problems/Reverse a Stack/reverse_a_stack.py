# -*- coding: utf-8 -*-
"""Reverse a Stack

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XJBRltSdVnAyNILUZiRBNOuOgLirSXTw

Problem: Reverse the elements of a stack.

Solution: Use recursion to reverse the stack.

- **Explanation**: We recurse through the stack, popping and pushing elements. Each recursion step performs a constant amount of work (O(1)), and the depth of recursion is proportional to the number of elements in the stack (O(n)).

- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
"""

def reverse_stack(stack):
    if not stack:
        return
    item = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, item)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)