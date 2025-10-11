"""
recursion

"""


def square_num(n):
    def calculate():
        print(n*n)
        square_num(4)

    calculate()

square_num(4)

"""
Overwriting built in functions of python
"""