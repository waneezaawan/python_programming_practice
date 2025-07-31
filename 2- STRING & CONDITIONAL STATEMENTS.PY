#CHAPTER 2
#STRINGS & CONDITIONAL STATEMENTS

"""str1 = "my name is waina.my age is 20"
print(str1)
str2 = "my name is waina.\n my age is 20"
print(str2)
str3 = "my name is waina.\t my age is 20"
print(str3)"""

#BASICS OPERATIONS
#CONCATENATION

"""str1 = "waina"
str2 = "awan"
final_str = str1+str2
print(final_str)"""

#LENGTH OF STR

"""str1 = "waina"
len1 = len(str1)
print(len1)

print(final_str)


str1 = "waina"
len1 = len(str1)
print(len1)

str2 = "awan"
len2 = len(str2)
print(len2)

final_str = str1+str2
print(final_str)
print(len(final_str))"""

#INDEXING

"""str = "waina awan"
ch = str[6]
print(ch)"""

#SLICING

"""str = "waina awan"
print(str[6:9])

str = "apna college"
print(str[0:])

str = "waina awan"
print(str[:9])"""

#SLICING
#NEGATIVE INDEX

"""str = "waina awan"
print(str[-6:-9])

str = "apna college"
print(str[-0:])

str = "waina awan"
print(str[:-9])"""

#STRING FUNCTIONS

"""str = "I am studing python from apna college"
print(str.endswith("ege"))

str = "i am studing python from apna college"
print(str.capitalize())
"I am studi
str = "I am studing python from apna college"
print(str.replace("python","java"))

str = "I am studing python from apna college"
print(str.find("o"))

str = "I am from studing python from apna college"
print(str.count("from"))"""

#LETS PRACTICE

#WAP to input users first number & print its length.

"""name = input("enter you name:")
print("length of your name is:",len(name))"""

#WAP to find the occurrence of $ in a string.

"""str = "hi $ i am waina $ symbol of $"
print(str.count("$"))"""

#CONDITIONAL STATEMENTS

"""light = "green"

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look") 
elif(light == "green"):
    print("go")  
else:
    print("light is broken")"""

#NESTING

"""age = 50

if(age >= 30):
    if(age >= 40):
        print("can vote")
    else:
        print("cannot vote")    

age = 35

if(age >= 30):
    if(age >= 40):
        print("can vote")
    else:
        print("cannot vote")"""

#LETS PRACTICE

#WAP to check if a number entered by the user is odd and even.

"""num = 14 
rem = num % 2

if(rem ==0):
    print("even")
else:
    print("odd")    


num = int(input("enter number:")) 
rem = num % 2

if(rem ==0):
    print("even")
else:
    print("odd")"""

#WAP to find the greatest of 3 numbers entered by the user.

"""a = 2
b = 7
c = 3

if(a >= b a
and a >= c):
    print("a is greatest")
elif("b >= c"):
    print("b is greatest")  
else:
    print("c is greatest")     


a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a >= b and a >= c):
    print("first number is greatest:", a)
elif(b >= c):
    print("second number is greatest:", b)  
else:
    print("third number is greatest:", c)"""

#WAP to check if a number is a  multiple of 7 or not.

"""x = int(input("enter number:"))

if(x % 7 == 0):
    print("multiple of 7")
else:
    ("not a multiple:") """
