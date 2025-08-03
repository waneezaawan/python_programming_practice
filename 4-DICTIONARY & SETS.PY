
#CHAPTER 4
#DICTIONARY & SETS

#DICTIONARY IN PYTHON

"""info = {
    "name" : "waina awan",
    "age" : 20,                                   #DICTIONARY   MUTABLE  =  THAT CAN CHANGE
    "subjacts" : ["python", "java", "c"],
    "marks" : 98.9,
    "tuple" : (" dictionart", "sets"),
    "is_adult" : "true",
}

print(info)

info = {
    "name" : "waina awan",
    "age" : 20,                                  
    "subjects" : ["python", "java", "c"],
    "marks" : 98.9,
    "tuple" : (" dictionart", "sets"),
    "is_adult" : "true",
}

print(info["name"])
print(info["subjects"])
print(info["tuple"])

info = {
    "name" : "waina awan",
    "age" : 20,                                  
    "subjects" : ["python", "java", "c"],
    "marks" : 98.9,
    "tuple" : (" dictionart", "sets"),
    "is_adult" : "true",
}
info["name"] = "waina"
info["sur name"] = "awan"
print(info)"""

#NESTED DICTIONARIES

"""student ={
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["bio"])"""

#DICTIONARY METHODS

"""student ={
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
print(list(student.keys()))


student ={
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
print(len(student))
print(list(student.keys()))

student ={
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
print(len(list(student.keys())))

student = {
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
print(student.values())

student = {
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
print(list(student.values()))

student = {
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
print(student.items())

student = {
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
print(list(student.items()))

student = {
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
print(student["name"])
print(student.get("name"))

student = {
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
print(student.update({"city" : "lahore"}))
print(student)

student = {
    "name" : "waina",
    "subjects" : {
        "phy" : 80,
        "chem" : 70,
        "bio" : 95,
    }
}
new_dict = {"city" : "lahore"}
print(student.update(new_dict))
print(student)"""

#SETS IN PYTHON                            #SET    MUTABLE  =  THAT CAN CHANGE
                                        #SET ELEMENTS  IMMUTABLE  =  THAT CANNOT CHANGE
"""collection = {1,2,3,4,5}
print(collection)
print(type(collection))
print(len(collection))

collection = set()
print(type(collection))"""

#SET METHODS

"""collection = set()
collection.add(1)
collection.add(2)
collection.add(1)
print((collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add(1)
print(len(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.remove(1)
print((collection))

collection = set()
collection.add(1)
collection.add(2)
collection.remove(1)
print(len(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.clear()
print((collection))

collection = set()
collection.add(1)
collection.add(2)
collection.clear()
print(len(collection))

collection = {"apna college", "python","hello", "java"}
print(collection.pop())
print(collection.pop())

set1 = {1,2,3}
set2 = {2,3,4,5}

print(set1.union(set2))

set1 = {1,2,3}
set2 = {2,3,4,5}

print(set1.intersection(set2))"""

#LETS PRACTICE

#Store following words meaning in a python dictionary.
#Table : "a piece of furniture" , "lists of facts & figures"
#Cat : "a small amimal"

"""dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture" , "lists of facts # figure"],
}
print(dictionary)"""

#You are given a list of subjects for students.Assume one classroom is required for i subject.
#How many classroom are needed by all students.
#"python", "java", "c++", "python","javascript","java", "python", "java", "c++", "c"

"""students = {
    "python", "java", "c++", "python","javascript","java", "python", "java", "c++", "c"
}
print(len(students))"""

#WAP to enter marks of 3 subjects from the user and store then in a dictionary.Start with an
#empty dictionary & add one by one.Use subject name as key & marks as value.

"""marks = {}

x = int(input("enter phy:"))
marks.update({"phy": x})

x = int(input("enter chem:"))
marks.update({"chem": x})

x = int(input("enter math:"))
marks.update({"math": x})

print(marks)"""

#Figure out a way to store 9 & 9.0 as separate values in the set.
#(You can take help of built_in data type)

"""values = {
    ("float" , 9.0),
    ("int" , 9)
}
print(values)"""