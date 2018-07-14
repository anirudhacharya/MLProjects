import numpy as np
import math
from matplotlib import pyplot as pp

def gaussian2D(x, mu, sigma):
    z = ((np.matrix(x - mu)) * np.linalg.inv(sigma) * (np.matrix(x - mu)).T)*(-0.5)
    temp = math.pow((2*math.pi*np.linalg.det(sigma)), -0.5)
    y = temp * math.exp(z)
    return y

'''if __name__ == '__main__':
    #print gaussian(np.matrix([0,0]),np.matrix([0,0]),np.matrix([[1,0],[0,1]]))         
    #pp.plot(gaussian(np.linspace(-3,3,120), 0, 2))
    '''
    
def gaussian1D(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / 2 * np.power(sig, 2.))/(np.power(2*np.pi, 0.5)*sig)

x = np.linspace(-100, 100, 5000)
pp.plot(x, gaussian1D(x, -10, .10) + gaussian1D(x, 10, 0.5))

pp.show()