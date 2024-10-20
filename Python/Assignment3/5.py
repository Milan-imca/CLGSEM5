''' 5. Write a lambda function that takes two arguments and returns their product. Use this lambda
  function with the map() function to multiply elements of two lists together.'''
  
  
  # Lambda function
product = lambda x, y: x * y

# Lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Use map with lambda
result = list(map(product, list1, list2))
print(result)
