'''
    6. Create a tuple with your five favorite fruits.
        1. Access and print the first and last items in the tuple.
        2. Attempt to add a new food to the tuple and observe what happens.
        3. Convert the tuple to a list, add a new fruit, and convert it back to a tuple.
'''



fruits = ('apple','banana','pineapple','orange','watermelon')
print(f"The tuple of fruits : {fruits}")

firstItem = fruits[0]
lastItem = fruits[4]

print(f"First fruit is : {firstItem}")
print(f"Last fruit  is  : {lastItem}")


# fruits[5] = "guava" 
# The above line will give this error :    
# TypeError: 'tuple' object does not support item assignment

listOfFruits = list(fruits)
print(f"The list of fruits : {listOfFruits}")
listOfFruits.append('kiwi')
print(f"Added new fruit : {listOfFruits}")
        

# convert the listOfFruits back to a tuple
tupleOfFruits = tuple(listOfFruits)
print(f'The tuple of fruits : {tupleOfFruits}')


