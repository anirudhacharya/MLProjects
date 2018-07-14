import numpy as np
from cvxopt import matrix, solvers
'''
Q = 2*matrix([ [2, .5], [.5, 1] ])
p = matrix([1.0, 1.0])
#G = matrix([[-1.0,0.0],[0.0,-1.0]])
#h = matrix([0.0,0.0])
A = matrix([1.0, 1.0], (1,2))
b = matrix(1.0)
sol=solvers.qp(Q, p, A, b)
print(sol['x'])

P = matrix(np.identity(5), tc='d')
q = matrix(np.array([4,1,0,2,3]), tc='d')
G = -1*matrix(np.identity(5), tc='d')
h = matrix(np.array([0,0,0,0,0]), tc='d')
A = matrix([1.0,0.0,2.0,3.0,4.0], (1,5))
b = matrix([4.0])

sol = solvers.qp(P,q,G,h,A,b)
print(sol['x'])
'''

def quadProg():
    fin = open('in_file.txt','r')
    input = fin.read().split('\n')
    y_t = np.array([float(input[0])])
    line = input[1].split(',')
    w_t = np.array([float(i) for i in line])
    line = input[2].split(',')
    x_t = np.array([float(i) for i in line])
    
    dim = len(line)
    #P = matrix(np.identity(5), tc='d')
    P = matrix(np.identity(dim), tc='d')
    #q = matrix(np.array([4,1,0,2,3]), tc='d')
    q = -1 * matrix(w_t, tc='d')
    #G = -1*matrix(np.identity(5), tc='d')
    G = -1*matrix(np.identity(dim), tc='d')
    #h = matrix(np.array([0,0,0,0,0]), tc='d')
    h = matrix(np.zeros(dim), tc='d')
    #A = matrix([1.0,0.0,2.0,3.0,4.0], (1,5))
    A = matrix(x_t, (1,dim))
    #b = matrix([4.0])
    b = matrix(y_t)
    
    print P
    print q
    print G
    print h
    print A
    print b
    try:
        sol = solvers.qp(P,q,G,h,A,b)
    except:
        oPut = w_t
    oPut = [round(i,2) for i in sol['x']]
    fout = open('out.txt','w')
    fout.write(" ".join(str(i) for i in oPut))
    print(oPut)

if __name__ == '__main__':
    quadProg()