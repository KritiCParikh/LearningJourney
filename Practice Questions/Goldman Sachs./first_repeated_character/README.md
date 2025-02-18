### Question:
Given a string, find the first character that repeats. If no character repeats, return an empty string.

### Concept Name:
**Hashing (Using a Set or Dictionary)**

### Explanation:
To solve this problem, you can use a set to track the characters you have encountered while iterating through the string. The first character that you encounter more than once is the repeated character with the leftmost first appearance. If no character repeats, return an empty string.

### Python Solution:

```python
def firstRepeatingCharacter(s):
    seen = set()  # Set to store characters we've encountered
    
    for char in s:
        if char in seen:
            return char  # Return the character if it has appeared before
        seen.add(char)  # Add the character to the set
    
    return ""  # Return empty string if no repeating character is found

# Example usage
s = "abcabc"
print(firstRepeatingCharacter(s))  # Output: "a"

s = "abcdef"
print(firstRepeatingCharacter(s))  # Output: ""

```
## **Explanation of the Output:**
1. Initialization: We create an empty set seen to store the characters we encounter.
2. Iterate Through the String: We iterate over each character in the string:
- If the character is already in the set, it means we have encountered it before, so we return this character as the first repeating character.
- If the character is not in the set, we add it to the set and continue.
3. Return Result: If we complete the loop without finding any repeated character, we return an empty string.

## **Example Input:**
s = "abcabc"


## **Output:**
"a"

