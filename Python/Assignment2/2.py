#  2. WAP that accepts time value in integer (24 hour format). If time entered is less than 12, pring “Good
#  Morning” else if time entered is between 12 to 4(16), print “Good Afternoon” else if time is between 4(16) to 8(20)
#  print “Good Night”.


user_time = int(input("Enter the time in 24 hr format : "))

if user_time < 12:
    print("Good morning")
elif user_time > 12 and user_time < 16:
    print("Good Afternoon")
elif user_time > 16 and user_time < 20:
    print("Good Night")