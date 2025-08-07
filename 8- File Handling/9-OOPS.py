
#CHAPTER 9

#OOPS  (OBJECT ORIENTED PROGRAMMING SYSTEM)

#PART 1

#OOPS IN PYTHON
#To map with real word scenarios,we started using object in code. This is call object oriented 
#programming .

#CLASS & OBJECT IN PYTHON
#Class is a blueprint for creating objects.

#Creating class

"""class Student:
    name = "waina awan"
    
#Creating object (instance)
 
s1 = Student()
print(s1)"""
    
"""class Student:
    name = "waina awan"
    
s1 = Student()
print(s1.name)"""
    
"""class Student:
    name = "waina awan"
    
s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

s3 = Student()
print(s3.name)"""

"""class Car:
    color = "black"
    brand = "Audi"
    model = "2025"
    
Car1 = Car()
print(Car1.color)
print(Car1.brand)
print(Car1.model)"""

#__init__ Function
#Constructor

"""class Student:
    
    def __init__(self, name):
        self.name = name
        print("adding a new student in my darabase")
        
s1 = Student("Waina Awan")
print(s1.name)

s2 = Student("Zunaira Awan")
print(s2.name)

s3 = Student("Mukaram Awan")
print(s3.name)

s4 = Student("Arqam Awan")
print(s4.name)""" 


"""class Student:
    
    #Parameterized constructors                                  #Default constructors                              
    def __init__(self, name, marks):                            #def __init__(self):
        self.name = name                                        #pass
        self.marks = marks
        print("adding a new student in my darabase")
        
s1 = Student("Waina Awan",97)
print(s1.name,s1.marks)

s2 = Student("Zunaira Awan",99)
print(s2.name,s2.marks)

s3 = Student("Mukaram Awan",88)
print(s3.name,s3.marks)

s4 = Student("Arqam Awan",95)
print(s4.name,s4.marks)"""

#Class & instances attributes

"""class Student:
    
    college_name = "Punjab College"                                                 
    def __init__(self, name, marks):                            
        self.name = name                                       
        self.marks = marks
        print("adding a new student in my darabase")
        
s1 = Student("Waina Awan",97)
print(s1.name,s1.marks)

s2 = Student("Zunaira Awan",99)
print(s2.name,s2.marks)

s3 = Student("Mukaram Awan",88)
print(s3.name,s3.marks)

s4 = Student("Arqam Awan",95)
print(s4.name,s4.marks)

print(Student.college_name)"""

"""class Student:
    
    college_name = "Punjab College" 
    name = "waneeza awan"            #class attribute                                           
    def __init__(self, name, marks):                            
        self.name = name             #object attribute > class attribute                          
        self.marks = marks
        print("adding a new student in my darabase")
        
s1 = Student("Waina Awan",97)
print(s1.name,s1.marks)"""

#METHODS
#Method are functions that belong to abjects.

"""class Student:
    college_name ="punjab college"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student",self.name)
        
    def get_marks(self):
        return self.marks
    
s1 = Student("waina awan", 95)
s1.welcome()
print(s1.get_marks())"""

#LETS PRACTICE

#Creat student class that takes name & marks of 3 subjects as arguments in constructor
#Then creat a method to print the average.

"""class Student:
    def __init__(self, name,  marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("hi", self.name, "your avg score is:", sum/3)
    
s1 = Student("waina awan",[98, 95, 100])
s1.get_avg()"""

"""class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("hi", self.name, "your avg score is:",sum/3 )
    
s1 = Student("waina awan",[98, 95, 100])
s1.get_avg()     
       
s1.name = "waneeza awan"
s1.get_avg()"""

#STATIC METHODS
#Methods that don,t use the self parameters (work at class level)

"""class Student:
    
    @staticmethod       #decorator
    def hello():
        print("hello")
        
    def __init__(self, name):
        self.name = name
        print("adding a new student in my darabase")
        
s1 = Student("Waina Awan")
print(s1.name)
s1.hello()"""

#IMPORTANT

#ABSTRACTION
#Hiding the implementation details of a class and only showing the essential features to the user.

#FOR EXAMPLE

"""class Car():
    
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.acc = True
        self.clutch = True
        print("car started")
        
car1 = Car()
car1.start()"""

#ENCAPSULATION
#Wrapping data and functions into a single unit (object).

#LETS PRACTICE

#Creat Account class with two attributes-balance and account no.
#Creat methods for debit,credit and printing the balance.

"""class Account:
    
    def __init__(self,bal,acc):
       self.balance = bal
       self.account_no =  acc
    #Debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balancs =", self.get_balance())
        
    #Credit method
    def Credit(self,amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total balancs =", self.get_balance())
        
    def get_balance(self):
        return self.balance
     
acc1 = Account(10000,1234)
acc1.debit(1000)
acc1.Credit(500)
acc1.Credit(400000)"""