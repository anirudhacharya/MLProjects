'''
Created on Apr 9, 2014

@author: Anirudh
'''

import numpy as np
import matplotlib.pyplot as plt
import random

data1 = np.genfromtxt(open('data/dataset1.txt','r'), delimiter=' ', dtype='f8')
data2 = np.genfromtxt(open('data/dataset2.txt','r'), delimiter='  ', dtype='f8')
data = data2
K=3

def main():
    mu = np.zeros((K,2))
    for i in range(K):
        mu[i] = random.choice(data)
    print mu
    r,mu = kMeansClassifier(mu, K, data)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1) 
    
    """ax.set_title("Data set 1 color coded scatter plot of data")
    ax.scatter(data1[:,0][:800], data1[:,1][:800], color='red')
    ax.scatter(data1[:,0][800:], data1[:,1][800:], color='blue')
    #ax.scatter(data2[:,0][1000:1500], data2[:,1][1000:1500], color='green')"""
    
    for i,point in enumerate(data):
        if r[i]==0:
            ax.scatter(point[0], point[1], color='orange')
        elif r[i]==1:
            ax.scatter(point[0], point[1], color='green')
        else:
            ax.scatter(point[0], point[1], color='blue')
    print mu
    ax.scatter([mu[0][0]], [mu[0][1]], color='red')
    ax.scatter([mu[1][0]], [mu[1][1]], color='red')
    ax.scatter([mu[2][0]], [mu[2][1]], color='red')
    
    plt.show()

def kMeansClassifier(mu, K, data):
    r = np.zeros((len(data)))
    mu = np.zeros((K,2))
    J = 0
    for i in range(30):
        print i
        r = expectation(mu, r, data)
        mu = maximization(mu, K, r, data)
        tempJ = 0
        for i,point in enumerate(data):
            cluster = r[i]
            tempJ = tempJ + np.linalg.norm(data - mu[cluster]) ** 2
        tempJ = tempJ / len(data)
        print tempJ    
        if abs(J - tempJ) < 0.1:
            break
        J = tempJ
    return r,mu
        
def expectation(mu, r, data):
    for i,dataPoint in enumerate(data):
        dist = np.zeros(K)
        for j,mean in enumerate(mu):
            dist[j] = np.linalg.norm(dataPoint-mean)
            
        r[i] = np.argmin(dist)
    return r
    
def maximization(mu, K, r, data):
    new_mu = np.zeros((K,2))
    numPoints = np.zeros(K)
    for i, dataPoint in enumerate(data):
        category = r[i]
        numPoints[category] = numPoints[category] + 1
        new_mu[category] = ((new_mu[category] * (numPoints[category]-1)) + dataPoint) / numPoints[category]
        
    mu = new_mu
    return mu

if __name__ == '__main__':
    main()
    '''print "END"
    print np.mean(data2[:500][:,0]), np.mean(data2[:500][:,1])
    print np.mean(data2[500:1000][:,0]), np.mean(data2[500:1000][:,1])
    print np.mean(data2[1000:1500][:,0]), np.mean(data2[1000:1500][:,1])'''