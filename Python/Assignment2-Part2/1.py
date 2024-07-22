# 1. Create a list of your five favorite fruits. And perform following menu based operations :
    # 1. Add a new fruit to the list.
    # 2. Remove a fruit from the list.
    # 3. Print the first and last fruit in the list.
    # 4. Sort the list in alphabetical order.

fruits=['apple', 'kiwi', 'papaya', 'orange', 'greenapple']

# for i in range(1,6):
#     x = input(f"Enter fruit {i} : ")
#     fruits.append(x)
print(f"List of Fruits : {fruits}")

print("Menu: ")
print("1.Add a new fruit to the list.")
print("2.Remove a fruit from the list.")
print("3.Print the first and last fruit in the list.")
print("4. Sort the list in alphabetical order.")

choice = int(input("Enter choice : "))

if choice == 1:
    print("Add a new fruit : ")
    newFruit = input("Enter fruit name : ")
    fruits.append(newFruit)
    print(f"List of Fruits : {fruits}")
elif choice == 2:
    lastFruit = fruits.pop()
    print(f"List of Fruits : {fruits}")
    print(f"Removed the last item from list that was : {lastFruit}")
elif choice == 3:
    firstFruit = fruits[0]
    lastFruit = fruits[len(fruits) - 1]
    print(f"List of Fruits : {fruits}")
    print(f"First fruit : {firstFruit}\nLast fruit : {lastFruit}")
elif choice == 4:
    fruits.sort()
    print("Sorted fruits in alphabetical order : ",fruits)
else:
    print("Invalid input select from 1 to 4 only!")