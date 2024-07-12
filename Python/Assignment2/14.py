'''
14. WAP that accepts a string s1. Create a menu based on following options:
 1. if user enters 1, check number of uppsercase in string
 2. if user enters 2, check number of lowercase in string
 3. if user enters 3, check number of spaces in string
'''

s1 = input("Enter s1 : ")
print("Menu")
print('''
    1. Check if the string in uppercase
    2. Check if the string is lowercase
    3. Check if the number of spaces in string
    ''')
choice = int(input("Enter choice : "))

if choice == 1:
    print("check if is in uppercase : ")
    if s1.isupper():
        print(f"{s1} is in Uppercase")
    else:
        print(f"{s1} is not in uppercase")
        
elif choice == 2:
    print("Check if string is in lowercase")
    if s1.islower():
        print(f"{s1} is in Lowercase")
    else:
        print(f"{s1} is not in Lowercase")

elif choice == 3:
    print("Counting the space in the string : ")
    count_of_space = s1.count(' ')
    print(f"Count of spaces in {s1} is : {count_of_space}")
    
else:
    print("Invalid choice ...")
    