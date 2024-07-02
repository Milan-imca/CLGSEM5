# - Take Student name , course , sem ,marks (5 subjects) , total and average (given on 21/6/24)

name = input("Enter Student name : ")
course = input("Enter the course name : ")
semester = input("Enter the semester : ")
marks = []

for i in range(1,6):
    mark = int(input(f"Enter the marks of Subject-{i} : "))
    marks.append(mark)
    
total_marks = sum(marks)
average_marks = float(total_marks/5)

print(f"Student name : {name}")
print(f"Course : {course}")
print(f"Semester : {semester}")
print("Marks obtained :")
for i in range(5):
    print(f"Subject-{i+1} : {marks[i]}")
print(f"Total Marks : {total_marks}")
print(f"Average : {average_marks}")
