# class Student:
#   def getInfo(self):
#     self.name = input("Enter you subh naam : ")
  
#   def dipslayInfo(self):
#     print(f"tumhara subh naam : {self.name} haiiiiii")
    

# s1 = Student()
# s1.getInfo()
# s1.dipslayInfo()


# => normal constructor
# class Student:
#   def __init__(self,roll_no,naam):
#     self.roll_no = roll_no
#     self.naam = naam
  
#   def displayInfo(self):
#     print(f"Roll no : {self.roll_no}")    
#     print(f"Name: {self.naam}")    

# s1=Student(54,"Milan")
# s1.displayInfo()


# => input from user using constructor
# class Game:
  
#   def __init__(self):
#     self.name = input("Enter game name : ")
#     self.score = input("Enter you score : ")
    
#   def displayGameInfo(self):
#     print(f"Game name : {self.name}")
#     print(f"Game score : {self.score}")


# g1 = Game()
# g1.displayGameInfo()

# => using constructor and destructor:

# class Person:
#   def __init__(self,name="",age=""): # default arguement
#     self.name = name
#     self.age = age
#     print("Constructor called!")
  
#   def printName(self):
#     print(f"Name : {self.name}")
#     print(f"Age : {self.age}")
  
#   # destructor
#   def __del__(self):
#     print("Destructor called!")
    


# p1 = Person("Yashvi",20)
# p1.printName()

# name = input("Enter name : ")
# age = int(input("Enter age : "))

# p2 = Person(name,age)
# p2.printName()




# => Inheritance: (single inheritance)
# class Person:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
  
#   def printPersonDetails(self):
#     print(f"Name : {self.name}\nAge : {self.age}")
    
    
# class Student(Person):
#   def __init__(self,name,age,rollNo,course,sem):
#     super().__init__(name,age)
#     self.rollNo = rollNo
#     self.course = course
#     self.sem = sem
  
#   def printStudentDetails(self):
#     print(f"Roll no : {self.rollNo}\nCourse : {self.course}\nSem : {self.sem}")

# p1 = Person("Milan",21)
# p1.printPersonDetails()


# print("---------------")
# p2 = Student("Milan",21,54,"imca",5)
# p2.printPersonDetails()
# p2.printStudentDetails()




#  Multiple Inheritance:
# class A:
#   def __init__(self,a):
#     self.a = a 
  
#   def printA(self):
#     print(f"Value of a : {self.a}")

# class B:
#   def __init__(self,b):
#     self.b = b 
  
#   def printB(self):
#     print(f"Value of a : {self.b}")
    
# class C(A,B):
#   def __init__(self,a,b,c):
#     A.__init__(self,a)
#     B.__init__(self,b)
#     self.c = c 
    
#   def printC(self):
#     print(f"Value of C : {self.c}")
    
    
# obj = C(1,2,3)
# obj.printA()
# obj.printB()
# obj.printC()



# Multi-level Inheritance:
class University:
  def __init__(self,uname):
    self.uname = uname
    
  def printUniversityName(self):
    print(f"University name : {self.uname}")

class Department(University):
  def __init__(self,dname,uname):
    super().__init__(uname)
    self.dname = dname
    
  def printDepartmenetName(self):
    print(f"Department name : {self.dname}")
    
class Course(Department):
  def __init__(self,cname,dname,uname):
    super().__init__(dname,uname)
    self.cname = cname
    
  def printCourseName(self):
    print(f"Course name : {self.cname}")
    
    
obj = Course("imca","fcait","gls")
obj.printCourseName()
obj.printDepartmenetName()
obj.printUniversityName()


