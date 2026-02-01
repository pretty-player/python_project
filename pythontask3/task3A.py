# 1. Define grading criteria
def get_grade(percentage):
    if percentage >= 90: return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B"
    elif percentage >= 60: return "C"
    else: return "F"

# 2. Collect marks for 5 students
students_data = []
num_students = 5
num_subjects = 3

for i in range(num_students):
    name = input(f"Enter name for student {i+1}: ")
    marks = []
    for j in range(num_subjects):
        mark = float(input(f"  Enter marks for Subject {j+1} (0-100): "))
        marks.append(mark)
    
    total = sum(marks)
    percentage = total / num_subjects
    grade = get_grade(percentage)
    
    # Store data as a dictionary for easy ranking
    students_data.append({
        "name": name,
        "total": total,
        "grade": grade
    })

# 3. Assign Ranks based on total marks
# Sort students by total marks in descending order
students_data.sort(key=lambda x: x["total"], reverse=True)

# 4. Display Final Report
print("\n" + "="*40)
print(f"{'Rank':<5} {'Name':<12} {'Total':<8} {'Grade':<5}")
print("-" * 40)

for index, student in enumerate(students_data):
    rank = index + 1
    print(f"{rank:<5} {student['name']:<12} {student['total']:<8.2f} {student['grade']:<5}")
