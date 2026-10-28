# main.py

from Stud.marks import total_marks, percentage
from Stud.grade import calculate_grade
from Stud.attendance import attendance_eligibility

name = input("Enter student name: ")

n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

attendance = float(input("Enter attendance percentage: "))

total = total_marks(marks)
percent = percentage(marks)
grade = calculate_grade(percent)
eligibility = attendance_eligibility(attendance)

print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percent, "%")
print("Grade:", grade)
print("Attendance:", attendance, "%")
print("Eligibility:", eligibility)