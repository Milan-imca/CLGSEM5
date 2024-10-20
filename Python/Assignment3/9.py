''' 9. Write a function apply_operation(a, b, operation) where operation is a function (like add,
subtract, etc.). The apply_operation function should return the result of applying operation
to a and b.'''

def apply_operation(a, b, operation):
    return operation(a, b)

print(apply_operation(5, 3, lambda x, y: x + y)) 
print(apply_operation(5, 3, lambda x, y: x * y)) 

