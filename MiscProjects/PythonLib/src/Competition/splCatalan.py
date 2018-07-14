'''
Created on Jun 4, 2014

@author: Anirudh
'''
import math
import timeit

def binomial(n,r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

def catalyn(n):
    return binomial(2*n,n)/(n+1)

start = timeit.timeit()
T = int(raw_input())
flowers = []
for i in range(T):
    num = int(raw_input())
    result = 0
    i=1
    while i <= num:
        result = result + (binomial(num,i)*catalyn(i))
        i = i+1
    print result
    
end = timeit.timeit()
print end-start