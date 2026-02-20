# File I/O in Python
# I = Input , O = Output
# Python can be used to perform operations on a file.(read and write data)
# Types of all files
# Text Files : .txt , .docx , .log , etc
# Binary Files : .mp4 , .mov , .png , .jpeg , etc
# r = open for reading (dafault)
# w = open for writing, truncting the file first
# x = create a new file and open it for writing
# a = open for writing, appending to the end of the file if it exists
# b = binary mode
# t = text mode (default)
# + = open a disk file for updating (reading and writing)
# r+ = read + overwrites (pointer starting)
# w+ = read + overwrite (truncates)
# a+ = read + append (pointer in end)

f = open("Demo text.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("Demo text.txt", "r")
data = f.read(5)
print(data)
f.close()

f = open("Demo text.txt","r")

line_1 = f.readline()
print(line_1)

line_2 = f.readline()
print(line_2)

f.close()

f = open("Demo text.txt","w")
f.write("I want to lean HTML. 123")
f.close()

f = open("Demo text.txt","a")
f.write("Then i'll learn CSS")
f.close()

f = open("Demo text.txt","a")
f.write("\nAfter that JAVASCRIPT")
f.close()

f = open("Sample.txt", "w")
f.close()

f = open("Demo text.txt", "r+")
f.write("abc")
f.close()   # abc overwrites at starting three alphabets
            # if w+ is used then everytjing is deleted and abc is only found over there

f = open("Demo text.txt", "r+")
f.write("abc")
print(f.read())
f.close()

with open("Demo text.txt", "r") as f:
    data = f.read()
    print(data)

with open("Demo text.txt", "w") as f:
    f.write("new data")

# Deleting a file
import os
os.remove("Sample.txt")

# Practice
# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# We are learning File I/O
# Using Java
# I like programming in Java.
with open("Practice.txt", "w") as f:
    f.write("Hi everyone\nWe are learning File I/O\n")
    f.write("Using Java.\nI like programming i Java")

# WAF that replace all occurences of Java with Python in above file
with open("Practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("Practice.txt", "w") as f:
    f.write(new_data)

# Search if the word "learning" exists in file or not.
word = "learning"
with open("Practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")

# WE can also write it as
def check_for_word():
    word = "learning"
    with open("Practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")

check_for_word()

# WAF to find in which line of the file does the word "learning" occurs first. Print-1 if word not found.
def check_for_word():
    word = "learning"
    with open("Practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("Not Found")
            
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("Practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())

# From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("Practice2.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val)%2 == 0):
            count += 1

print(count)