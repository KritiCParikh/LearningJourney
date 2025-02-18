# **Question:**  
Given two fractions represented as an array of two elements (numerator and denominator), the task is to find the reduced fraction which is the sum of the two fractions.

---

## **Concept Name:**  
**Fraction Addition and Simplification**

---

## **Explanation:**  
- To add two fractions, the fractions must first have a common denominator.
- Once the fractions are added, simplify the result by dividing both the numerator and denominator by their greatest common divisor (GCD).
- The GCD can be computed using the Euclidean algorithm.

### **Step-by-Step Approach:**
1. Find the Least Common Denominator (LCD) of the two fractions. This can be done by multiplying the denominators.
2. Adjust both fractions to have the LCD as their denominator.
3. Add the numerators of the two fractions.
4. Simplify the result by finding the GCD of the numerator and the denominator and divide both by the GCD.

---

## **Python Solution:**
```python
import math

def add_fractions(frac1, frac2):
    # Find the Least Common Denominator (LCD)
    denominator = frac1[1] * frac2[1]
    
    # Adjust the numerators to the common denominator
    numerator = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    
    # Simplify the fraction by dividing both numerator and denominator by their GCD
    gcd = math.gcd(numerator, denominator)
    
    return [numerator // gcd, denominator // gcd]

# Example usage
fraction1 = [1, 2]
fraction2 = [1, 3]

result = add_fractions(fraction1, fraction2)
print(result)  # Output: [5, 6]
```


----
## **Explanation of the Output:**
The sum of 1/2 + 1/3 results in the fraction 5/6, which is already in its simplest form.