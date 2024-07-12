# 6  WAP to check if string is alphanumeric or numeric

string = input("Enter string : ")

if string.isalnum():
    if string.isdigit():
        print(f"{string} is a numeric")
    else:
        print(f"{string} is a alphanumeric")
elif string.isdigit():
    print(f"{string} is a numeric")
    