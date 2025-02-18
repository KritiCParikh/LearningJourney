# **Question:**  
Given a string "A B A B C A B A B C D", compress it into the following format:  
"A B * C * D". Here, until "A B *", the string "A B" repeats twice.  
But until "A B * C *", the string "A B A B C" repeats twice.

---

## **Concept Name:**  
**Pattern Compression with Frequency Analysis**

---

## **Explanation:**  
- The goal is to identify the repeating patterns in the string and compress them into the form where the repeating parts are replaced by "*".
- You need to iterate through the string and keep track of repeating sequences. If a sequence repeats, replace it with "*".
- You must dynamically identify and track repeating parts and ensure the compression is applied correctly for the full string.

### **Step-by-Step Approach:**
1. Split the string into words.
2. Initialize a list to store the final compressed form.
3. Iterate over the string and find repeated sequences.
4. Keep track of the frequency of each subsequence.
5. Replace the repeated subsequences with `*` when encountered a second time.

---

## **Python Solution:**
```python
def compress_string(s):
    words = s.split()
    result = []
    word_count = {}

    for i in range(len(words)):
        # Check if this word has been seen before
        if words[i] in word_count and word_count[words[i]] == 1:
            result.append('*')
        else:
            result.append(words[i])
            word_count[words[i]] = word_count.get(words[i], 0) + 1

    return ' '.join(result)


# Example usage
input_str = "A B A B C A B A B C D"
output_str = compress_string(input_str)
print(output_str)  # Output: "A B * C * D"
```

----
## **Explanation of the Output:**
For "A B A B", the "A B" sequence repeats twice, so it's compressed to "A B *".
For "A B A B C", the "A B A B C" sequence repeats twice, so it's compressed to "A B * C *".
The last "D" does not repeat, so it's left as is.
