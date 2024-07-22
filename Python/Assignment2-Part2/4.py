'''
    4. Create a list of 25 numbers. Take input from user.
        1. Display the numbers greater than 10.
        2. Display the numbers that are even.
        3. Display the numbers that are odd.
        4. Display the numbers that are positive.
        5. Display the numbers that are negetive.
'''

list = [1,-2,3,4,5,6,-7,-8,-9,10,11,12,-13,14,15,16,-17,18,-19,20,-21,22,23,24,-25]
n = len(list)

print("Menu : ")
print('''
    1. Display the numbers greater than 10.
    2. Display the numbers that are even.
    3. Display the numbers that are odd.
    4. Display the numbers that are positive.
    5. Display the numbers that are negetive.   
''')

choice = int(input("Enter choice : "))


if choice == 1:

    for i in range(0,n):
        if list[i]>10:
            print(list[i],end=" ")
elif choice == 2:
    print("Even numbers : ")
    for i in range(0,n):
        if list[i] % 2 == 0:
            print(list[i])
elif choice == 3:
    print("Odd numbers : ")
    for i in range(0,n):
        if list[i] % 2 != 0:
            print(list[i])
elif choice == 4:
    print("Positive numbers : ")
    for i in range(0,n):
        if list[i]>0:
            print(list[i],end=" ")
elif choice == 5:
    print("Negative numbers : ")
    for i in range(0,n):
        if list[i]<0:
            print(list[i],end=" ")
else:
    print("Invalid choice !")