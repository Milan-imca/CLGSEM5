'''
12. WAP that accepts two string values s1 and s2. Create a menu based on following options:
 1. if user enters 1, find length of string
 2. if user enters 2, Concatenate both the strings
 3. if user enters 3, reverse the string
 4. if user enters 4, pring each character of string in newline
'''


s1 = input("Enter s1 : ")
s2 = input("Enter s2 : ")

print("Menu")
print('''
    1. Find length of String
    2. Concate both string
    3. Reverse String
    4. Print each Character of string in a new line
    ''')
choice = int(input("Enter choice : "))

if choice == 1:
    print("PRINTING THE LENGTH OF STRING")
    print(f"Length of s1 {len(s1)}")
    print(f"Length of s2 {len(s2)}")

elif choice == 2:
    print("Concating 2 Strings")
    result = s1+s2
    print(f"{s1} + {s2} = {result}")

elif choice == 3:
    print("Reverse of Strings")
    print(f"Reverse of {s1} : {s1[::-1]}")
    print(f"Reverse of {s2} : {s2[::-1]}")

elif choice == 4:
    print("Printing each character of String in a new line : ")
    print(f"Printing the characters of {s1}")
    for i in s1:
        print(i)
    print(f"Printing the characters of {s2}")
    for i in s2:
        print(i)

else:
    print("Invalid choice...Try again")