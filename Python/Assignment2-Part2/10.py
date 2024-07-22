'''
    10. Create a tuple of 10 integers. Take startindex and endindex from user. Display tuple
    elements between those indexes only
'''

tuple = (1,2,3,4,5,6,7,8,9,10)

startIndex = int(input("Enter start index : "))
endIndex = int(input("Enter end index : "))

print(tuple[startIndex:endIndex])