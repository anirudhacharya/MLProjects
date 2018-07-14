'''
Created on Sep 6, 2014

@author: Anirudh
'''
import numpy as np

def main():
    F,N = [int(i) for i in raw_input().split(' ')]
    B = np.zeros(N)
    A = np.zeros((N,F))

    for i in range(N):
        line = raw_input().split(' ')
        B[i] = line[-1]
        A[i] = line[:F]

    T = int(raw_input())
    test = np.zeros((T,F))
    for i in range(T):
        line = raw_input().split(' ')
        test[i] = line
    
    test = np.column_stack((np.ones(T),test))
    A = np.column_stack((np.ones(N),A))
    alpha = 0.3 
    model = LinRegression()
    w = model.getParameters(A, B, alpha, N, F)
    y = model.solve(w, test, T)
    for val in y:
        print val
        return
    '''
    print w
    print A
    print B
    import matplotlib.pyplot as pyplot

    pyplot.plot(Jval,range(len(Jval)),'r')
    pyplot.show()
    '''    
    
class LinRegression:
    def __init__(self):
        return
    
    def getParameters(self, A, B, alpha, N, F):
        w = np.ones(F+1)
        h = np.dot(w,A.T)
        J = sum((h-B)**2)/(2*N)
        Jval = []
        Jval.append(J)
        while True:
            dJ = (h - B)/N
            for i in range(F+1):
                w[i] = w[i] - alpha*sum(dJ * A[:,i])    
        
            prevJ = J
            h = np.dot(w,A.T)
            J = sum((h-B)**2)/(2*N)  
            Jval.append(J)  
            if abs(J-prevJ)<0.0001:
                break
        
        return w
    
    def solve(self, w, test, T):
        for i in range(T):
            y = np.dot(w,test.T)
        return y

if __name__ == '__main__':
    main()