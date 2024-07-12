'''
11. WAP that accepts one integer value n1. Create a menu based on following options:
 a) if user enters 1, caluculate square of n1
 b) if user enters 2, caluculate cube of n1
'''

print("Menu")
print("1. caluculate square")
print("2. caluculate cube")

choice = int(input("Enter the choice : "))

if choice == 1:
    print("Calculating Square : ")
    n1 = int(input("Enter number : "))
    square = n1*n1
    print(f"Sqaure of {n1} : {square}")

elif choice == 2:
    print("Calculating Cube : ")
    n1 = int(input("Enter number : "))
    cube = n1*n1*n1
    print(f"Cube of {n1} : {cube}")

else:
    print("Invalid choice")