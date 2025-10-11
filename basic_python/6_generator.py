

"""

Day 6

Pure Functions 

Impure functions 

Lambda Function, lambda function in list comprehension 

Generator,function that used with “yield” keyword. Used 

	Memory effiecient 

	Next keyword built in python function to get the value of generator 

	Tuple comprehension 



"""



l = [lambda args=x: x*10 for x in range(1,5)]


for i in l:
    print(i)



# def l(x=10):
#    return x*10

# for i in range(1,5):
#     print(l())