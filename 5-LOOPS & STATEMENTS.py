
#CHAPTER 5
#LOOPS

#WHILE LOOP

"""count = 1
while count <= 10:
    print("pakistan")
    count += 1

i = 1
while i <= 10:
    print("pakistan")
    i += 1

i = 1
while i <= 10:
    print("apnacolllege")
    i += 1

i = 1
while i <= 1000:
    print("apnacolllege",i)
    i += 1

i = 1
while i <= 10:
    print(i)
    i += 1
print("loop ended")

i = 10
while i >= 1:
    print(i)
    i -= 1
print("loop ended")

i = 1
while i <= 20:
    print("waina awan", i)
    i += 1
print("loop ended")"""

#KETS PRACTICE

#Print numbers from 1 to 100

"""i = 1
while i <= 100:
    print(i)
    i += 1
    print("loop ended")"""

#Print numbers from 100 to 1

"""i = 100
while i >= 1:
    print(i)
    i -= 1
    print("loop ended")"""

#Print the multiplication table of a number n

"""i = 1
while i <= 10:
    print(5*i)
    i += 1
    print("loop ended")

n = int(input("enter number:"))
i = 1
while i <= 10:
    print(n*i)
    i += 1
    print("loop ended")"""

#Print the elements of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]

"""nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

players = ["babar azam","saim ayub","haris rouf","naseem shah"]

idx = 0
while idx < len(players):
    print(players[idx])
    idx += 1"""

#Search for a number x in this tuple using loop.
#(1,4,9,16,25,36,49,64,81,100)

"""nums = (1,4,9,16,25,36,49,64,81,100)

x = 81

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
    else:
        print("finding")
    i += 1"""

#BREAK & CONTINUE

#Break

"""i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("loop ended")

i = 1
while i <= 20:
    print(i)
    if(i == 10):
        break
    i += 1
print("loop ended")

nums = (1,4,9,16,25,36,49,64,81,100)

x = 81

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
        break
    else:
        print("finding")
    i += 1
print("loop ended")"""

#CONTINUE

"""i = 0
while i <= 10:
    if(i == 5):
        i += 1
        continue
    print(i)
    i += 1

i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1"""

#FOR LOOPS
                                        #List, String or Tuple k lye or loop use hota
"""nums = [1,2,3,4,5,6,7]

for val in nums:
    print(val)


players = ["babar azam","virat kholi","saim ayub","naseem shah"]

for val in players:
    print(val)

tup = (5,4,3,2,1)

for nums in tup:
    print(nums)

str = "apnacollege"

for char in str:
    print(char)

str = "apnacollege"

for char in str:
    print(char)
else:
    print("end")

str = "apnacollege"

for char in str:
    if(char == "o"):
        print("o found")
        break
    print(char)
else:
    print("end")"""

#LETS PRACTICE
#USING FOR

#Print the elements of the following list using a loop.
#[1,4,9,16,25,36,49,64,81,100]

"""list = [1,4,9,16,25,36,49,64,81,100]

for val in list:
    print(val)"""

#Search for a number x in this tuple using loop.

"""nums = (1,4,9,16,25,36,49,64,81,100)
x = 25

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx",idx)
    idx += 1 

tup = (1,4,9,16,25,36,49,64,81,100)
x = 100

idx = 0
for val in tup:
    if(val == x):
        print("number found at idx",idx)
        break
    idx += 1 """

#range()

"""seq = range(10)

for i in seq:
    print(i)

for i in range(20):         #range(stop)
    print(i)

for i in range(2,20):           #range(start,stop)
    print(i)

for i in range(2,20,2):           #range(start,stop,step)
    print(i)

for i in range(2,101,2):
    print(i)

for i in range(1,100,2):
    print(i)"""

#LETS PRACTICE
#USING FOR & RANGE

#Print numbers from 1 to 100.

"""for i in range(1,101):
    print(i)"""

#Print numbers from 1 to 100.

"""for i in range(100,0,-1):
    print(i)"""

#Print the multiplication table of a number n.

"""n = int(input("enter number:"))

for i in range(1,11):
    print(i*n)"""

#PASS STATEMENT

"""for i in range(5):
    pass

print("some useful work")"""

#LETS PRACTICE

#WAP to find the sum of first n numbers (using while)

"""n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i +=1
print("total sum =",sum)"""

#using for loop

"""n = 5
sum = 0

for i in range(1,n+1):
    sum += i
print("total sum =",sum)"""

#WAP to find the factorial of  first n number(using for loop)

#using while loop

"""n = 4
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =",fact)"""

#using for loop

"""n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
    
print("factorial =",fact)"""