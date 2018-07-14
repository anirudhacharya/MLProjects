'''
Created on Aug 23, 2014

@author: Anirudh
'''
'''
The logic is to maintain a small array of minimum percentage. We start off with an array of length 5 holding 101 values each.
We make one pass with the input values and read values from the 
'''
import sys

minList = [101 for i in range(5)]
min = minList[0]

def insert(num):
    minList.append(num)
    sorted(minList)
    minList.pop()
    return

while True:
    num = float(raw_input())
    if num is None:
        break
    if num <= minList[-1]:
        insert(num)
        
for n in minList:
    print("%.6f" % round(n,6))