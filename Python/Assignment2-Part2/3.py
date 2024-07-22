'''
    3. Create two lists: one of even numbers and one of odd numbers.
        1. Print both the lists.
        2. Concatenate the two lists.
        3. Use the extend method to add the elements of the second list to the first list.
        4. Sort the combined list
'''

list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]

print("List 1 : ",list1)
print("List 2 : ",list2)

concatedList = list1 + list2
print("Concated list : ",concatedList)

list1.extend(list2)
print("List1 : ",list1)

concatedList.sort()
print(concatedList)