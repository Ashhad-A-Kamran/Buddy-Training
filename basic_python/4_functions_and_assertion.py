

"""
check if a is non 0 using assert

"""


# def quadratic_checker(a,b,c):
#     assert a!=0, "Division by zero error"
#     return print(-(b) + ((4 * a * c)**0.5) / (2 * a))


# quadratic_checker(4,3,0)
# quadratic_checker(0,2,4)



"""
Check even odd 

"""

# l = list(range(1,11))

# def check_even_odd(n):
#     if n%2 == 0:
#         return "Even" 
#     else:
#         return "Odd"


# # flag = check_even_odd(l)

# even_list = []
# odd_list = []

# for i in l:
#     if check_even_odd(i) == "Even":
#         even_list.append(i)
#     else:
#         odd_list.append(i)

# print(even_list)
# print(odd_list)


"""
fibonacci series

"""


def fibonacci(n=10):
    a, b= 0,1

    for _ in range(n):
        print(a, end=" ")

        a, b = b, a+b
        print(b)

fibonacci()



"""
Can be assigned to another variable

"""

def abc():
    print("hello")


newfunc = abc
newfunc