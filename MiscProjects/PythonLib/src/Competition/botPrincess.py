'''
Created on Jun 10, 2014

@author: Anirudh
'''
#!/bin/python
def find(mat, elem):
    for row, i in enumerate(mat):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1

def displayPathtoPrincess(n,grid):
    bot_pos = find(grid,'m')
    p_pos = find(grid,'p')
    y_diff = p_pos[0] - bot_pos[0]
    x_diff = p_pos[1] - bot_pos[1]
    for i in range(abs(y_diff)):
        if y_diff < 0:
            print "UP"
        else:
            print "DOWN"
            
    for i in range(abs(x_diff)):
        if x_diff < 0:
            print "LEFT"
        else:
            print "RIGHT"
    return

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)