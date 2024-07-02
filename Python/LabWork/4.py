# - Menu based Program for following cases:`upper()`,`lower()`,`title()`,`sentence()`


print("Options : ")
print("1. Convert to Upper case")
print("2. Convert to Lower case")
print("3. Convert to Title case")
print("4. Convert to Sentence case")

choice = int(input("Enter the Choice : "))
str = input("Enter the string : ")

match choice:
    case 1:
        print(f"Upper Case : {str.upper()}")
    case 2:
        print(f"Lower Case : {str.lower()}")
    case 3:
        print(f"Title Case : {str.title()}")
    case 4:
        print(f"Sentence Case : {str.capitalize()}")
    case _:
        print(f"Invalid choie! Try Again")