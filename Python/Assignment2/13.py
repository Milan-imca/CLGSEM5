'''
13. WAP taking into consideration following:
 1. Accept string s1. 
2. Accept two integer values start and stop.
 3. Print substring from start to stop from string s1
'''

s1 = input("Enter s1 : ")
start = int(input("Enter start : "))
stop = int(input("Enter end : "))

result = s1[start:stop]
print(f"Printing {s1} from {start}th index to {stop}th index : {result}")