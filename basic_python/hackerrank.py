#Task1
# n = int(input())

# for i in range(1,n+1):
#     print(i, end="")



#Task2
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# A = set(map(int, input().split()))
# B = set(map(int, input().split()))

# happiness = 0

# for x in arr:
#     if x in A:
#         happiness += 1
#     elif x in B:
#         happiness -= 1

# print(happiness)



#Task3
# n = int(input())
# stamps = set()

# for i in range(0,n):
#     countries = input().strip()
#     stamps.add(countries)
    
# print(len(stamps))



#Task 4
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    line_split = line.split(" ")
    line_joined = "-".join(line_split)
    return line_joined
    

line = input()
result = split_and_join(line)
print(result)