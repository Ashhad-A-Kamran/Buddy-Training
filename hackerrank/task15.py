"""Let's use decorators to build a name directory! You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input."""



n = int(input("How many people? "))
data_dict = {
    "first_name": [],
    "last_name": [],
    "age": [],
    "sex": []}


for i in range(n):
    data = input("").split(" ")

    data_dict["first_name"].append(data[0])
    data_dict["last_name"].append(data[1])
    data_dict["age"].append(data[2])
    data_dict["sex"].append(data[3])
    


people = list(zip(
    data_dict["first_name"],
    data_dict["last_name"],
    data_dict["age"],
    data_dict["sex"],
    ))


people.sort(key=lambda x :x[2])

print(people)





# import operator

# def person_lister(f):
#     def inner(people):




#     return inner

# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# people = [input().split() for i in range(int(input()))]
# print(*name_format(people), sep='\n')