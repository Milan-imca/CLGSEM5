# 10. WAP that accepts one integer value n1. Create a menu based on following options:
#  a) if user enters 1, print sum of all odd numbers from 1 to n1
#  b) if user enters 2, print sum of all even numbers from 1 to n1

print("Menu")
print("1. For sum of Odd numbers")
print("2. For sum of Even numbers")

choice = int(input("Enter the choice : "))

if choice == 1:
    n1 = int(input('Enter n1 : '))
    print(f"Printing the odd numbers from 1 to {n1} :")
    for i in range(1,n1+1,2):
        print(i,end=" ")
elif choice == 2:
    n1 = int(input('Enter n1 : '))
    print(f"Printing Even number from 1 to {n1} : ")
    for i in range(2,n1,2):
        print(i,end=" ")
else:
    print('Invalid choice!')