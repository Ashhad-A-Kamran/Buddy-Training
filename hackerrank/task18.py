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


# def calculator():
#     def add(a,b):
#         return a+b
    
#     def subtract(a,b):
#         return a-b

#     def multiply(a,b):
#         return a*b

#     def divide(a,b):
#         return a/b
    
#     return [add, subtract, multiply, divide]


# func = calculator()

# add = func[0]
# subtract = func[1]
# multiply = func[2]
# divide = func[3]

# print(add(2,3))
# print(subtract(55,40))
# print(divide(50,10.5))
# print(multiply(4.3,2))

 
""" 2 sir
Write a function prime_upto(n) that returns all prime numbers upto n

Include input validation for type and value

"""

# def prime_upto(n):
#     if isinstance(n, int) and n<100:

#         primes = []
#         for i in range(2, n+1):
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 primes.append(i)
#     else:
#         print("Please provide an integer and less than 100")
#         return []         
#     return primes

# print(prime_upto(21))


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



""" 4 Sir
Generator from Dictionary keys/ values write two generators
    - dict_keys() yields keys
    - dict_values() yields values
"""

# def dict_keys(data):
#     for key,values in data.items():
#         yield key



# def dict_values(data):
#     for key,values in data.items():
#         yield values


# dict_for_k_v = {"name": "Ashhad Ashhad",
#                 "last_name": "Kamran",
#                 "age": 2,
#                 "sex": "M",
#                 }

# keys_gen = dict_keys(dict_for_k_v)
# values_gen = dict_values(dict_for_k_v)

# print(next(keys_gen))
# print(next(values_gen))

# print(next(keys_gen))
# print(next(keys_gen))
# print(next(keys_gen))




""" 5. hackerrank
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




""" 6 hackerrank
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
"""


# def print_full_name(first, last):
#     print(f"Hello {first} {last}! You just delved into python.")

# first_name = input()
# last_name = input()
# print_full_name(first_name, last_name)





""" 7. hackerrank
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



""" 8. Chatgpt
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





""" 9.
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




""" 10. chatgpt
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





""" 11. Chatgpt
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
    


""" 12. Chatgpt
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




""" 13. Chatgpt
Decorator + Callback — Timing Function Execution
Problem:

Write a decorator timer(callback) that measures how long a function takes to run and sends that duration to a callback function.

The callback should simply print the duration.

"""


# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         time_taken = end_time - start_time
#         print(time_taken)
#         callback(time_taken)
#         return time_taken
#     return wrapper

# def callback(get_time):
#     print(f"Time taken: {get_time}")

# @timer #slow_function = timer(slow_function)
# def slow_function():
#     time.sleep(2)
#     print("Execution Done")

# slow_function()


""" 14. Chatgpt
Generator + Higher-Order Function — Infinite Power Sequence
Problem:

Write a function power_sequence(base) that returns a generator producing powers of base (e.g., 2, 4, 8, 16, ...).
Then, create a higher-order function get_first_n(generator_func, n) that takes the generator function and returns the first n values.

Example:
gen = power_sequence(2)
print(get_first_n(gen, 5))  # [2, 4, 8, 16, 32]
"""

# def power_sequence(base):
#     power = base
#     while True:
#         yield power
#         power *= base


# def get_first_n(generator_func, n):
#     l = []
#     for _ in range(n):
#         l.append(next(generator_func))
#     return l

# gen = power_sequence(3)


# print(get_first_n(gen, 5))




""" 15. Chatgpt
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



# def run_if(condition):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if condition:
#                 result = func(*args,**kwargs)
#                 return result
#             else:
#                 print("Function not run, condition is False")
#         return wrapper
#     return decorator

# should_run = lambda: True
# should_not_run = lambda: False


# @run_if(should_run)
# def hello():
#     print("Hello function run")

# @run_if(should_not_run)
# def bye():
#     print("Byw function run!")

# hello()
# bye()





""" 16. Chatpgt
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



# def stream_numbers():
#     while True:
#         n = input("Enter number or 'stop': ")
#         if n == "stop":
#             break
#         yield int(n)


# def process_stream(generator, callback):
#     for number in generator:
#         callback(number)
    

# def print_double(x):
#     print(x * 2)

# print(process_stream(stream_numbers(), print_double))




""" 17 Chatgpt

Functions, Arguments, Higher-Order Functions

