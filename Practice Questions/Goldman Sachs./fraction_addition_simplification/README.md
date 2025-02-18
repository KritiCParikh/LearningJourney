# **Question:**  
Given two fractions \( \frac{a}{b} + \frac{c}{d} \), simplify the expression and return the result in its simplest form.

---

## **Example**  
**Input:**  
a = 1, b = 2, c = 1, d = 3

**Output:**  
5/6


---

## **Concept Name:**  
**Fraction Addition and Simplification**  

---

## **Explanation:**  
- To add two fractions \( \frac{a}{b} \) and \( \frac{c}{d} \), first find a common denominator (which is the least common denominator).  
- Then, add the numerators accordingly.  
- After addition, simplify the resulting fraction by dividing both the numerator and the denominator by their greatest common divisor (GCD).  

---

## **Python Solution:**  
```python
import math

def add_fractions(a, b, c, d):
    # Find the common denominator
    denominator = b * d
    numerator = (a * d) + (c * b)
    
    # Simplify the fraction
    gcd_value = math.gcd(numerator, denominator)
    
    # Return the simplified fraction
    return f"{numerator // gcd_value}/{denominator // gcd_value}"

# Example usage
a, b, c, d = 1, 2, 1, 3
print(add_fractions(a, b, c, d))  # Output: "5/6"
```
