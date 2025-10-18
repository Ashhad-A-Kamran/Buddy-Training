

""" MINION GAME PROBLEM
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12

"""
# def minion_game(s):
#     # your code goes here
#     vowels = ['a', 'e', 'i' , 'o' ,'u']

#     stuart_points = 0
#     kevin_points = 0

#     stuart_list = []
#     kevin_list = []

    

#     def checker(a, string):
#         nonlocal kevin_list
#         nonlocal kevin_points
#         if a in string:
#             kevin_points += 1
#             kevin_list.append(i)
#         return kevin_list

#     for i in s:
#         if i in vowels:
#             kevin_points += 1
#             kevin_list.append(i)
#             b = checker("".join(kevin_list), s)
#             print("B: ", b)
#             print(kevin_list)
#             print("Kevin points if: ", kevin_points)
#         else:
#             kevin_points += 1
#             kevin_list.append(i)

#             print("Else: ", kevin_list)
#             print("Kevin points else: ", kevin_points)


# string = "banana"

# print(minion_game(string))



def minion_game(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()
    print(string)
    n = len(string)

    stuart_score = 0
    kevin_score = 0

    for i in range(n):
        if string[i] in vowels:
            kevin_score += (n - i)
        else:
            stuart_score += (n - i)

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
