'''
8. Write a function outer_function(text) that defines a nested function inner_function() which
prints the reversed version of text. The outer_function should call inner_function and return
its result.
'''

def outer_function(text):
  def inner_function():
    return text[::-1]
  return inner_function()

print(outer_function('Hello'))