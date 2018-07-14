'''
Created on May 19, 2014

@author: Anirudh
'''
import random
import numpy as np

fHandle = open('dice.txt','a')
fHandle.truncate()
for i in range(10000):
    if random.random() < 0.35:
        fHandle.write('1')
    else:
        fHandle.write('0')
    fHandle.write('\n')
    