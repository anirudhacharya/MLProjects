'''
Created on Jan 2, 2014

@author: aachary8
'''
import numpy as np

def EditDistance(str1, str2):
    """
    
    """
    str1 = str1.lower()
    str2 = str2.lower()
    len1 = len(str1)+1
    len2 = len(str2)+1
    distMat = np.zeros((len1,len2))
    distMat[0] = range(len2)
    distMat[:,0] = range(len1)
    dirMat = np.zeros((len1,len2)) 
    i = 1
    while i < len1:
        j = 1
        while j < len2:
            #print str1[i-1], str2[j-1]
            if(str1[i-1] == str2[j-1]):
                listOfVal = [distMat[i-1][j-1], (distMat[i-1][j]+1), (distMat[i][j-1]+1)]
                distMat[i][j] = min(listOfVal)
                dir = listOfVal.index(min(listOfVal))
                '''
                0 --> when letters are same
                1 --> when removing or adding a letter
                2 --> when swapping a letter
                '''
                dirMat[i][j] = dir
            else:
                listOfVal = [(distMat[i-1][j-1]+2), (distMat[i-1][j]+1), (distMat[i][j-1]+1)]
                distMat[i][j] = min(listOfVal)
                dir = listOfVal.index(min(listOfVal))
                '''
                0 --> diagonal
                1 --> up
                2 --> left
                '''
                dirMat[i][j] = dir
            j = j+1
        i = i+1
    print distMat
    print dirMat
    return distMat[len1-1][len2-1]

if __name__ == '__main__':
     #print EditDistance('aaabd','aaaaabbd')
     print EditDistance('a','aaaaabbd')