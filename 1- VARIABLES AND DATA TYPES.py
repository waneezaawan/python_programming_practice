#CHAPTER 1
#VARIABLES AND DATA TYPES

"""print("hello world")
print("waina is my name")
print("my age is 20")
print("waina is my name","my age is 20")

print(467)
print(89890)
print(12+8)
print(4_4)"""

#VARIABLES
"""
name = "waina
age = 20
price = 23.7

print(name)
print(age)
print(price)

print("my name is:",name)
print("my age is:",age)

age2 = age

print(age2)

name = "waina"
age = 20
price = 23.7
old = True
a = None

print(type(name))
print(type(age))
print(type(price))
print(type(old))
print(type(a))"""

#COMMENTS IN PYTHON

#INPUTS IN PYTHON

"""name = input("name:")
age = int(input("age:"))
price = float(input("price:"))

print("My name is", name,"and I am", age,"years old")"""

#PRACTICE TIME

#CONDITIONAL STATEMENTS

#TRAFIC LIGHT CODE

"""light = input("light:")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look") 
elif(light == "green"):
    print("go")  
else:
    print("light is broken")"""

#GRADS OF STUDIENTS

"""marks = int(input("marks:"))

if(marks >= 90):
    print("A")
elif(marks >= 80 and marks <= 90):
    print("B")  
elif(marks >= 70 and marks <= 88):
    print("C")      
else:
    print("D")"""

#SINGLE LINE IF/TERMARY OPERATOR

"""food = input("food:")

eat = "yes" if food == "cake" else "no"
print(eat)

food = input ("food:")
print("sweet") if food == "cake" or food == "ice creem" else ("not sweet")"""

#TYPE CONVERSION

"""a = 3
b = 2.7
sum = a + b
print(sum)"""

#TYPE CASTING

"""a = int("2")
b = 4.25

print(type(a))
print(a + b)"""

#INPUT IN PYTHON

"""name = input("enter your namr:")
print("you entered:",name)

age = input("enter your age:")
print("you entered:",age)

val = input("enter some value:")
print(type(val),val)

name = input("enter name:")
age = input("enter age:")
marks = input("enter marks:")

print("welcome:",name)
print("age",age)
print("marks",marks)"""

#LETS PRACTICE

#Write a program to input 2 numbers & print their sum.

"""first = int(input("enter first:"))
second = int(input("enter second:"))

print("sum =", first + second)"""

#WAP to input side of a square & print its area.

"""side = int(input("enter square side:"))

print("area =",side*side)"""

#WAP to input 2 floating point numbers & print their average.

"""a = float(input("enter first:"))
b = float(input("enter second:"))

print("avg =",(a + b)/2)"""

#WAP to input 2 int numbers.a & b
#print true if a is greater then or equal to b.if not print false.

"""a = int(input("enter first number:"))
b = int(input("enter second number:"))

print(a >= b)"""