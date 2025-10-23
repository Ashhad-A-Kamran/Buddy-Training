"""

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1 and time t2.



Input:
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

Output:
25200
88200

"""

import math
import os
import random
import re
import sys
from dotenv import load_dotenv

load_dotenv()

# Complete the time_delta function below.
def time_delta(t1, t2):
    list_1 = t1.split() # [Sun, 10, May, 2015, 13:54:36, -0700]
    list_2 = t2.split()

    time_1, time_2 = list_1[-2], list_2[-2]

    hour_1 = time_1.split(":")
    hour_2 = time_2.split(":")


    total = 0

    for k in list_1:

        if k == 4:
            for i,j in enumerate(k):
                
                if i == 0:
                    hours = int(j) - int(hour_2[0])
                    pos_hours = abs(hours)
                    total += (pos_hours * 3600)
                if i == 1:
                    minutes = int(j) - int(hour_2[1])
                    pos_minutes = abs(minutes)
                    total += (pos_minutes * 60)
                if i == 2:
                    seconds = int(j) - int(hour_2[2])
                    pos_seconds = abs(seconds)
                    total += pos_seconds

        if k == 1:
            days = int(k) - int(list_2[k])
            total += (abs(days)*24*3600)

        if k == 5:
            hours = int(k) - int(list_2[k][1]) 
            positive_hours = abs(hours)
            total += (positive_hours * 3600)

            minutes = int(list_1[k][2:]) - int(list_2[k][2:])
            positive_minutes = abs(hours)

            total += (positive_minutes * 60)


    return str(total)






# fptr = open(os.environ["OUTPUT_PATH"], 'w')

t = int(input())

for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)
#     fptr.write(delta + '\n')

# fptr.close()
