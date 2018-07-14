import numpy as np
import scipy.special as ss
import pylab as pl
import math
import nltk

def main():
    plot(0.1,0.1)
    plot(1,1)
    plot(2,3)
    plot(10,10)
    plot(20,30)
    pl.legend()
    pl.show()
    return
    
def betaFunc(pr,alpha,beta):
    const = math.gamma(alpha+beta)/(math.gamma(alpha)*math.gamma(beta))
    temp = const*(pr**(alpha-1))*((1-pr)**(beta-1))
    return temp

def plot(alpha,beta):
    Ly = []
    Lx = []
    pr = np.mgrid[0:1:100j]
    for p in pr:
        Lx.append(p)
        Ly.append(betaFunc(p,alpha,beta))
        
    pl.plot(Lx,Ly,label="a=%f, b=%f" %(alpha,beta))
    
if __name__ == "__main__":
    main()