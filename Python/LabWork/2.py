# - Accept 2 String from user : Check if 2nd String exists in 1st string `if yes` then `how many times`.If the string is occuring for more than 1 time then print the index of each occurence. (1/7/2024)


str1 = input("Enter string1 : ")
str2 = input("Enter string2 : ")

if str2 in str1:
    count = str1.count(str2)
    print(f"{str2} is occuring {count} times in {str1}")
    
    if count > 1:
        print("Indexes of occuring : ")
        
        start = 0
        while True:
            start = str1.find(str2,start)
            if start == -1:
                break
            print(start)
            start += 1
else:
    print(f"{str2} is not occuring in {str1}")
            
