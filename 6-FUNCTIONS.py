
#CHAPTER 6
#FUNCTIONS 

#FUNCTIONS IN PYTHON

"""def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum



calc_sum(4,9)

calc_sum(3,7)

calc_sum(5,8)

def calc_sum(a,b):
    return a + b

sum = calc_sum(4,5)
print(sum)

def print_apnacollege():
    print("apnacollege")

print_apnacollege()
print_apnacollege()
print_apnacollege()
print_apnacollege()
print_apnacollege()
print_apnacollege()
print_apnacollege()
print_apnacollege()"""

#average of 3 numbers

"""def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(45,79,94)"""

#FUNCTION TYPES

#BUIKT IN FUNCTIONS                  
#USER DEFINED FUNCTIONS

#BUILT IN FUNCTIONS
#jo functions already python k ander hoty wo built in functions hoty.

# foe exemple
#print()
#len()
#type()
#range()

#USER DEFINED FUNCTIONS
#fo functions hum khud(programer khud)likhta hy wo user defuned functions hoty.

#DEFAULT PARAMETERS

"""def calc_prod(a,b = 3):
    print(a * b) 
    return a * b
calc_prod(2)

def calc_prod(b,a = 3):
    print(a * b) 
    return a * b
calc_prod(4)

def calc_prod(a = 5,b = 3):
    print(a * b) 
    return a * b
calc_prod()

def calc_prod(a ,b):
    print(a * b) 
    return a * b
calc_prod(6,4)"""

#LETS PRACTICE

#WAF to print the length of a list(list is the parameter)

"""cities = ["lahore","islamabad","karachi","gujranwala","multan","pashawar"]
players = ["babar azam","virat kholi","saim ayub","haris rouf","shadab khan"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(players)"""

#WAF to print the elements of a list in a single line(list is the parameter)

"""players = ["babar azam", "virat kholi", "saim ayub", "haris rouf", "shadab khan"]

def print_list(list):
    for i in list:
        print(i,end = " ")
print_list(players)"""

#WAF to find the factorial of n(n is the peremeter)

"""def calc_fact(n):
    fact = 1
    for i in range(1,n + 1):
        fact *= i
    print(fact) 

calc_fact(6) """

#WAF to convert USD to INR.

"""def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"usd =", inr_val,"inr")

converter(100)"""