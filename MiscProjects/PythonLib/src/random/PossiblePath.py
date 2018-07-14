'''
Created on Jun 14, 2014

@author: Anirudh
'''
from fractions import gcd

T = int(raw_input())
for i in range(T):
    num = [int(i) for i in raw_input().split(' ')]
    a = num[0]
    b = num[1]
    x = num[2]
    y = num[3]
    factor = gcd(a,b)
    if (x%factor)==0:
        if (y%factor)==0:
            print "YES"
    else:
        print "NO"
