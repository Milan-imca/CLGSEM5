#  1. WAP that accepts two integer values n1, n2 from user. Check if n1 is divisible by n2

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))

if n1 % n2 == 0:
    print(f"{n1} is divisible by {n2}")
else:
    print(f"{n1} is not divisible by {n2}")
