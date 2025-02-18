# **Question:**  
Given a list of students with their scores in different subjects, find the student with the maximum average score.

### Example:
Input:  
students = [ ["Alice", [80, 85, 90]], ["Bob", [75, 80, 95]], ["Charlie", [90, 90, 90]] ]


Output:  
"Charlie" with an average score of 90.0


---

## **Concept Name:**  
**Hashing (Using Dictionary for Aggregation)**

---

## **Explanation:**  
To solve this problem, we can iterate through the list of students, compute the average score for each student, and then find the student with the maximum average score.

### **Steps:**
1. **Store Student Scores:** Use a dictionary to store each student's name and their corresponding scores.
2. **Compute Average:** For each student, calculate the average score by dividing the sum of their scores by the number of subjects.
3. **Track Maximum:** Compare the average score of each student to find the one with the highest average.

---

## **Python Solution:**
```python
def max_average_score(students):
    max_avg = 0
    top_student = ""
    
    # Iterate through the list of students
    for student, scores in students:
        avg_score = sum(scores) / len(scores)  # Calculate the average score
        
        # If the current student's average is greater than the max average, update
        if avg_score > max_avg:
            max_avg = avg_score
            top_student = student
    
    return top_student, round(max_avg, 2)

# Example usage
students = [
    ["Alice", [80, 85, 90]], 
    ["Bob", [75, 80, 95]], 
    ["Charlie", [90, 90, 90]]
]

student, avg = max_average_score(students)
print(f"The student with the maximum average score is {student} with an average score of {avg}")

```
## **Explanation of the Output:**
The function computes the average score for each student:
- Alice: (80 + 85 + 90) / 3 = 85.0
- Bob: (75 + 80 + 95) / 3 = 83.33
- Charlie: (90 + 90 + 90) / 3 = 90.0
Since Charlie has the highest average score, the output will be:

- The student with the maximum average score is Charlie with an average score of 90.0
