'''
 8. WAP that accepts one integer value n1. Create a menu based on following options:
 a) if user enters 1, find factorial of the number
 b) if user enters 2, print fibonacci from 1 to n1
'''

print("Menu:")
print("Press 1. Factorial of a number ")
print("Press 2. Fibonacci of a number ")
choice = int(input("Enter the choice :"))

if choice == 1:
    print("Factorial of a number : ")
    num = int(input("Enter number : "))
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print(f"The factorial of {num} : {fact}")
    
elif choice == 2:
    print("Fibonacci : ")
    n1 = int(input("Enter a number (n1): "))
    a = 0
    b = 1

    print("Fibonacci series from 1 to", n1, ":")
    while b <= n1:
        if b >= 1:
            print(b, end=' ')
        temp = b
        b = a + b
        a = temp

else:
    print("Invalid input")  
    
    
    