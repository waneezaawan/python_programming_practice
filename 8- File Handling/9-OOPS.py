
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


#CHAPTER 9
#OOPS  (OBJECT ORIENTED PROGRAMMING SYSTEM)

#PART 2

#DEL KEYWORD
#Used to delete object properties or object itself.

"""class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
               
s1 = Student("waina awan", 100)

del s1
print(s1)"""


"""class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
               
s1 = Student("waina awan", 100)
print(s1.name)
print(s1.marks)
del s1
print(s1)"""

#PRIVATE (LIKE) ATTRIBUTES & METHODS.

"""class Account:
    
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        
acc1 = Account("12345", "abc")
print(acc1.acc_no)
print(acc1.__acc_pass)"""      

"""class Account:
    
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("12345", "abc")
print(acc1.acc_no)
print(acc1.reset_pass())"""

"""class Person:
    __name = "waina awan"
    
p1 = Person()
print(p1.__name)"""

"""class Person:
    __name = "waina awan"
    
    def __hello(self):
        print("hello person")
    
    def welcome(self):
        self.__hello()
        
p1 = Person()
print(p1.welcome())"""

#INHERITANCE
#When one class (child/derived) drives the properties & methods of another class (parent/base).

"""class Car:
    
    color = "black"
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stoped.")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
car1 = ToyotaCar("fartuner")
print(car1.name)
print(car1.start())
print(car1.stop())     
print(car1.color)"""

#INHERTANCE TYPES

#Single Inhertance
#Multi_level Inhertance
#Multiple Inhertance

#SINGLE INHERTANCE

"""class Car:
    
    color = "black"
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stoped.")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
car1 = ToyotaCar("fartuner")
print(car1.name)
print(car1.start())
print(car1.stop())     
print(car1.color)"""

#MULTI_LEVEL INHERTANCE

"""class Car:
    
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stoped.")
        
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
        
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
        
car1 = Fortuner("diesel")
car1.start"""

#MULTIPLE INHERTANCE

"""class A:
    varA = "welcome to class A"
    
class B:
    varB = "welcome to class B"

class C(A, B):
     varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB) 
print(c1.varA)"""

#SUPER METHOD  
#Super()method is used to access methods of the parent class.

"""class Car:
    
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("car started")
        
    def stop():
        print("car stoped")
        
class ToyotaCar(Car):
    
    def __init__(self, name, type):
        super().__init__(type)
        super().start()
        self.name = name
         
car1 = ToyotaCar("fortuner","electric")
print(car1.name)        
print(car1.type)"""

#CLASS METHODS

#A class methos is bound to the class & receive the class as an implicit first argument. 

"""class person:
    
    name = "waina awan"
    
    @classmethod        #DECORATOR
    def changeName(cls,name):
        cls.name = name
        
p1 = person()
p1.changeName("waneeza awan")
print(p1.name)
print(person.name)"""

#PROPERTY
#We use @property decorater on any method in the class to use the method as a property.

"""class Student:
    
    def __init__(self,phy, chem, bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio
        
    @property  
    def percentage(self):
        return str((self.phy + self.chem + self.bio) /3) + "%"
    
stu1 = Student(95, 89, 100)
print(stu1.percentage)

stu1.phy = 90
print(stu1.percentage)"""

#POLYMORPHISM : OPERATOR OVERLOADING
#When the same operator is allowed to have different meaning according to the context.

#OPERATORS & DUNDER FUNCTION
# a + b  __add__

"""class Complex:
    
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def ShowNumbers(self):
        print(self.real, "i +", self.img, "j")
        
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
        
num1 = Complex(2,4)
num1.ShowNumbers()

num2 = Complex(4,6)
num2.ShowNumbers()

num3 = num1 + num2
num3.ShowNumbers()"""

# a - b  __sub__

"""class Complex:
    
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def ShowNumbers(self):
        print(self.real, "i +", self.img, "j")
        
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
        
num1 = Complex(2,4)
num1.ShowNumbers()

num2 = Complex(4,6)
num2.ShowNumbers()

num3 = num1 - num2
num3.ShowNumbers()"""

#LETS PRACTICE

#Define a circle class to creat a circle with radius r USING the constructor.
#Sefine an Area() method of the class which calculate s the area of the circle.
#Define a perimeter() method of the class which allow you to calculate the perimeter of the circle.

"""class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 22/7 * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
        
c1 = Circle(21)
print(c1.area())        
print(c1.perimeter())"""

#Define an employee class with attributes role, department & salary.This class also has a showdetails()
#methods.
#Creat an engineer class that inherit properties from employee & has additional attributes:name & age.

"""class Employee:
    
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showDetails(self):
        print("role =", self.role)
        print("department =", self.department)
        print("salary =", self.salary)
        
class Engineer(Employee):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer", "IT", "80,000")
    
       
e1 = Employee("accountant", "finance", "70,000")
e1.showDetails()
eng1 = Engineer("waina awan", 20)
eng1.showDetails()"""

#Creat a class called order which stores items & its price.
#Use dunder function__gt__() to convey that:
#order1 > order2 if price of order1 > price of order2

"""class Order:
    
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1 = Order("chips", 20)
odr2 = Order("tea", 15)    

print(odr1 > odr2)"""

