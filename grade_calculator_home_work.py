num_subjects = int (input ("How many subjects do you have?"))
total_grades = 0

for i in range (1, num_subjects+1):
    subject_name = input (f"Enter the name of subject {i}:")
    grade = int (input(f"Enter the grade for {subject_name}:"))
    total_grades += grade

average_grade = total_grades / num_subjects

print (f"Your average grade is: {round(average_grade)}")
