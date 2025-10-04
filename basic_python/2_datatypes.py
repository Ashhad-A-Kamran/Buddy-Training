


#
# List
# import sys

# li = []
# size = sys.getsizeof(li)
# print("before appending", id(li))
# print("empty list size:", size)

# for i in range(10):
#     li.append(i)
# print("after appending", id(li))
# print("size after appending:", sys.getsizeof(li))



#indexing and slicing
# l = [4,5,6,7,8,9]

# print(l[1:-1])


# del l[2]
# del l[1:3]
# del l

# l.remove(5)


# l.pop(5)


# # removes the elements of the list
# l.clear()


# # Order mattes in list
# l1 = [1,2,3]
# l2 = [3,2,1]
# print(l1==l2)

# sorted_l1 = sorted(l1)

# sort = l1.sort()



# Tuple
# t = (1, 2, 3)
# print(t)

# # elements can be added in tuple
# t = t + t
# print(t)

# t = t - t
# print(t)


# immutable

# tuple unpacking
    # a,b,c = (1,2,4)
    # print(a,b,c)

# """we can do this:
# """
# d3 = dict([(1,1), (2,2), (3,3)])
# print(d3)

# # Mutable data types cannot be "keys"
# data= {(1,2,3,4): "im here"}

# print(data)




# Assignment 1

# data = {
#     "Person1": [75, 85, 96],
#     "Person2": [88, 92, 80],
#     "Person3": [90, 85, 87]
# }


# data["Person4"] = [55,66,77]
# data["Person5"] = [54,65,76]
# data["Person6"] = [53,64,75]

# print(data)

# def average_sorted(data):
#     avgs = []
#     dict2 = {}
#     for i in data:
#         avg = sum(data[i]) / len(data[i])
#         avg = round(avg, 2)
#         avgs.append(avg)
#         dict2[i] = avg
#     print("\nDictionary 2:",tuple(dict2.items()))
#     return sorted(tuple(dict2.items()), key= lambda x: x[1], reverse=True)
    
# # sorted(key= 
# sorted_tuple = average_sorted(data)
# print("\n Sorted tuple: ", sorted_tuple)




# # Assignment 2

# data = {}

# while True:
#     all_subjects = set()
#     all_marks = []
#     add_more = input("\nAdd more names or press X to stop\n")
#     if add_more.lower() == "x":
#         break
#     else: 
#         name = input("Name: ")
#         age = input("Age: ")
#         number_subjects = int(input("Number of subjects: "))
#         for i in range(number_subjects):
#             subject= input("Subject: ")
#             all_subjects.add(subject)

#             marks = int(input("Marks: "))
#             all_marks.append(marks) 

#         data[(name, age)] = [all_subjects, all_marks]

# print("\nYou entered:", data)




# # Assignment 3
# import json
# product1 = {
#     "info": ("Shoe", "wearable"),
#     "price": 1001,
#     "ratings": [1,9,3],
#     "tags": ("tag1", "tag2", "tag3")
# }

# product2 = {
#     "info": ("Bottle", "Usable"),
#     "price": 1090,
#     "ratings": [2,2,3],
#     "tags": ("tag1", "tag2", "tag3")
# }

# product3 = {
#     "info": ("Perfume", "Fragments"),
#     "price": 1400,
#     "ratings": [1,4,3],
#     "tags": ("tag1", "tag2", "tag3")
# }

# cart = [product1, product2, product3]

# # category of the second product
# print(cart[1]["info"][1])

# # total price of all the products
# overall_sum = 0
# for i in range (len(cart)):
#     overall_sum = overall_sum + cart[i]["price"]
#     print(overall_sum)

# #average rating of first product
# rating = sum(cart[0]["ratings"]) / len(cart[0]["ratings"])
# print("average rating of 1st product: ", rating)

# #combine all tags from products using | operator
# all_tags = ""
# for i in range(len(cart)):
#     a,b,c = cart[i]["tags"]
#     print(a,b,c, sep="|", end="|")

# # # input your data into the cart
# name = input("Product name: ")
# category = input("Product category: ")
# price = int(input("Product price: "))
# ratings = []
# tags = tuple()
# for i in range(0,3):
#     add_ratings = int(input(f"Enter 3 ratings ({i+1}/3): "))
#     ratings.append(add_ratings)

#     add_tags = input(f"Enter tag ({i+1}/3): ")
#     tags = tags + (add_tags,)

# new_product = {
#     "info": (name, category),
#     "price": price,
#     "ratings": ratings,
#     "tags": tags
# }

# cart.append(new_product)

# print(json.dumps(cart, indent=4))



# Assignment 4
students = {
    "Ali": [80, 90, 85],
    "Sara": [70, 75, 80],
    "Usman": [90, 95, 92],
    "Ayesha": [60, 65, 58]
}

print("Student List: ", students.items())

total_marks = 0
avg_marks = 0

student_list = []
for key,values in students.items():
    total_marks = sum(students[key])
    avg_marks = sum(students[key]) / len(students[key])
    student_list.append((key, total_marks, avg_marks))
    
    print("Total marks: ", total_marks, end=", ")
    print("Average Marks:   ", avg_marks)

print(student_list)

# Sort based on average marks in descending order
sorted_students = sorted(student_list, key= lambda x: x[2], reverse=True)

print("\nSorted students based on average marks: ", sorted_students)


# Convert to dicitonary

sorted_dict = {}
for i in range(len(sorted_students)):
    name = sorted_students[i][0]
    sorted_dict[name] = (sorted_students[i][1], sorted_students[i][2])

print("sorted_dict: ", sorted_dict)
for i,item in enumerate(sorted_dict.items()):
    if i<2:
        print("Top students: ", item[0])
    else:
        break


