

"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.


"""



n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr), reverse=True)
    
print(sorted_arr[1])