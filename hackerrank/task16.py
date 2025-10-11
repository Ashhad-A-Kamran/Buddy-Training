""" 1
Write a Python function to find the maximum of three numbers.

"""
# def max_3(l):
#     return (max(l))

# print(max_3([9,99,999]))



""" 2
Write a Python function to sum all the numbers in a list.
 
"""
# def find_sum(l): return (sum(l))

# print(find_sum([9,99,999]))


""" 3
Write a Python function to multiply all the numbers in a list.

"""

# def mult_all(l):
#     j = 1
#     for i in l:
#         j *= i
#     return j

# print(mult_all([8, 2, 3, -1, 7]))




""" 4
Write a Python program to reverse a string.

"""
# s = "1234abcd"

# print(s[::-1])



""" 5
Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
"""

# def factorial(f):
#     j = 1
#     for i in range(1, f+1):
#         j = i*j
#     return j

# print(factorial(12))


""" 6
Write a Python function to check whether a number falls within a given range.
"""


# def check_in_range(n, r):
#     flag = False
#     if n in r:
#         return True
#     return False
    

# print((check_in_range(3, [1,2,3,4,5,6])))



""" 7
Write a Python function that accepts a string and counts the number of upper and lower case letters.
"""


# def count_upper_lower(s):
#     upper = 0
#     lower = 0

#     for i in s:
#         if i.isupper():
#             upper += 1
#         elif i.islower():
#             lower += 1
#         else:
#             "Not counted"

#     return upper, lower

# print(count_upper_lower("The quick brown dox JUMPED over the fence"))



""" 8
Write a Python function that takes a list and returns a new list with distinct elements from the first list.

"""

# def return_list(l): return set(l)

# print(list(return_list([1,1,2,2,3,3,4,4,5,5])))



""" 9 
Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

"""


# def is_prime(n):
#     priime = False
#     for i in range(2,n):
#         if n % i == 0:
#             prime = False
#             return False
#     return True

# print(is_prime(23))
# print(is_prime(27))


""" 10
Write a Python program to print the even numbers from a given list.
"""


# def print_even_odd(l):
#     l = [i for i in l if i % 2 == 0]
#     return l


# print(print_even_odd([2,2,3,4,5,6,7,8,9,10]))



""" 11
"""



""" 12
Write a Python function that checks whether a passed string is a palindrome or not.
"""


# def palindrome(l):
#     reversed = l[::-1]
#     if l == reversed:
#         return True
#     return False

# print(palindrome("racecar"))
# print(palindrome("Ashhad"))



""" 13
Write a Python function that prints out the first n rows of Pascal's triangle.
"""





""" 14
Write a Python function to check whether a string is a pangram or not.
"""
# import string


# alphabets = set(string.ascii_lowercase)


# def check_pangram(s):
#     once = set(s.lower())
#     if alphabets <= once:
#         return True
#     return False


# print(check_pangram("This is not a pangram"))
# print(check_pangram("The quick brown fox jumps over the lazy dog"))



""" 15
Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

"""

# our_input = input("Enter hyphen separated str: ").split("-")
# print("-".join(sorted(our_input)))



""" 16
Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included)."""


# def sqaure():
#     l = [i**2 for i in range(1,31)]
#     print(l)

    
# sqaure()



""" 17
Write a Python program to create a chain of function decorators (bold, italic, underline etc.).

A decorator is a function that takes another function as input, adds some behavior, and returns a modified function.
"""


# def bold(func):    


#     return func

# def italic(func):
#     return func

# def underline(func):
#     return func


# def make_bold():
#     text = input("enter your text: ")



# def outer(func):
#     def wrapper(*args):
#         print("before")
#         func()
#         print("after")
#     return wrapper

# @outer
# def inner(a,b):
#     return a+b

""" 18
Write a Python program to execute a string containing Python code.

"""

# take_input = input("Enter Python Code: ")

# exec(take_input)





""" 19
Write a Python program to access a function inside a function.


"""

def take_func(func):
    result = func()
    return result

def give_to_func():
    return 3+2

take_func(give_to_func)







""" 21
Write a Python program that invokes a function after a specified period of time.
"""

# import time

# name = input("Name: ")

# def print_greeting(name):
#     print(f"Hello dear {name}, good luck!")

# time.sleep(5)
    
# print_greeting(name)