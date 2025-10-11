""" Closure

Write a function make_multiplier(n) that returns another function which multiplies any given number by n.

For example:
double = make_multiplier(2)
print(double(5))  # 10
"""

# def make_multiplier(n):
#     def multiply(x):
#         return x*n
#     return multiply

# double = make_multiplier(2)
# print(double(5))



""" Closure
Running Average
Create a closure running_average() that returns a function. Each call updates and returns the current average of all numbers passed so far.
"""


# def running_average():
#     l = []
#     def calc(n):
#         l.append(n)
#         return sum(l)/len(l)
#     return calc

# add_num = running_average()

# print("Your Average: ", add_num(5))
# print("Your Average: ", add_num(6))
# print("Your Average: ", add_num(8))



""" Closure
Countdown Function
Write a closure that initializes a number and returns a function that decreases it by 1 each time you call it.
"""

# def outer():
#     d = 5
#     def inner():
#         nonlocal d
#         d -= 1
#         return d
#     return inner


# count = outer(10)
# print(count())
# print(count())
# print(count())




""" Decorator
Execution Timer
Create a decorator @timeit that measures how long a function takes to run.
"""

# import time

# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
        
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Function execution took {end - start} seconds")
#     return wrapper

# @timeit
# def new_func():
#     return 500*500

# @timeit
# def calculate_sum(n,m):
#     return n+m

# new_func()
# calculate_sum(m=8,n=7)

""" Decorator
Require Login
Write @require_login decorator that only runs the function if logged_in = True.
"""

# logged_in = True


# def require_login(func):
#     def wrapper(*args, **kwargs):
#        if func(*args, **kwargs):
#            print("You have logged in!")
#        else:
#             print("Please Login first") 



#     return wrapper


# @require_login
# def abcd(id, password):
#     if id == "Osama" and password == "123":
#         return True


# abcd("Osama", "123")

# abcd("Osama1", "123")



""" Decorator
Error Catcher
Decorator that catches exceptions and prints "Error occurred" instead of crashing."""


data = 4

def error_catcher(func):
    def wrapper():
        try:
            return func()
        except Exception:
            print("Error occurred")
    return wrapper

@error_catcher
def give_data():
    print("Data is of acceptable type. Please proceed")


give_data()
        

""" Higher Order Function
Apply Twice
Write apply_twice(func, value) that calls func(func(value)).
"""


# def apply_twice(func, value):
#     return func(func(value)) # -> return add_num(add_num(value))


# def add_num(value):
#     return value+1


# print(apply_twice(add_num, 1))



"""  Higher Order Function
Filter Evens
Implement your own version of Python’s filter() using a higher-order function.
"""








"""  Higher Order Function
Compose Functions
Build compose(f, g) that returns a new function h(x) = f(g(x))."""

# def compose(f,g):
#     pass






""" Callback

Custom Sort Callback
Pass a callback function to sort a list of tuples by the second element.
"""


# list_of_tuples = [(1,2,3,4), (2,3,4,5)]

# def sort_list(callback):
#     print("sorting list")
#     print("result of callback: ", callback(list_of_tuples))
#     print("\n\nSorting complete")


# def callback(l):
#     l.sort(key = lambda x: x[1],reverse=True)
#     return l

# sort_list(callback)



""" Callback
Event Trigger
Write a function on_event(callback) that calls callback() when a condition is met.
"""


# x = [1,2,3,4,5]

# def on_event(callback):
#     for i in x:
#         if i > 5:
#             callback()
#         else:
#             print("condition not satisfied")


# def callback():
#     print("x is greater than 5")


# on_event(callback)




""" Callback
Download Simulation
Simulate a file download — call a progress_callback(percent) function every 10%."""

# import time

# def downloading(callback):
#     for i in range(0,101):
#         time.sleep(0.1)
#         callback(i)


# def progress_callback(x):
#     if x%10 ==0:
#         print(f"Downloaded {x}%")

# downloading(progress_callback)




# =======================================================================

# ADVANCED

# =======================================================================

"""
1. Higher-Order Function Problem

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





"""
2. Callback Function Problem

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





















"""
3. Closure Function Problem

Problem:
Write a closure make_counter(start) that returns two functions:

increment() → increases the count and returns it

decrement() → decreases the count and returns it

Each counter should keep its own internal state (independent of others).

Example:

counter1 = make_counter(10)
counter2 = make_counter(0)

print(counter1['increment']())  # 11
print(counter1['decrement']())  # 10
print(counter2['increment']())  # 1


Hint:
Use nonlocal to modify a variable inside nested functions.
"""


















"""
4. Decorator Problem

Problem:
Write a decorator time_logger that:

Records how long the wrapped function took to run

Prints: Function <name> took X.XXX seconds

Example:

@time_logger
def slow_function():
    import time
    time.sleep(1.2)
    print("Done")

slow_function()


Expected Output:

Done
Function slow_function took 1.200 seconds


Hint:
Use time.time() before and after the function call.
"""