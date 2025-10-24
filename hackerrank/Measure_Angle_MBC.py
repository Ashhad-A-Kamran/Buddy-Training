"""
Find the Angle MBC

LINK: https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

ABC is a right triangle, 90° at B.
Therefore, ∠ABC = 90°.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.

Your task is to find ∠MBC (angle θ°, as shown in the figure) in degrees.

Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.

"""




import math

AB = int(input())
BC = int(input())

AC = ((BC**2) + (AB**2))**0.5
MC = AC/2

AM = MC

angle_BCM = math.acos((((BC**2) + (AC**2)) - (AB**2) )/(2*BC*AC)) 



BM = math.sqrt(((BC**2) + (MC**2)) - math.cos(angle_BCM) * (2*BC*MC))

angle_MBC = math.asin((math.sin(angle_BCM) * MC) /  BM)
angle_MBC_deg = math.degrees(angle_MBC)
print(f"{round(angle_MBC_deg)}\u00b0")
