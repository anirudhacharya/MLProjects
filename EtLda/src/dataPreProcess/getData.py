'''
Created on Mar 29, 2014

@author: Anirudh
'''
#from __future__ import print_function
import numpy as np

'''
dataMat = np.genfromtxt(open('data/corpus.csv','r'), delimiter=',')[1:4]
seperatedData = {}
for row in dataMat:
    curYear = row[0]
    if(curYear in seperatedData):
        seperatedData[curYear] + "\n" + (row[1:])
    else:
        seperatedData[curYear] = row[1] + " " + row[2]
        
fileH = open('out.txt','w')
fileH.write(seperatedData[0])
'''
fHandle = open('./../data/coloradodebate.txt','r')
str=fHandle.readline()
while True:
    str = str[str.find('-')+1:]
    print str.strip()
    str = fHandle.readline()
    if str==None or str=="":
        break