### Question:
Implement a function that takes two unsigned integers as arguments, namely numerator and denominator, and outputs a string representing the fraction in decimal form. If there is a repeating and non-terminating digit that appears in the decimal form, write that in parenthesis.

### Example Input and Output:
- **Input**: `2, 5`
  **Output**: `"0.4"`

- **Input**: `1, 2`
  **Output**: `"0.5"`

- **Input**: `1, 3`
  **Output**: `"0.(3)"`

- **Input**: `12, 5`
  **Output**: `"2.4"`

- **Input**: `11, 20`
  **Output**: `"0.55"`

- **Input**: `5, 3`
  **Output**: `"1.(6)"`

### Concept Name:
**Long Division for Decimal Representation with Detection of Repeating Cycles**

### Explanation:
To solve this problem:
1. Perform the division manually to get the integer part and the decimal part.
2. Track the remainders during the decimal calculation. If a remainder repeats, it means a repeating decimal starts at that point.
3. If a remainder repeats, enclose the repeating part in parentheses.

### Python Solution:

```python
def fraction_to_decimal(numerator, denominator):
    # Edge case: If the numerator is 0, return "0"
    if numerator == 0:
        return "0"
    
    # Determine the sign of the result
    sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
    
    # Work with absolute values to simplify the calculation
    numerator, denominator = abs(numerator), abs(denominator)
    
    # Calculate the integer part of the division
    integer_part = numerator // denominator
    remainder = numerator % denominator
    
    # If there is no remainder, return the result as an integer
    if remainder == 0:
        return f"{sign}{integer_part}"
    
    # Prepare for the decimal part
    decimal_part = ""
    remainder_map = {}
    
    # Perform long division to calculate the decimal part
    index = 0
    while remainder != 0:
        # If the remainder repeats, we have a repeating decimal
        if remainder in remainder_map:
            repeat_index = remainder_map[remainder]
            decimal_part = decimal_part[:repeat_index] + f"({decimal_part[repeat_index:]})"
            return f"{sign}{integer_part}.{decimal_part}"
        
        # Store the index of the remainder
        remainder_map[remainder] = index
        
        # Update the remainder by multiplying by 10
        remainder *= 10
        decimal_part += str(remainder // denominator)
        remainder %= denominator
        index += 1
    
    # Return the final result
    return f"{sign}{integer_part}.{decimal_part}"

# Example usage
print(fraction_to_decimal(2, 5))  # Output: "0.4"
print(fraction_to_decimal(1, 2))  # Output: "0.5"
print(fraction_to_decimal(1, 3))  # Output: "0.(3)"
print(fraction_to_decimal(12, 5))  # Output: "2.4"
print(fraction_to_decimal(11, 20))  # Output: "0.55"
print(fraction_to_decimal(5, 3))  # Output: "1.(6)"


```
## **Explanation of the Output:**
1. Sign Handling: We check if the result should be negative by using the XOR (^) operation on the signs of the numerator and denominator.
2. Integer Part: The integer part is calculated using floor division (//), and the remainder is obtained using the modulo operator (%).
3. Decimal Part Calculation: We use long division to calculate the decimal part. At each step, we multiply the remainder by 10, divide by the denominator, and append the result to the decimal part.
4. Repeat Detection: We store the remainder at each step in a dictionary (remainder_map). If we encounter the same remainder again, it indicates that the decimal has started repeating, and we insert parentheses around the repeating part.
5. Edge Case: If the numerator is 0, we directly return "0".


## **Example 1:**
fraction_to_decimal(2, 5)
# Output: "0.4"


## **Example 2:**
fraction_to_decimal(1, 3)
# Output: "0.(3)"



## **Example 3:**
fraction_to_decimal(5, 3)
# Output: "1.(6)"

## **Example 4:**
fraction_to_decimal(12, 5)
# Output: "2.4"
