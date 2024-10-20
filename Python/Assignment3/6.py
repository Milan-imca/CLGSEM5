'''
  6. Write a Python function sum_and_product(numbers) that takes a list of numbers as input
  and returns a tuple containing two values: The sum of all the numbers in the list. The
  product of all the numbers in the list.
'''

def sum_and_products(numbers):
  totalSum = sum(numbers)
  product = 1
  for num in numbers:
    product = product * num
  return (totalSum,product)

list = [1,2,3,4]
print(f"The sum and product of the list {list} :- {sum_and_products(list)}")



