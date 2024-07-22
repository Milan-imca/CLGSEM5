# 11. Create a dictionary that stores list of courses and no of students enroled as key and values
# respectively. Take name of course from user and display no of students enroled in that
# course.


data = {
    "IMCA":180,
    "BCA":200,
    "BCA Hons":150
}

key = input("Enter the course name : ")

print(f"Number of students in {key} : {data[key]}")