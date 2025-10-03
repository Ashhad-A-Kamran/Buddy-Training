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

data = {}

while True:
    all_subjects = set()
    all_marks = []
    add_more = input("\nAdd more names or press X to stop\n")
    if add_more.lower() == "x":
        break
    else: 
        name = input("Name: ")
        age = input("Age: ")
        number_subjects = int(input("Number of subjects: "))
        for i in range(number_subjects):
            subject= input("Subject: ")
            all_subjects.add(subject)

            marks = int(input("Marks: "))
            all_marks.append(marks) 

        data[(name, age)] = [all_subjects, all_marks]

print("\nYou entered:", data)

data["name"] = name


