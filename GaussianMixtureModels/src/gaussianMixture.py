'''
Created on Apr 11, 2014

@author: Anirudh
'''
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import matplotlib as mpl
from sklearn import mixture
import itertools

data1 = np.genfromtxt(open('data/dataset1.txt','r'), delimiter=' ', dtype='f8')
data2 = np.genfromtxt(open('data/dataset2.txt','r'), delimiter='  ', dtype='f8')
K=3

def main():
    data = data2
    dataCov = np.cov(data.T)
    mu = np.zeros((K,2))
    covar = {}
    mixCoeff = [1.0/K for i in range(K)]
    response = np.zeros((len(data),K))
    mu = np.array([[1.89165417, 0.24267632],[-1.11387973, 0.13775981],[0.32698275, -0.21492636]])
    #mu = np.array([[3.01698571, 0.04558442],[-0.13084763, -0.05305959]])
    
    covar[1] = np.cov(data[:100].T)
    covar[2] = np.cov(data[500:600].T)
    covar[0] = np.cov(data[100:150].T)
    
    for i in range(K):
        mu[i] = data[random.choice(range(len(data)))]
        #covar[i] = dataCov #findParameters(data, mu[i])
        #mixCoeff[i] = 1.0/K'''
    
    print mu
    #print covar
    likelihood = [0]
    for i in range(100):
        print i
        response = expectation(data, mu, covar, mixCoeff)
        mu, covar, mixCoeff = maximization(data, mu, covar, mixCoeff, response) 
        
        tempLikelihood = 0
        for point in data:
            sum = 0
            for k in range(K):
                sum = sum + (mixCoeff[k] * multiVarGaussian(point,mu[k],covar[k]))
            tempLikelihood = tempLikelihood + math.log(sum)
        print tempLikelihood
        if (abs(likelihood[-1] - tempLikelihood) < 0.1 ):
            break
        likelihood.append(tempLikelihood)
        
    fig = plt.figure()
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1,1,1)
    ax1.set_title("Gaussian Mixture Clustering of Dataset 2")
    ax1.plot(range(len(likelihood)-1),likelihood[1:],'r', linewidth=1)
    ax1.plot(range(len(likelihood)-1),likelihood[1:],'ro',linewidth=2)
    plt.ylabel("Maximum Likelihood")
    plt.xlabel("Iteration")

    ax = fig.add_subplot(1,1,1)
    ax.set_title("Random initialization Clustering - Dataset2")
    for i,row in enumerate(data):
        r = response[i][0]
        g = response[i][1]
        b = response[i][2]
        ax.scatter([row[0]],[row[1]], color=(r,g,b))
    
    plt.show()
    print mu

def expectation(data, mu, covar, mixCoeff):
    response = np.zeros((len(data),K))
    for i,point in enumerate(data):
        for j in range(K):
            response[i][j] = mixCoeff[j] * multiVarGaussian(point, mu[j], covar[j])
        response[i] = response[i]/sum(response[i])
    return response

def maximization(data, mu, covar, mixCoeff, responsibility):
    for i in range(K):
        N_k = sum(responsibility[:,i])
        mu[i] = [sum(responsibility[:,i] * data[:,0]), sum(responsibility[:,i] * data[:,1])] / N_k
        temp = (responsibility[:,i] * (data - mu[i]).T)
        covar[i] = (np.asmatrix(temp,'f8') * (np.asmatrix(temp, 'f8')).T) / N_k
        mixCoeff[i] = N_k / len(data)
    return mu, covar, mixCoeff

def multiVarGaussian(x, mu, covar):
    D = len(x)
    x1 = np.matrix(x - mu)
    x2 = np.linalg.inv(covar)
    x3 = (np.matrix(x - mu)).T
    z = x1 * x2 * x3 *(-0.5)
    temp = math.pow((((2*math.pi) ** D)*np.linalg.det(covar)), -0.5)
    y = temp * math.exp(z)
    return y

def findParameters(dataArray, mu):
    #mu = dataArray[:,0:2].mean(0,'f8')
    sigma = np.matrix([[0,0],[0,0]])
    for row in dataArray:
        temp = np.matrix(row) - np.matrix(mu)
        sigma = sigma + (temp * temp.T)
    sigma = sigma / (dataArray.size-1)
    return np.asanyarray(sigma)
                                                                
if __name__ == '__main__':
    main()