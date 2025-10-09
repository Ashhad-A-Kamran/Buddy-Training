

"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

"""


N = int(input())
l = []

for i in range(N):
    take_input = input().split()

    if take_input[0] == "insert":
        l.insert(int(take_input[1]), int(take_input[2]))
    elif take_input[0] == "print":
        print(l)
    elif take_input[0] == "remove":
        l.remove(int(take_input[1]))
    elif take_input[0] == "append":
        l.append(int(take_input[1]))
    elif take_input[0] == "sort":
        l.sort()
    elif take_input[0] == "pop":
        l.pop()
    elif take_input[0] == "revers`e":
        l.reverse()

