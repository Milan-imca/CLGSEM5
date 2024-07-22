'''
7. Create a tuple with 10 elements. Write a menu based program to perform following

operations:
1. Find sum of all elements of tuple.
2. find average of all elements of tuple.
3. Sort the tuple
4. find biggest element of the tuple
5. find smallest element of the tuple
'''




tuple = (1,2,3,4,5,10,9,8,7,6)

print("Menu : ")
print('''
    1. Find sum of all elements of tuple.
    2. find average of all elements of tuple.
    3. Sort the tuple
    4. find biggest element of the tuple
    5. find smallest element of the tuple
''')

ch = int(input("Enter choie : "))
if ch == 1:
    sumOfTuple = sum(tuple)
    print("The sum of tuple is : ",sumOfTuple)
elif ch == 2:
    sumOfTuple = sum(tuple)
    avgOfTuple = sumOfTuple/len(tuple)
    print("The average of tuple is : ",avgOfTuple)
elif ch == 3:
    sortedTuple = sorted(tuple)
    print("Sorted tuple : ",sortedTuple)
elif ch == 4:
    maxElement = max(tuple)
    print(maxElement)
elif ch == 5:
    minElement = min(tuple)
    print(minElement)
else:
    print("Invalid !!")