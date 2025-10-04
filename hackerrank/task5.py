


"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

"""


records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])

records_sorted = sorted(records, key=lambda x:x[1])

scores = sorted(set([s for n, s in records]))

second_lowest = scores[1]


second_lowest_students = [n for n,s in records_sorted if s==second_lowest]

for i in sorted(second_lowest_students):
    print(i)
    
