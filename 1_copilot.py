# Task_A: create a list of three students
students = ["Jon", "Kim", "Lee"]

# Task_D: change Jon to John
students[0] = "John"

# Task_C: add Sara and Miko to the list after creation
students.append("Sara")
students.append("Miko")

# Task_B: function to greet each student and show total
def greet_students(student_list):
    for student in student_list:
        print(f"Hi {student}")
    print(f"Total number of students: {len(student_list)}")

# Call the function
greet_students(students)



