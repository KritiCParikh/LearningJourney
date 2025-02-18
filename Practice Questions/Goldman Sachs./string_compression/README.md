### Question:
Given a string, compress it using the following method:
- Begin with the first character of the string.
- Count how many times the character repeats consecutively.
- Replace the character with the character followed by the count of its occurrences.
- If the compressed string is not shorter than the original string, return the original string.

### Concept Name:
**String Compression**

### Explanation:
This problem is about compressing the input string by replacing consecutive duplicate characters with the character followed by the count of occurrences. If the compressed string results in a length greater than or equal to the original string, we should return the original string.

### Python Solution:

```python
def compress_string(s):
    n = len(s)
    if n == 0:
        return s
    
    # Initialize variables
    compressed = []
    count = 1
    
    # Traverse the string
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1  # Increase count if the character is the same as the previous one
        else:
            # Append the current character and its count to the compressed string
            compressed.append(s[i - 1] + str(count))
            count = 1  # Reset the count
    
    # Append the last character and its count
    compressed.append(s[-1] + str(count))
    
    # Join the list into a compressed string
    compressed_str = ''.join(compressed)
    
    # Return the original string if the compressed string is longer
    return compressed_str if len(compressed_str) < n else s

# Example usage
s = "aabcccccaaa"
print(compress_string(s))  # Output: "a2b1c5a3"

```
## **Explanation of the Output:**
1. Initialization: We start by checking if the string is empty. If it is, we return the string as is. We initialize an empty list compressed to store the resulting compressed string and a count variable to track the occurrences of each character.
2. Traverse the String: We loop through the string and compare each character with the previous one:
- If the character is the same as the previous one, we increment the count.
- If the character is different, we append the previous character and its count to the compressed list and reset the count to 1.
3. Final Append: After the loop, we add the last character and its count to the compressed list.
4. Return Result: We join the compressed list into a string and compare its length to the original string. If the compressed string is shorter, we return it; otherwise, we return the original string.

## **Example Input:**
s = "aabcccccaaa"



## **Output:**
"a2b1c5a3"

## **Time Complexity:**
O(n): Where n is the length of the string. We loop through the string once and perform constant-time operations within the loop.

## **Space Complexity:**
O(n): The space complexity is O(n) because we store the compressed string in a list, which in the worst case could store up to n characters.


