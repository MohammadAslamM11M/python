# Write a program to find the greatest of four numbers entered by user.

# number = []
# greatest = 0

# for i in range(4):
#     number.append(int(input("Enter four numbers: ")))

# for num in number:
#     if(num > greatest):
#         greatest = num

# print(greatest)

# -----------------------------------

# Write a program to find out whether a student has passed or failed if it requires a total of 40%
# and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# totalMarks = 0
# marksForEachSubject = []
# isPass = False

# for i in range(3):
#     marks = int(input("Enter marks: "))
#     totalMarks += marks
#     if(marks >= 33):
#         marksForEachSubject.append(marks)
#     else:
#         isPass = False

# for mark in marksForEachSubject:
#     if(totalMarks/3 >= 40):
#         isPass = True
#     else:
#         isPass = False

# print(isPass)

# 