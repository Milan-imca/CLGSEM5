'''
  7. Write a function find_max(*args) that accepts any number of positional arguments and
  returns the maximum value. Use argument unpacking to test your function with a list of
  numbers.
'''

def find_max(*args):
  return max(args)

list = [1,2,34,99]
print(f"Max number from {list} : {find_max(*list)}")


