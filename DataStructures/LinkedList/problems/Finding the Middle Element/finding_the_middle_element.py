# -*- coding: utf-8 -*-
"""Finding the Middle Element.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XJBRltSdVnAyNILUZiRBNOuOgLirSXTw

Problem: Find the middle element of a linked list.

Explanation: Use the slow and fast pointers technique where the slow pointer moves one step and fast pointer moves two steps. When fast reaches the end, slow will be at the middle.


---


Time Complexity: O(n)

Space Complexity: O(1)
"""

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow