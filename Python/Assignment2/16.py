'''
16. WAP that accepts a string s1. Pring the longest word in the string
'''

s1 = input("Ente a string : ")

words = s1.split()

longest_word = ""
max_length=0

for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)

print(f"The longest word in {s1} is {longest_word}")