Write a function that demonstrates all types of arguments: positional, keyword, default, and *args, **kwargs.
"""

# def func(p,*args, keyword="some keyword", **kwargs):
#     print(p,args, keyword, kwargs, sep="\n")


# func(33, [22,11,44], some="keyword")




""" 18
Create a function that returns another function which adds a fixed number to its input (closure)."""


# def take_func(func):
#     return func()+4

# def base_func():
#     return 5

# print(take_func(base_func))




""" 19 Chatgpt

Store multiple arithmetic functions (add, sub, mul) inside a dictionary and call them based on user input."""



# def call_func(dict1):
    
#     while True:
#         inp = input("Choose: add, sub, mul, div or exit").strip().lower()
#         if inp == "exit":
#             break
        
#         try:
#             x, y = map(float, input("Enter two numbers separated by space: ").split())
#             print("Result:", func_dict[inp](x, y))
#         except ZeroDivisionError:
#             print("Cannot divide by zero")
#         except ValueError:
#             print("Please enter valid values")
#         except KeyError:
#             print("You typed a number while entering function name")




# add = lambda x,y: x+y
# sub = lambda x,y: x-y
# mul = lambda x,y: x*y
# div = lambda x,y: x/y

# func_dict = {
#     "add": add, 
#     "sub": sub, 
#     "mul": mul, 
#     "div": div}

# call_func(func_dict)



""" 20 Chatgpt

Write a function that accepts another function as a parameter and calls it twice.
"""

# def calling(calls):
#     calls()
#     calls()

# def function_to_be_called():
#     print("im a functions")


# calling(function_to_be_called)



""" 21 Chatgpt
Create a function that returns multiple functions from within it and call each one individually.
"""


# def returns(l):

#     return 






""" 22 Chatgpt
Write a function that takes a function and a list, applies the function to each element, and returns the modified list (custom map).
"""

# def custom_map(func, l):
#     result = []
#     for i in l:
#         func_output = func(i)
#         result.append(func_output)
#     print(result)
#     return result


# l = [2,3,4,5,6]

# def addon(n):
#     return n*2


# custom_map(addon, l)



""" 23 Chatgpt
Nested Functions, Closures, Decorators, Callbacks

Create a closure that takes an exponent n and returns a function that raises a number to that power."""


# def func(exp):
#     def mult(num):
#         return num ** exp
#     return mult

# call_func = func(3)

# print(call_func(5))



""" 24 Chatgpt

Write a decorator that prints the name of the function before executing it.
"""

# def show_name(func):
#     def wrapper(*args, **kwargs):
#         print("Running:", func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

# @show_name
# def greet():
#     print("Hello")

# greet()


""" 25 Chatgpt
Write a decorator that counts how many times a function has been called."""


# def count_calls(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f"{func.__name__} called {count} times")
#         return func(*args, **kwargs)
#     return wrapper

# @count_calls
# def hello():
#     print("Hello!")

# hello()
# hello()





""" 26 Chatgpt
Write a decorator that logs all function calls to a text file.
"""


# def log_to_file(func):
#     def wrapper(*args, **kwargs):
#         with open("log.txt", "a") as f:
#             f.write(f"Called {func.__name__}\n")
#         return func(*args, **kwargs)
#     return wrapper

# @log_to_file
# def test():
#     print("Function executed")

# test()



""" 27 Chatgpt
Write a callback function that runs after a simulated download is complete.
"""


# import time

# def download(callback):
#     print("Downloading...")
#     time.sleep(1)
#     callback("Download complete!")

# def notify(msg):
#     print("Callback:", msg)

# download(notify)



""" 28 Chatgpt
Write a program where one function takes another function as an argument and executes it only if a condition is True.
"""






""" 29 Chatgpt 
Implement a fallback decorator that returns a default value if the main function fails.
"""


# def fallback(default_value):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except Exception:
#                 return default_value
#         return wrapper
#     return decorator

# @fallback(default_value="Default Result")

# We can write above as follows 
# hold_result = fallback(value)

# some_other = hold_result(risky_divide)


# def risky_divide(a, b):
#     return a / b

# print(risky_divide(10, 0))

""" 30 Chatgpt
Write a function with nested scopes that uses both global and nonlocal keywords to modify variables at different levels.
"""

# x = 5 

# def outer():
#     y = 10
#     def inner():
#         nonlocal y
#         global x
#         y += 1
#         x += 1
#         print("Inner y:", y, "Global x:", x)
#     inner()
#     print("Outer y:", y)

# outer()
# print("Global x:", x)




""" 31 Chatgpt
Write a decorator that takes parameters (for example, a unit of time) and modifies the output message.
"""

# def modify(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return func
#     return wrapper


# @modify
# def give_time(tyme):
#     print("This is the time: ", tyme)

# give_time(10)




""" 32 Chatgpt
Write a function that takes multiple callbacks and executes them in sequence after a simulated event.
"""

# def calls(callback_1, callback_2):
#     give_true = lambda x: True
#     give_false = lambda y: False

#     if give_true(None):
#         callback_1()
#     if give_false(None) == False:
#         callback_2()


# def print_callback(): print("Callback 1 called: ")
# def multiply_callback(): print("callback 2 called: ", 55*33)


# calls(print_callback, multiply_callback)





""" 33 Chatgpt 
Write a decorator that caches the results of a function (simple memoization).
"""
### Memoization means to store result and use the value again if same value occurs, so it does not need to compute again


# def memoize(func):
#     cache = {}
#     def wrapper(*args):
#         if args in cache:
#             print("Cache", cache)
#             print("Args: ", args)
#             print("If block started")
#             return cache[args]
#         result = func(*args)
#         cache[args] = result
#         return result
#     return wrapper

# @memoize
# def fibonacci(n):
#     if n <= 1:
#         return n
#     result = fibonacci(n-1) + fibonacci(n-2)
#     print("Fib number result", result)
#     return result

# print("Fibonaccis: ", fibonacci(10))



""" 34 Online

