'''
  4. Create a module operations.py with functions for arithmetic operations (add, subtract,
  multiply, divide). Import this module in another script and use its functions. Take numbers
  as user inputs and pass in module functions
'''

import operations as op


num1 = int(input('Enter a num1 : '))
num2 = int(input('Enter a num2 : '))

print(f"Add : {op.add(num1,num2)} ")
print(f"Subtract : {op.subtract(num1,num2)} ")
print(f"Multiply : {op.multiply(num1,num2)} ")
print(f"Divide : {op.divide(num1,num2)} ")