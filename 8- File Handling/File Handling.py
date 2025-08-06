#CHAPTER 8
#FILE I/O (INPUT & OUTPUT)

#FILE I/O IN PYTHON

#Python can be used to perform opperations on a file.(read & write data)

#TYPES OF ALL FILES

# text file :  .txt, .docx, .log etc.
#Jin ma cracter form ma data store hota hy wo text files hoti hain.

# binart file : .mp4, .mov, .png, .jpeg etc.
#Jin ma character ki form ma data store ni hota balka kesi or formate ma data stoe hota wo 
#binary files hoti hain.

#OPEN , READ & CLOSE FILES

#READING A FILE

"""f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("demo.txt","r")
data = f.read(10)
print(data)
f.close()

f = open("demo.txt","r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

f = open("demo.txt","r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

f.close()"""

#WRITING TO A FILE

"""f = open("sample.txt", "w")
f.close()

f = open("demo.txt", "w")
f.write("i want to learn javascript tomorrow. 123")
f.close()

f = open("demo.txt", "a")
f.write("Then I,ll move to ReactJS")
f.close()

f = open("demo.txt", "a")

f.write("\nAfter that nodejs")

f.close()

f = open("demo.txt", "r+")
f.write("abc")
f.close()

f = open("demo.txt", "r+")
f.write("abc")
print(f.read())
f.close()

f = open("demo.txt", "w+")
print(f.read())
f.close()

f = open("demo.txt", "w+")
print(f.read())
f.write("abc")
f.close()

f = open("demo.txt", "a+")
print(f.read())
f.close()

f = open("demo.txt", "a+")
print(f.read())
f.write("abc")
f.close()"""

#WITH SYNTAX

"""with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
     f.write("i am learning python from apnacollege")"""

#DELETING A FILE
#USING THE OS MODULE

"""import os

os.remove("demo.txt")"""

#LETS PRACTICE

#Creat a new file "practice.txt" using python.Add the following data in it.
#HI everyone
#We are learning file I/O
#using java
#I like programming in java.

"""with open("practice.txt","w") as f:
    f.write("Hi everyone\nWe are learning file I/O\nusing java\nI like programming in java")"""

#WAF that replace all occerances of "Java" with "python" in above file.

"""with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","python")
print(new_data)"""

#Search if the word "learning" exist in the file or not.

"""word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")"""

"""def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")
check_for_word()"""

#WAF to find if which line f the file does the word "learning" occure first.
#Print -1 if word not found.

"""def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no )
                return
            line_no +=1

    
    return -1

check_for_line()"""

def check_for_line():
    word = "waina awan"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no )
                return
            line_no +=1

    
    return -1

print(check_for_line())

#From a file containing numbers separated by comma.Print the count of even
#numbers

"""count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    
    nums = data.split(",")
    for val in nums:
        if(int(val)%2 == 0):
            count += 1
            
print(count)"""