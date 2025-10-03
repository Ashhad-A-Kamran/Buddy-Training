


"""
Task 4

You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen."""



def split_and_join(line):
    line_split = line.split(" ")
    line_joined = "-".join(line_split)
    return line_joined
    

line = input()
result = split_and_join(line)
print(result)