Matrix Multiplication via List Comprehensions

Write a Python function that performs matrix multiplication using list comprehensions."""


# def mat_mul(l:list, m:list):
#     n = [i*j for i in l for j in m]
#     print(n)
#     return n


# mat_mul([[2,3],[7,2]], [[3,4], [3,4]])

# Matrix is row x column

# mat_a = list(map(int, input("Matrix A size: ").split()))
# mat_b = list(map(int, input("Matrix B size: ").split()))

# rows_a, cols_a = mat_a
# rows_b, cols_b = mat_b

# if cols_a != rows_b:
#     print("NOT Possible: Multiplication requires columns a equal to rows of b")

# mat_A = [[2,3],
#          [4,5]]

# mat_B = [[4,5],
#          [2,3]]



# for i in range(0,len(mat_A[0])+1):
#     for j in mat_B[0]:
#         mat_A[i]




""" 35 Extract Strings by Size Lambda
Write a Python program to extract a specified size of strings from a given list of string values using lambda.

Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']"""


# l = ['Python', 'list', 'exercises', 'practice', 'solution']

# length = int(input("length of string to extract: "))

# new_list = [i for i in l if len(i) == length]

# print("Extracted strings: \n", new_list)



""" 36 Count Floats Lambda
Write a Python program to count float values in a mixed list using lambda.

Original list:
[1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
Number of floats in the said mixed list:
3
"""

# new_l = [input("Enter input:") for i in range(int(input("no of inputs: ")))]

# for i in range(len(new_l)):
#     try:
#         new_l[i] = float(new_l[i])
#         if new_l[i].is_integer():
#             new_l[i] = int(new_l[i])
#     except ValueError:
#         pass

# filtered_list = list(filter(lambda x: isinstance(x, float), new_l))

# print(len(filtered_list))


""" 37 Max/Min Tuple in List Lambda

Write a Python program to find the maximum and minimum values in a given list of tuples using the lambda function.

Original list with tuples:
[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
Maximum and minimum values of the said list of tuples:
(74, 62)
"""

# orig_tuple = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]

# new_tuple = sorted(orig_tuple, key = lambda x:x[1])

# print(f"Maximum:{new_tuple[-1][1]}, Minimum: {new_tuple[0][1]}")



""" 38 Remove None Values Lambda

Write a Python program to remove None values from a given list using the lambda function.

Original list:
[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
Remove None value from the said list:
[12, 0, 23, -55, 234, 89, 0, 6, -12]
"""


# prev_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# newlist = list(filter(lambda x: x is not None, prev_list))

# print(newlist)


""" 39 Sum of Nested Lists Using Recursion

Write a Python program to sum recursion lists using recursion.
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
"""


test_data = [1, 2, [3,4], [5,6], [2,34,[4,3]]]

def cal_sum(test):
    total =0
    for i in test:
        if isinstance(i, list):
            total += cal_sum(i)
        else:
            total += i

    return total
print(cal_sum(test_data))


""" 40
8. Harmonic Series Sum Using Recursion

Write a Python program to calculate the sum of harmonic series upto n terms.

Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example :

1 + (1/2) + (1/3) + (1/4) + (1/5)
"""

# def harmonic_sum_upto(n):
