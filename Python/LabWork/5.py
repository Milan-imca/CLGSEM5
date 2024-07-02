# Write a Program that accepts a number n1 , take 2 more values n2 and n3 , Check if n1 is divisible by n2 or n3 or both or none

n1 = 11
n2 = 2
n3 = 3


# NOTE this will not work!!!
# if n1 % n2 == 0:
#     print(f"{n1} is divisble by {n2}")
# elif n1 % n3 == 0:
#     print(f"{n1} is divisble by {n2}")
# elif n1 % n2 == 0 and n1 % n3 == 0:
#     print(f"{n1} is divisible by both {n2} and {n3}")
# else:
#     print(f"{n1} is neither divisble by {n2} nor {n3}")


if n1 % n2 == 0:
    if n1 % n3 == 0:
        print(f"{n1} is divisible by both {n2} and {n3}")
    else:
        print(f"{n1} is divisible by {n2}")
elif n1 % n3 == 0:
    if n1 % n2 == 0:
        print(f"{n1} is divisible by both {n2} and {n3}")
    else:
        print(f"{n1} is not divisible by {n2}")
else:
    print(f"{n1} is not divisible by {n2} and {n3}")