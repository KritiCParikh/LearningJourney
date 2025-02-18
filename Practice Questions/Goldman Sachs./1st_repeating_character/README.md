### Question:
Given a string, find the first repeating character whose first appearance is the leftmost. If no character repeats, return `0`.

### Example Input and Output:
- **Input**: `"mariasharapova"`
  **Output**: `"a"`

- **Input**: `"abcdef"`
  **Output**: `0`

- **Input**: `"abac"`
  **Output**: `"a"`

- **Input**: `"xyzxyz"`
  **Output**: `"x"`

### Concept Name:
**Finding the First Repeating Character**

### Explanation:
The goal is to find the first character that repeats in the string. We can do this by iterating through the string and using a set to track the characters we have encountered. As soon as we encounter a character that is already in the set, we return it as the first repeating character.

### Python Solution:

```python
def first_repeating_character(s):
    seen = set()  # Set to keep track of characters we have already seen
    
    # Iterate through the string
    for char in s:
        if char in seen:
            return char  # Return the first repeating character
        seen.add(char)
    
    return 0  # Return 0 if no repeating character is found

# Example usage
print(first_repeating_character("mariasharapova"))  # Output: "a"
print(first_repeating_character("abcdef"))  # Output: 0
print(first_repeating_character("abac"))  # Output: "a"
print(first_repeating_character("xyzxyz"))  # Output: "x"


```
## **Explanation of the Output:**
1. Set for Tracking: We use a set (seen) to keep track of the characters we have already encountered as we iterate through the string.
2. Iteration and Checking: For each character, we check if it is already in the set. If it is, we return it as the first repeating character.
3. Return 0: If no repeating character is found after checking all characters, we return 0.


## **Example 1:**
first_repeating_character("mariasharapova")
# Output: "a"



## **Example 2:**
first_repeating_character("abcdef")
# Output: 0




## **Example 3:**
first_repeating_character("abac")
# Output: "a"


## **Example 4:**
first_repeating_character("xyzxyz")
# Output: "x"
