# try :
#   print("code start")
#   print(1/0)

# except:
#   print("an error occurs")

# finally:
#   print("reached to finally blocked!!")


# => user defined exception:

class AgeError(Exception):
  def __init__(self,message):
    super().__init__(message)

# AgeError -> __init__() 
# __init__() [ageError constructor] -> Exception ka constructor
# try:
#   age = int(input("Enter age : "))
#   if age < 0:
#     raise AgeError("Invalid age!!")
#   elif age < 18:
#     print("Age can't be less than 18")
#   else:
#     print("Age is valid!!")

# except AgeError:
#   print("AgeError : Invalid age entered")

# except AgeError as e:
#   print(f"Error : {e}")


# => directly using Exception class
try:
  age = int(input("Enter age : "))
  if age <= 0:
    raise Exception("Age can't be 0 or less than 0")
  elif age < 18:
    print("Age can't be less than 18")
  else:
    print("Age is valid!!!")
# except Exception:
#   print("Error : Invalid age error")4
except Exception as e:
  print(f"Error : {e}")