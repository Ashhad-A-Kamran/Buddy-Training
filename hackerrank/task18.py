# l = [lambda args=x: x*10 for x in range(1,5)]


# for i in l:
#     print(i)



# def l(x=10):
#    return x*10

# for i in range(1,5):
#     print(l())


""" 1 sir
Build a calculator() that returns nested functions for add,subtract, multiply, and divide. 

Each returned function should take 2 parameters, and return the result

validate Division by zero
"""









 
""" 2 sir
Write a function prime_upto(n) that returns all prime numbers upto n

Include input validation for type and value

"""

def prime_upto(n):
    if isinstance(n, int) and n<100:

        primes = []
        for i in range(2, n+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                primes.append(i)
    else:
        print("Please provide an integer and less than 100")
        return []         
    return primes

print(prime_upto(21))


# def prime_upto(n):
#     # Input validation
#     if not isinstance(n, int) or n < 2:
#         print("Please enter a positive integer greater than 1.")
#         return []

#     primes = []
#     for i in range(2, n + 1):
#         for j in range(2, int(i ** 0.5) + 1):  # check up to sqrt(i)
#             if i % j == 0:
#                 break
#         else:
#             primes.append(i)  # only executed if no divisor found

#     return primes


# # Example usage:
# print(prime_upto(21))




""" 3 sir
Write a function that accepts a list of numbers and returns a dictionary of total, average, max, min, all even numbers(in a list)


"""

# def enter_nums(l):
#     dict1 = {
#         "total" : sum(l),
#         "average": sum(l)/len(l),
#         "max": max(l),
#         "min": min(l),
#         "even numbers": [i for i in l if i%2==0]
#     }

#     return dict1

# print(enter_nums([44,33,22,55,66,77,98]))






""" 4. hackerrank
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

# def swap_case(s):
#     new_string=""
#     for i in s:
#         if i.isupper():
#             new_string += i.lower()
#         elif i.islower():
#             new_string += i.upper()
#         else:
#             new_string += i
#     return new_string

# s = input("Input text: ")
# result = swap_case(s)
# print(result)




""" 5 hackerrank
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
"""


# def print_full_name(first, last):
#     print(f"Hello {first} {last}! You just delved into python.")

# first_name = input()
# last_name = input()
# print_full_name(first_name, last_name)





""" 6. hackerrank
Let's use decorators to build a name directory! You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.
"""

# import operator

# def person_lister(f):
#     def inner(people):
#         print("People: ", people)
#         list_sorted = sorted(people, key= lambda x: int(x[2]))
#         print("list_sorted: ", list_sorted)
        
#         return [f(person) for person in list_sorted]
#     return inner

# @person_lister # name_format = person_lister(name_format)
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# people = [input().split() for i in range(int(input()))]

# print(*name_format(people), sep='\n')



""" 7. Chatgpt
Higher-Order Function Problem

Problem:
Create a higher-order function data_pipeline that takes a list of functions (steps) and returns a new function.
When called with a number, the returned function should run that number through all the steps in order, passing the output of one as the input of the next.

Example:

def double(x): return x * 2
def add_three(x): return x + 3
def square(x): return x ** 2

pipeline = data_pipeline([double, add_three, square])
print(pipeline(2))


Expected Output:

49   # ((2*2)+3)**2


Hint:
Use function composition — your higher-order function returns another function.

"""


# def data_pipeline(func_list):
#     def apply_func(x):
#         for func in func_list:
#             print("Before applying function: ", x)
#             print(func)
#             x = func(x)
#             print("\nAfter applying function: ", x)
#         return x
#     return apply_func



# def double(x): return x * 2
# def add_three(x): return x + 3
# def square(x): return x ** 2


# pipeline = data_pipeline([double, add_three, square])
# print(pipeline(2))





""" 8.
Callback Function Problem

Problem:
Write a function fetch_data(callback) that simulates fetching data from a server (just sleep for 2 seconds).
When data is “fetched,” it should call the callback function with the result.

Example:

def print_result(data):
    print(f"Received: {data}")

fetch_data(print_result)


Expected Output (after 2 seconds):

Received: {'status': 'success', 'data': [1,2,3,4]}


Hint:
Use time.sleep() to simulate delay and then call the callback function.
"""

# import time

# def fetch_data(callback):
#     print("Fetching data...")
        
#     print("Data fetched successfully.")
#     print(callback())



# def callback():
#     return {'status': 'success', 'data': [1,2,3]}


# fetch_data(callback)




""" 9. chatgpt
Closure Function Problem

Problem:
Write a closure make_counter(start) that returns two functions:

increment() → increases the count and returns it

decrement() → decreases the count and returns it

Each counter should keep its own internal state (independent of others).

Example:

counter1 = make_counter(10)
counter2 = make_counter(0)

print(counter1['increment']())
print(counter1['decrement']())  # 10
print(counter2['increment']())  # 1


Hint:
Use nonlocal to modify a variable inside nested functions.
"""


# def make_counter(start):
#     state = start
#     def increment():
#         nonlocal state
#         state += 1
#         return state
    
#     def decrement():
#         nonlocal state
#         state -= 1
#         return state 
    
#     return [increment, decrement]

# counter1 = make_counter(10)
# counter2 = make_counter(0)

# # plus 1
# print(counter1[0]())
# print(counter1[0]())
# print(counter1[0]())
# print(counter1[0]())  

# # minus 1
# print(counter1[1]())
# print(counter1[1]())





""" 10. Chatgpt
Decorator Problem

Problem:
Write a decorator time_logger that:

Records how long the wrapped function took to run

Prints: Function <name> took X.XXX seconds


Hint:
Use time.time() before and after the function call.
"""

# import time
# def time_logger(func):
#     def wrapper(*args, **kwargs):
#         start= time.time()
#         func(*args, **kwargs)
#         end= time.time()
#         print(f"{func.__name__} execution took {round(end - start, 5)} seconds")
#         return func
#     return wrapper

# @time_logger
# def multiply():
#     (5000000999001233322*5)**2


# @time_logger
# def looper():
#     for i in range(0,10001):
#         i+=1

# multiply()
# looper()
    


""" 11. Chatgpt
Closure + Lambda — Dynamic Multiplier Factory
Problem:

Write a closure make_multiplier(factor) that returns a lambda function which multiplies any given number by factor.

Example:
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
"""


# def make_multiplier(factor):
#     f = lambda x: x*factor
#     return f

# print(
# make_multiplier(4)(6))




""" 12. Chatgpt
Decorator + Callback — Timing Function Execution
Problem:

Write a decorator timer(callback) that measures how long a function takes to run and sends that duration to a callback function.

The callback should simply print the duration.

Example:
import time

def show_time(t):
    print(f"Function took {t:.3f} seconds")

@timer(show_time)
def slow_function():
    time.sleep(1)
    print("Done!")

slow_function()
"""















""" 13. Chatgpt
Generator + Higher-Order Function — Infinite Power Sequence
Problem:

Write a function power_sequence(base) that returns a generator producing powers of base (e.g., 2, 4, 8, 16, ...).
Then, create a higher-order function get_first_n(generator_func, n) that takes the generator function and returns the first n values.

Example:
gen = power_sequence(2)
print(get_first_n(gen, 5))  # [2, 4, 8, 16, 32]
"""








""" 14. Chatgpt
Decorator + Lambda — Conditional Execution Decorator
Problem:

Create a decorator run_if(condition) that only runs the function if condition() (a lambda or function returning bool) is True.

Example:
should_run = lambda: True
should_not_run = lambda: False

@run_if(should_run)
def hello():
    print("Hello World!")

@run_if(should_not_run)
def bye():
    print("Goodbye!")

hello()  # prints "Hello World!"
bye()    # prints nothing
"""












""" 15. Chatpgt
Callback + Generator — Stream Processor
Problem:

Write a generator stream_numbers() that yields numbers from user input (stops when “stop” is entered).
Write a function process_stream(generator, callback) that runs through the stream, and for each number, calls the callback function to handle it.

Example:
def print_double(x):
    print(x * 2)

def stream_numbers():
    while True:
        n = input("Enter number or 'stop': ")
        if n == "stop":
            break
        yield int(n)

process_stream(stream_numbers(), print_double)


Input/Output:

Enter number or 'stop': 5
10
Enter number or 'stop': 3
6
Enter number or 'stop': stop
"""