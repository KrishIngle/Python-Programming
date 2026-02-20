marks = [94.4, 87.2, 39.6, 65.7, 45.1]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])

student = ['Krishna', 18, 'Pune']
print(student)
student[2] = 'MIT-WPU'   # Will give error if index will be 3 or above
print(student)   # Lists are mutable and string are immutable
# LIST SLICING IS SAME AS STRING SLICING

# LIST METHODS
list = [2, 1, 3]
print(list)
list.append(4)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)
list.reverse()
print(list)
list.insert(3, 1)   # Syntax = name of list.insert(index, element)
print(list)
list.remove(1)   # removes first occurence of element
print(list)
list.pop(1)   # removes element at idx

tup = (2, 1, 3, 4)
print(tup)
print(type(tup))
print(tup[0])
# tup[0] = 5  will give error
tup1 = (1,)   # comma is copulsory if creating single element tuple, otherwise it'll consider it as integer
print(tup1)
# Slicing is same as lists

# Tuple Methods
tup2 = (1, 2, 3, 4, 3)
print(tup2)
print(tup2.index(2))
print(tup2.count(3))

# PRACTICE
# WAP to ask user to enter names of their 3 favorite movies & store them in a list
movies = []
movie1 = input('Enter your favorite movie: ')
movie2 = input('Enter your favorite movie: ')
movie3 = input('Enter your favorite movie: ')
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

# WAP to check if a list contains a palindrome of elements
list1 = [1, 2, 1]
list2 = [1, 2, 3]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 ==  list1):
    print('palindrome')
else:
    print('Not Palindrome')

copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2 ==  list2):
    print('palindrome')
else:
    print('Not Palindrome')

# WAP to count the number of students with grade A in following tuple, also store the values ina list and sort them from A to D
tup3 = ('C', 'D', 'A', 'A', 'B', 'C', 'A', 'A', 'D', 'B', 'B')
print(tup3)
print(tup3.count('A'))
list3 = [*tup3]
print(list3)
list3.sort()
print(list3)