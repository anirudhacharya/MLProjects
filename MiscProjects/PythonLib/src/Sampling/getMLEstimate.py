'''
Created on May 19, 2014

@author: Anirudh
'''
import numpy as np

fHandle = open('bernouliTrials.txt','r')
trainData = np.genfromtxt('input.txt', dtype='f8', delimiter=' ')
count = 0
for i in trainData:
    if i==1:
        count += 1
print (count*1.0)/len(trainData)