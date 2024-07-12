'''
7. WAP that accepts one integer value n1. Create a menu based on following options:
a) if user enters 1, find if number is prime or not
b) if user enters 2, print all prime numbers between 1 to n1
c) if user enters 3, print all odd numbers between 1 to n1
d) if user enters 4, print all even numbers between 1 to n1
'''

print("Menu\n")
print("1. find if number is prime or not")
print("2. print all prime numbers between 1 to n1")
print("3. print all odd numbers between 1 to n1")
print("4. print all even numbers between 1 to n1")
choice = int(input("Enter choice : "))


if choice == 1:
    num = int(input("Enter a number : "))
    is_Prime = False

    if num == 1:
        print("1 is not a prime number")
    elif num > 1:
        for i in range(2,num):
            if (num % i == 0):
                is_Prime == True
                break
    if is_Prime:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not prime number")

elif choice == 2:
    n1 = int(input("Enter n1 : "))
    for num in range(1,n1+1):
        if num == 1:
            continue
        if num <= 3:
            print(num)
            continue
        if num%2 == 0:
            continue
        
        isPrime = True
        for i in range(3,num):
            if num % i == 0:
                isPrime = False
            
        if isPrime:
            print(num,end=" ")

elif choice == 3:
    n1 = int(input("Enter n1 : "))
    print(f"Odd numbers between 1 to {n1}")
    for i in range(1,n1+1,2):
        print(i,end=" ")

elif choice == 4:
    n1 = int(input("Enter n1 : "))
    print(f"Even numbers between 1 to {n1}")
    for i in range(2,n1+1,2):
        print(i,end=" ")

else:
    print("Invalid choice...")


