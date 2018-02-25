'''
Created on Oct 9, 2013

@author: Anirudh
'''

import random as random

def main():
    d1 = 0
    d2 = 0
    d3 = 0
    n2 = 0
    n3 = 0
    list2D = []
    list3D = []
    size = 30
    list1D = generate1DList(size)
    for i in list1D:
        diff = 1
        for j in list1D:
            if j != i:
                curDiff = abs(j-i)
                if curDiff < diff:
                    diff = curDiff
        d1 = d1 + diff#abs(list1D[i] - list1D[(i+1)%len(list1D)])
    d1 = d1 / size
    print "d1"
    print d1
    
    while True:
        list2D = generate2DList(size)
        for i in list2D:
            diff = 1
            for j in list2D:
                if j != i:
                    curDiff = dist2D(i, j)
                    if curDiff < diff:
                        diff = curDiff
            d2 = d2 + diff#dist2D(list2D[i], list2D[(i+1)%len(list2D)])
        d2 = d2 / size
        n2 = n2 + 1
        if abs(d2-d1) < 0.001:
            break
    
    print "n2"
    print n2
    print "d2"
    print d2
    
    while True:
        list3D = generate3DList(size)
        for i in list3D:
            for j in list3D:
                if j != i:
                    curDiff = dist3D(i, j)
                    if curDiff < diff:
                        diff = curDiff
            d3 = d3 + diff#dist3D(list3D[i], list3D[(i+1)%len(list3D)])
        d3 = d3/size
        n3 = n3 + 1
        if abs(d3-d1)<0.001:
            break
    
    print "n3"
    print n3
    print "d3"
    print d3
    return

def generate1DList(size):
    list1D = []
    for i in range(30):
        list1D.append(random.random())
    return list1D
    
def generate2DList(size):
    list2D = []
    for i in range(size):
        list2D.append((random.random(), random.random()))
    return list2D
    
def generate3DList(size):
    list3D = []
    for i in range(size):
        list3D.append((random.random(), random.random(), random.random()))
    return list3D
    
def dist2D((x1,y1),(x2,y2)):
    distance = ((x2-x1)**2 + (y2-y1)**2) ** (0.5)
    return distance

def dist3D((x1, y1, z1),(x2, y2, z2)):
    distance = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) ** (0.5)
    return distance

if __name__ == '__main__':
    main()