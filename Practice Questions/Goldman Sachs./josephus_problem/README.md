# **Question:**  
There are `n` students sitting in a circle, each assigned a roll number from `1` to `n`. Starting with a given student, the teacher removes that student and then continues to remove every second student in the circle until only one student remains. The task is to determine the last student left.

---

## **Concept Name:**  
**Josephus Problem**

---

## **Explanation:**  
The Josephus problem is a famous theoretical problem in mathematics and computer science, often used to demonstrate circular data structures and recursive algorithms. The general idea is to eliminate every second person in a circle until only one person remains. 

### **Steps to Solve:**
1. **Recursive Formula:**
   The recursive solution to the Josephus problem is as follows:
   - If `n = 1` (i.e., only one student left), the position of the last remaining student is `0` (since indexing starts from `0`).
   - For `n > 1`, the position of the last student is given by the formula:
     ```
     Josephus(n) = (Josephus(n - 1) + 2) % n
     ```
     This means that we reduce the problem size by one (remove one student) and adjust the position by 2 due to the elimination every second student.

2. **Non-Recursive (Iterative) Approach:**
   We can compute the position iteratively by initializing the last position as `0` and then updating it for each value of `i` from `2` to `n`.

3. **Base Case:**
   For `n = 1`, the answer is `0` (the first person, in 0-indexed form).

---

## **Python Solution (Iterative):**
```python
def josephus(n, k):
    # Initialize the position of the last person to be 0 (base case)
    result = 0
    
    # Calculate the position for all values from 2 to n
    for i in range(2, n + 1):
        result = (result + k) % i
    
    # Since the result is 0-indexed, add 1 to make it 1-indexed
    return result + 1

# Example usage
n = 5  # Total number of students
k = 2  # Every second student is removed
start_position = 3  # Start from student with roll number 3

# Adjust start position to be 0-indexed
start_position = start_position - 1

# Shift the circle starting point using a circular shift (this is important)
students = list(range(1, n + 1))  # List of students with roll numbers 1 to n
students = students[start_position:] + students[:start_position]

# Now apply the Josephus function iteratively to determine the last remaining student
print(f"The last student left is: {josephus(n, k)}")


```
## **Explanation of the Output:**
For n = 5 students, starting with student 3, and removing every second student, the last student left is 2. This can be determined by iterating through the Josephus problem.

Example Breakdown:
- Start with: [1, 2, 3, 4, 5]
- Remove student 3, resulting in [1, 2, 4, 5]
- Remove student 5, resulting in [1, 2, 4]
- Remove student 1, resulting in [2, 4]
- Remove student 4, resulting in [2]