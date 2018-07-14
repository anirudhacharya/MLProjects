from itertools import chain, combinations, islice
import math

listSum = 0

def powerset(s):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    if len(s)%2==0:
        temp = chain.from_iterable(combinations(s, r) for r in range(len(s)/2))
        temp1 = combinations(s, len(s)/2)
        elem = (math.factorial(len(s))/(2*math.factorial(len(s)/2)))/2
        temp1 = islice(temp1,0,elem,None)
        return chain.from_iterable([temp,temp1])
    else:
        return chain.from_iterable(combinations(s, r) for r in range(len(s)/2 + 1))

def getX(numList):
    subs = powerset(numList)
    diffList = []
    for i in subs:
        diffList.append(abs((2*sum(i)) - listSum))
    return diffList

def mainF(x):
    if x==0:
        return 1
    elif x==1:
        return 3
    else:
        return ((6*mainF(x-1)) - mainF(x-2))
    
N = int(raw_input())
NList = [int(i) for i in raw_input().split(' ')]
listSum = sum(NList)
dList = getX(NList)
M = 0
for i in dList:
    M += mainF(i)
print (M*2)%((10**9)+7)
print powerset(['a','b'])[0]
