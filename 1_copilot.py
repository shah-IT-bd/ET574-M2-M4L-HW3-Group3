#Task_A

# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
# Add Sara and Miko to the list after creation
students.append("Sara")
students.append("Miko")
# function to print ‘Hi name’ for each student in the list
def greet_students(student_list):
    for student in student_list:
        print(f"Hi {student}")
    print(f"Total number of students: {len(student_list)}")
# call the function
greet_students(students)
