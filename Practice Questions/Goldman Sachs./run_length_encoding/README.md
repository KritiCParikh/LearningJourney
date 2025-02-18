# **Question:**  
Given a string consisting of consecutive repeating characters, compress it such that each group of repeating characters is represented by the character followed by its count.  

## **Example**  
**Input:** `"aaabbbbbccccdaa"`  
**Output:** `"a3b5c4d1a2"`  

---

## **Concept Name:**  
**Run-Length Encoding (String Compression)**  

---

## **Explanation:**  
- We traverse the string while keeping track of consecutive occurrences of each character.  
- When a character changes, we append the previous character and its count to the result.  
- Finally, we handle the last character's count and return the compressed string.  

---

## **Python Solution:**  
```python
def run_length_encoding(s):
    if not s:
        return ""
    
    compressed = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1  
    
    compressed.append(s[-1] + str(count))  # Add the last character group
    return "".join(compressed)
```

# Example usage
s = "aaabbbbbccccdaa"
print(run_length_encoding(s))  # Output: "a3b5c4d1a2"
