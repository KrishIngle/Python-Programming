# Functions
# Block of statements that perform a specific task
def calc_SUM(a, b):
    sum = a+b
    print(sum)
    return(sum)

calc_SUM(2, 3)

# This can also be written as
def Calc_sum(c, d):
    return c+d

Sum = Calc_sum(1, 2)
print(Sum)

def print_hello():
    print("Hello")

output = print_hello()
print(output)   # None will be the output as it doesnt return anything
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

def average(e, f, g):
    avg = (e+f+g)/3
    print(avg)
    return avg

average(10, 15, 18)

def cal_prod(h, i):
    print(h*i)
    return h*i

cal_prod(4, 5)

# Practice
# WAF to print the length of a list.(list is the parameter)
cities = ["PUNE","MUMBAI","BANGALORE","CHENNAI","HYDERABAD","DELHI"]
heroes = ["Spiderman","Batman", "Ironman", "Thor", "Superman"]


def print_length(list):
    print(len(list))

print_length(cities)
print_length(heroes)

# WAF to print the elements of a list in a single line.(list is the parameter)
def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(heroes)
print()

# WAF to find the factorial of n. (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(12)

# WAF to convert USD to INR
def price_convert(usd):
    inr = usd*90
    print(usd, "USD =", inr, "INR")

price_convert(3)

# WAF such that if number is even it will return the string EVEN and if od number then will return string ODD
def number_string(n):
    if n%2 == 0:
        print("Even")
    else:
        print("Odd")

number_string(5)

# RECURSION
# When a function calls itself repeatedly
def show(n):
    if n == 0:   # base case
        return
    print(n)
    show(n-1)
   
show(6)

# In general we will be using loops to solve programs
# Factorial of numbers
def fact(n):
    if n < 0:
        return "Factorial is not defined"
    elif(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

# PRACTICE
# Write a recursive function to calculate sum of first n natural number
def nums(n):
    if n<0:
        return "Number is not natural"
    elif n == 0:
        return 0
    else:
        return n+nums(n-1)
    
print(nums(10))

# Write a recursive function to print all elements in a list.
def lists(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    lists(list, idx+1)

heroes = ["Spiderman","Batman", "Ironman", "Thor", "Superman"]
lists(heroes)

# Define a function to generat Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    sequence.append(a)
    sequence.append(b)
    for i in range(2, n):
        a, b = b, a+b
        sequence.append(b)
    return sequence

print(fibonacci(10))

# Define a function for prime numbers
def is_prime(n):
    if(n<=1):
        return False
    else:
        for i in range(2, n):
            if(n%i == 0):
                return False
            return True
        
print(is_prime(67))

# Palindrome check
def palindrome_check(s):
    n =len(s)
    i = 0
    j = n-1
    while(i<=j):
        if(s[i] != s[j]):
            return False
        else:
            i = i+1
            j =j-1
        return True
    
print(palindrome_check("banana"))
print(palindrome_check("racecar"))