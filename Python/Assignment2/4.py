# 4. WAP that accepts one integer value n1 from user. Calculate the sum of all integers from 1 to n1.

n1 = int(input("Enter n1 : "))

sum=0

for i in range(1,n1+1):
    sum = i + sum

print(f"Sum from 1 to {n1} is {sum}") 