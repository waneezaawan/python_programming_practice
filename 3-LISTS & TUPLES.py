
#CHAPTER 3
#LISTS AND TUPLES

"""marks = [23.7, 34.7, 67.3, 87.5, 99.0]
print(marks)
print(type(marks))
print(marks[1])
print(marks[4])
print(len(marks))
                                               # strings   immutable = that cannot change
student = ["waina", 20, 100, "grw"]             #lists     mutables  = that can change  
print(student)
print(len(student))

student = ["waina", 20, 100, "grw"]             
print(student)
student[0] = "waina awan"
print(student)"""

#LISTS SLICING

"""marks = [50, 60, 70, 80, 90, 100]
print(marks[0:5])

marks = [50, 60, 70, 80, 90, 100]
print(marks[0:])

marks = [50, 60, 70, 80, 90, 100]
print(marks[:4])

marks = [50, 60, 70, 80, 90, 100]
print(marks[-4:-1])"""

#LISTS METHODS

"""list = [1, 2, 3, 4, 5]
list.append(6)
print(list)

list = [5, 3, 2, 4, 1]
list.sort()
print(list)

list = [5, 3, 2, 4, 1]
list.sort(reverse=True)
print(list)

list = [5, 3, 2, 4, 1]
list.reverse()
print(list)

list = [5, 3, 2, 4, 1]
list.insert(0, 6)
print(list)

list = [5, 3, 2, 4, 1]
list.remove(5)
print(list)

list = [5, 3, 2, 4, 1]
list.pop(3)
print(list)"""

#TUPLES IN PYTHON

"""tup = (1, 2, 3)
print(tup)                                                        #tuples  = immutables
print(len(tup))
print(type(tup))
print(tup[1])
print(tup[2])

tup =(1,)
print(tup)
print(type(tup))

tup =("waina awan",)
print(tup)
print(type(tup))

tup =(1.88,)
print(tup)
print(type(tup))

tup = ("waina awan", "zunaira awan","arqam awan","mukaram awan",)
print(tup)
print(type(tup))"""

#SLICING

"""tup = (1,2,3,4,5)
print(tup[2:4])

tup = (1,2,3,4,5)
print(tup[:4])

tup = (1,2,3,4,5)
print(tup[0:])

tup = (1,2,3,4,5)
print(tup[-5:])

tup = (1,2,3,4,5)
print(tup[:-1])"""

#TUPLES METHODS

"""tup = (1,2,3,4,5,1,3,5,5)
print(tup.index(3))

tup = (1,2,3,4,5,1,3,5,5)
print(tup.count(5))"""

#WAP to ask the user to enter name of their 3 favorite movies and store them in a list.

"""movies = []
mov1 = input("enter first movie:")
mov2 = input("enter second movie:")
mov3 = input("enter third movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)"""

#WAP to check if a list contain a palindrome of elements. (Hint: use copy() method)

"""list1 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):                    #PALINDROME
    print("palindrome")
else:
    print("not palindrome")    


list1 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):                    #NOT PALINDROME
    print("palindrome")
else:
    print("not palindrome")    


list1 = ["m","a","a","m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):                        #PALINDROME
    print("palindrome")
else:
    print("not palindrome")"""

#WAP to count the numbers of students with the A grade in the following tuples.
#("C", "D", "A", "A","B", "B", "A")

"""grade = ("C", "D", "A", "A","B", "B", "A")
print(grade.count("B"))"""

#WAP to store the above values in a list & sort them from "A" to "D".

"""grade = ["C", "D", "A", "A","B", "B", "A"]
grade.sort()
print(grade)"""