# 2. WAP to accept a string check if string is upper case or lower

string = input("Enter a string : ")

if string.isupper():
    print(f"{string} is in uppercase")
elif string.islower():
    print(f"{string} is in lowercase")
else:
    print(f'{string} is in mixture of uppercase and lowercase')