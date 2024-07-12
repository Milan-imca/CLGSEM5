# Take 3 numbers from user and find the greatest one without using logical operator:

n1 = 3
n2 = 2
n3 = 1

if n1 > n2:
    if n1 > n3:
        print(f"{n1} is greater than both {n2} and {n3}")
elif n2 > n1:
    if n2 > n3:
        print(f"{n2} is greater than {n1} and {n3}")
    else:
        print(f"{n3} is greater than {n1} and {n2}")
