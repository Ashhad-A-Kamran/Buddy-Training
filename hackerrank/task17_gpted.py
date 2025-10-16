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



