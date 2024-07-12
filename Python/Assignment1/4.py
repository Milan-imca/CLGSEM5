#  4. WAP that accepts 3 string from user i.e. string1, string2, string3. Replace string2 with string3 in string2

string1 = input("Enter string 1 : ")
string2 = input("Enter the string2 (to be replaced) : ")
string3 = input("Ener the string3 (new string) : ")


result = string1.replace(string2,string3)

print(result)