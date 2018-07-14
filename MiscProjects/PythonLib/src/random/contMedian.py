import random
import numpy as np
import math
nums = []
N = 10
for i in range(N):
    nums.append(random.choice(range(N*10)))
nums = [67, 51, 86, 60, 32, 1, 0, 91, 29, 64]
startInd = random.choice(range(N))
endInd = random.choice(range(N)[startInd:])

''' Naive method '''
i = startInd 
min = nums[i]
minInd = startInd
while i<=endInd:
    if nums[i]<min:
        min = nums[i]
        minInd = i
    i+=1

print min, minInd
M = np.zeros((N,N))
def process():
    for i in range(N):
        M[i][0] = i
    j=1
    while (1<<j) <= N:
        i=0
        while i+((1<<j)-1) < N:
            if nums[int(M[i][j-1])] <= nums[int(M[int(i + (1<<(j-1)))][j-1])]:
                M[i][j] = M[i][j-1]
            else:
                M[i][j] = M[int(i + (1<<(j-1)))][j-1]
            i+=1
        j+=1

def RMQ(i,j):
    k = int(math.log((j-i),2))
    if(nums[int(M[i][k])] <= nums[int(M[j-(1<<k)+1][k])]):
        return M[i][k]
    else:
        return M[j-(1<<k)+1][k]
process()
print int(RMQ(1,8))    