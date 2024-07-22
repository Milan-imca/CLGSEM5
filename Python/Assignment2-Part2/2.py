'''
    2. Create a list of numbers from 1 to 10.
        1. Print the first three numbers.
        2. Print the last three numbers.
        3. Print every other number in the list.
        4. Reverse the list.
'''

list = [1,2,3,4,5,6,7,8,9,10]

print("Menu")
print('''
        1. Print the first three numbers.
        2. Print the last three numbers.
        3. Print every other number in the list.
        4. Reverse the list.
''')

choice = int(input("Enter choice : "))

if choice == 1:
    print("First three number are : ",list[0:3])
elif choice == 2:
    list.reverse()
    print("Last three number are : ",list[0:3])
elif choice == 3:
    n = len(list)
    for i in range(0,n,2):
        print(list[i],end=" ")
elif choice == 4:
    list.reverse()
    print(list)
else:
    print("Invalid selection")