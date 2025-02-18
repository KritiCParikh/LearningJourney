# **Question:**  
Given an array where each element is a sub-array of length two, where:  
- The first index contains the student’s name.  
- The second index contains the marks scored.  

Find the maximum average score among all students. Each student may have multiple scores across different subjects.

---

## **Example**  
**Input:**  
```python
students = [
    ["Alice", 85], 
    ["Bob", 90], 
    ["Alice", 95], 
    ["Bob", 80], 
    ["Alice", 88]
]
```
**Output:** 
```
Maximum average score: 89.33 (Alice)
```

## **Concept Name:**  
**Hashing (Using Dictionary for Aggregation)**  

---

## **Explanation:**  
- Use a dictionary to store each student's total marks and count of subjects.  
- Iterate through the list, updating total marks and count for each student.  
- Compute the average for each student and track the maximum.  
- Return the student with the highest average.  

---

## **Python Solution:**  
```python
from collections import defaultdict

def max_average_score(students):
    scores = defaultdict(lambda: [0, 0])  # {student: [total_marks, count]}
    
    for name, marks in students:
        scores[name][0] += marks  # Add marks
        scores[name][1] += 1  # Increment count
    
    max_avg = 0
    top_student = ""

    for name, (total, count) in scores.items():
        avg = total / count
        if avg > max_avg:
            max_avg = avg
            top_student = name
    
    return top_student, round(max_avg, 2)

# Example usage
students = [
    ["Alice", 85], 
    ["Bob", 90], 
    ["Alice", 95], 
    ["Bob", 80], 
    ["Alice", 88]
]

student, avg = max_average_score(students)
print(f"Maximum average score: {avg} ({student})")  # Output: Maximum average score: 89.33 (Alice)


