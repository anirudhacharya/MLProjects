# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

def simulate(dice,grid):
    numberOfSim = 0
    sumOfIter = 0
    for i in range(5000):
        pos = 0
        numberOfIter = 0
        while pos!=99:
            if numberOfIter >= 1000:
                break
            number = (np.random.multinomial(1,dice)).argmax() + 1
            tempPos = pos + number
            if tempPos <= 99:
                pos = tempPos + grid[tempPos]
            numberOfIter += 1
        
        if numberOfIter < 1000:
            numberOfSim += 1
            sumOfIter += numberOfIter
    
    return sumOfIter/numberOfSim

T = int(raw_input())
for i in range(T):
    grid = np.zeros(100)
    dice = [float(i) for i in raw_input().split(',')]
    l,s = [int(i) for i in raw_input().split(',')]
    ladders = raw_input().split(' ')
    snakes = raw_input().split(' ')
    for j in ladders:
        fromPos,toPos = [int(k)-1 for k in j.split(',')]
        grid[fromPos] = toPos-fromPos
    for j in snakes:
        fromPos,toPos = [int(k)-1 for k in j.split(',')]
        grid[fromPos] = toPos-fromPos
    print simulate(dice,grid)