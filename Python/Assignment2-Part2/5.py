'''
    5. Create a list of 5 fruits. Perform following menu based operations.
        1. Take name of one fruit and index from user. Insert new fruit and the given index.
        2. Take name of one fruit and index from user. Remove new fruit and the given index.
        3. Remove last element from the list
'''

list = ['apple','banana','greenapple','papaya']

print("Menu : ")
print('''
    1. Take name of one fruit and index from user. Insert new fruit and the given index.
    2. Take name of  fruit and index from user. Remove new fruit .
    3. Remove last element from the list
''')

choice = int(input("Enter choice : "))

if choice == 1:
    i = int(input("Enter the index :"))
    value = input("Enter the fruit name  : ")
    list.insert(i,value)
    print("List : ",list)
elif choice == 2:
    value = input("Enter the fruit name to be removed")
    list.remove(value)
    print(list)
elif choice == 3:
    list.pop()
    print("List after removing the last element : ",list)
else:
    print("Invalid choice !!!")