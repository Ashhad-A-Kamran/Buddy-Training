"""
Explanantion
"""
l = [1,2,3,4,5,6,7,8,9]

# l2 = [i**2 for i in l]

# print(l2)


# l3 = [i for i in range(2,11,2)]
# print(l3)



"""
# Task1
Print all the odd prime numbers between 1 and 50 (both included) using list comprehension.
"""
# l = [i for i in range(0,50) if i%2 == 1 and i%3 !=  0]

# for i in range(1,51,2):
#     is_prime = True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime = False
#             break
#     if is_prime:
#         print("i: ", i)




"""
Dictionary Comprehension
Create a dictionary with student names as keys and their scores as values. Then, use dictionary comprehension to create a new dictionary that contains only the students who scored above 80.
"""
 
dict1 = {x: x**2 for x in range(1, 6)}

print(dict1)
