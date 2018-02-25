'''
Created on Oct 1, 2013

@author: Anirudh
'''
"""
This program does MAP, Maximum a priori classification of data 
"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

def main():
    trainingDataset = np.genfromtxt(open('Data/Training.txt','r'), delimiter=' ', 
                                    dtype='f8')
    testingDataset = np.genfromtxt(open('Data/Testing.txt','r'), delimiter=' ', 
                                   dtype='f8')
    class1, class2, class3 = splitDataSet(trainingDataset)
    prior1 = len(class1)/(float)(len(trainingDataset))
    prior2 = len(class2)/(float)(len(trainingDataset))
    prior3 = len(class3)/(float)(len(trainingDataset))
    
    mu1, sigma1 = findParameters(class1)
    mu2, sigma2 = findParameters(class2)
    mu3, sigma3 = findParameters(class3)
    
    dataset = testingDataset #trainingDataset
    classification = classifyData(dataset, mu1, sigma1, mu2, sigma2, mu3, 
                                  sigma3, prior1, prior2, prior3)
    
    dataDoc = np.column_stack((dataset, classification))
    errorCount = calcErrorRate(dataDoc)
    errorRate = errorCount/(float)(len(dataDoc))
    print errorCount, len(dataDoc), errorRate
    np.savetxt('Data/ClassifyTestingMLEP.txt', dataDoc, delimiter='\t', fmt='%f')
    return

def calcErrorRate(dataDoc):
    errorCount = 0
    for row in dataDoc:
        if row[2] != row[3]:
            errorCount = errorCount + 1
    return errorCount

def classifyData(dataset, mu1, sigma1, mu2, sigma2, mu3, sigma3, prior1, prior2, 
                 prior3):
    classification = []
    for row in dataset:
        x = row[0:2]
        if ((prior1 * guassian(x, mu1, sigma1)) > (prior2 * guassian(x, mu2, sigma2)) 
            and (prior1 * guassian(x, mu1, sigma1)) > (prior3 * guassian(x, mu3, 
                                                                         sigma3))):
            classification.append(1)
        elif ((prior2 * guassian(x, mu2, sigma2)) > (prior3 * guassian(x, mu3, 
                                                                       sigma3)) 
              and (prior2 * guassian(x, mu2, sigma2)) > (prior1 * guassian(x, mu1, 
                                                                           sigma1))):
            classification.append(2)
        else:
            classification.append(3)
    return classification

def guassian(x, mu, sigma):
    z = ((np.matrix(x - mu)) * np.linalg.inv(sigma) * (np.matrix(x - mu)).T)*(-0.5)
    temp = math.pow((2*math.pi*np.linalg.det(sigma)), -0.5)
    y = temp * math.exp(z)
    return y

def splitDataSet(dataset):
    list1 = []
    list2 = []
    list3 = []
    for row in dataset:
        if row[2]==1:
            list1.append(row)
        elif row[2]==2:
            list2.append(row)
        elif row[2]==3:
            list3.append(row)
    class1 = np.array(list1)[:,0:2]
    class2 = np.array(list2)[:,0:2]
    class3 = np.array(list3)[:,0:2]
    return class1, class2, class3

def findParameters(dataArray):
    mu = dataArray[:,0:2].mean(0,'f8')
    sigma = np.matrix([[0,0],[0,0]])
    for row in dataArray:
        temp = np.matrix(row) - np.matrix(mu)
        sigma = sigma + (temp * temp.T)
    sigma = sigma / (dataArray.size-1)
    return mu, sigma

if __name__ == '__main__':
    main()