students = {}

for i in range(5):
    print(f"\nEnter details for Student {i+1}")
    name = input("Name: ")
    marks = float(input("Marks: "))
    students[name] = marks

def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

topper = max(students, key=students.get)
top_marks = students[topper]

average = sum(students.values()) / len(students)

print("\n===== Student Results =====")

for name, marks in students.items():
    grade = assign_grade(marks)
    print(f"{name} → Marks: {marks}, Grade: {grade}")

print("\nTopper:", topper, "with", top_marks, "marks")
print("Class Average:", round(average, 2))