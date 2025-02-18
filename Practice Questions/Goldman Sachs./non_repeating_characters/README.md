### Question:
Given a string, write a function to find the first non-repeating character in it. If there is no non-repeating character, return `0`. 

### Example Input and Output:
- **Input**: `"aabbccd"`
  **Output**: `'d'`

- **Input**: `"abbccddee"`
  **Output**: `'a'`

- **Input**: `"iijjkkllmm"`
  **Output**: `0`

### Concept Name:
**Character Frequency Counting (Using a Hash Map)**

### Explanation:
To find the first non-repeating character in a string:
1. Count the frequency of each character in the string.
2. Iterate through the string and check the frequency of each character.
3. Return the first character that has a frequency of 1.
4. If no such character is found, return `0`.

### Python Solution:

```python
from collections import Counter

def first_non_repeating_char(s):
    # Count the frequency of each character in the string
    char_count = Counter(s)
    
    # Iterate through the string to find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If no non-repeating character is found, return 0
    return 0

# Example usage
print(first_non_repeating_char("aabbccd"))  # Output: 'd'
print(first_non_repeating_char("abbccddee"))  # Output: 'a'
print(first_non_repeating_char("iijjkkllmm"))  # Output: 0


```
## **Explanation of the Output:**
1. Counter: We use Counter from the collections module to count the occurrences of each character in the string. char_count is a dictionary-like object where keys are characters and values are their counts.
2. First Iteration: We iterate through the string and check the frequency of each character using char_count[char]. The first character with a count of 1 is returned.
3. If No Non-Repeating Character: If no non-repeating character is found in the string, the function returns 0.

## **Example 1:**
s = "aabbccd"

print(first_non_repeating_char(s))  # Output: 'd'

## **Example 2:**
s = "abbccddee"

print(first_non_repeating_char(s))  # Output: 'a'

## **Example 3:**
s = "iijjkkllmm"
print(first_non_repeating_char(s))  # Output: 0



