#  7. WAP to perform following functions using menu:
#  a) convert string to uppercase
#  b) convert string to lowercase
#  c) convert string to sentencecase
#  d) convert string to titlecase
#  e) convert string to switchcase ❌

string = input("Enter a string : ")

print("Menu")
print('''
    1. Convert to UPPERCASE
    2. Convert to LOWERCASE
    3. Convert to SENTENCECASE
    4. Convert to TITLECASE
    ''')

choice = int(input("Enter a choice : "))

if choice == 1:
    print("Converting to Uppercase : ")
    result = string.upper()
    print(f"Uppercase : {result}")
elif choice == 2:
    print("Converting to LowerCase:")
    result = string.lower()
    print(f"Lowercase : {result}")
elif choice == 3:
    print("Converting to SentenceCase:")
    result = string.capitalize()
    print(f"Capitalize : {result}")
elif choice == 4:
    print("Converting to TitleCase:")
    result = string.title()
    print(f"Titlecase : {result}")
else:
    print("Invalid choice Select between 1-4")