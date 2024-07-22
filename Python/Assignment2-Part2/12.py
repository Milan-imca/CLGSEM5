'''
12. Create a dictionary that stores list of courses and no of students enroled as key and values respectively and perform following menu based tasks:
1. display only keys
2. display only values
3. display both keys and values
'''


data = {
    "IMCA":180,
    "BCA":200,
    "BCA Hons":150
}

print("Menu : ")
print('''
    1. display only keys
    2. display only values
    3. display both keys and values
''')

ch = int(input("Enter choice : "))

if ch==1:
    print("keys : ")
    for  i in data:
        print(i)
elif ch==2:
    print("values")
    for i in data:
        print(data[i])
elif ch==3:
    print("Keys and values :")
    for key,value in data.items():
        print(f"{key} : {value}")
else:
    print("Invalid!!")