# Simple Grade Tracker
name = input("enter student name: ")
marks = int(input("enter marks: "))
if marks >=90 :
    grade = "A"
elif marks>= 75:
    grade = "B"
elif marks>= 50:
    grade = "c"
else: grade = "fail"
print("student:", name)
print("grade:", grade)    

