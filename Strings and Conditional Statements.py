str1 = "This is a string"
str2 = 'Krish'
print(str1, str2)
print(str1 + str2)
print(str1 + " " + str2)
print(len(str1 + " " + str2))  # Spacing is also included

str3 = """This is also a string
spans multiple line"""
print(str3)

str4 = "My name is Krishna.\nI'm 18"
print(str4)
print(len(str4))
print(str4[3])
print(str4[1:4])
print(str4[7:])
print(str4[:9])
print(str4[1:16:4])
print(str4[-16:])
print(str4[:-16])
print(str4[-3:-1])
print(str4[::-1])
print(str4[::2])

str5 = "krishna ajay ingle"
print(str5.endswith('le'))
print(str5.startswith('Kr'))
print(str5.capitalize())
print(str5)
print(str5.replace('a', 'o'))
print(str5.find('a'))
print(str5.find('krishna'))
print(str5.count('a'))

# WAP to inpt user's first name and print its length
Name = input("Enter Your Name: ")
print(len(Name))

# WAP to find the occurence of 'a' in a string
str6 = "Hi, how r u"
print(str6.count('a'))

# CONDITIONAL STATEMENTS
age = int(input("Enter your AGE: "))
if (age >= 21):
    print("Can Drink Only Mild Beer")
elif (age >= 25):
    print("Is Legal To Drink Everything")
else:
    print("You are a MINOR \nGROW UP KIDDO")

