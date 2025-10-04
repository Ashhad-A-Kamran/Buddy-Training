"""# Task 1
# Given a list of words, create a dictionary mapping each word to its length.
"""
# words = input("Enter words: ").split(" ")
# l = {word: len(word) for word in words}
# print(type(l))
# print("L: ", l)

#======================================================
"""# Task 2
# Given a string, create a dictionary mapping each character to the number of times it appears."""

# words = input("Enter words: ")

# dict2={i: words.count(i) for i in words}

# print(dict2)


#======================================================
"""# Task 3
# Even or Odd Mapping
# Create a dictionary for numbers 1–20 where the key is the number and the value is "even" or "odd"."""


# dict3 = {i:"odd" if i%2 else "even" for i in range(1,2)}

# print(dict3)

#======================================================

"""# Task 4 Student Grades
# Given a dictionary of students and their marks, use dictionary comprehension to create a new dictionary that stores only the students who scored 50 or more.
"""
# student_marks = {"Ash": 55, "Had": 65, "Osama": 40,"Hamza": 65}

# dict4 = {key:value for key, value in student_marks.items() if value>=50}

# print(dict4)


#======================================================
"""#Task5

# Word Frequency (Case-Insensitive)
# Given a sentence, build a dictionary that counts how many times each word appears (ignoring case)."""


# sentence = "My name is Ashhad, and the coffee is on the coffee"

# splitted = sentence.split(" ")
# print(splitted)

# dict5 = {splitted[x]: (sentence.count(str(splitted[x]))) for x in splitted}
# print(dict5)

