
#CHAPTER 7

#RECURSION

#FUNCTION WITHOUT RECURSION

"""def show(n):
    print(n)

show(5)"""

#FUNCTION WITH RECURSION

"""def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(10)

def show(n):
    if(n == 10):
        return
    print(n)
    show(n+1)

show(0)

def show(n):
    if(n == 11):
        return
    print(n)
    show(n+1)

show(1)

def show(n):
    if(n ==0):
         return
    print(n)
    show(n-1)
    
show(101)

def show(n):
    if(n ==0):
         return
    print(n)
    show(n-1)
    print("end")
    
show(101)

def fact(n):
    if(n == 0 or n == 1):
        return 1
    return fact(n-1) * n

print(fact(6))

def fact(n):
    if(n == 0 or n == 1):
        return 1
    return fact(n-1) * n

print(fact(4))"""

#LETS PRACTICE

#Write a recursion function to calculate the sum of first n natural numbers.

"""def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = (calc_sum(10))
print(sum)"""

#Write a recursion function to print all elements in a list.
#Hint : use list & index as parameters.

"""def print_list(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx + 1)

players = ["babar azam", "virat kholi", "haris rouf", "naseem shah", "saim ayub"]

print_list(players)"""