# 3. WAP to print length of the accepted string. If length is greater than 15, split string into individual words

string = input("Enter string : ")
length_of_string = len(string)

if length_of_string > 15:
    result = string.split()
    print(result)
else:
    print(f"The length of string is not greater than 15")
