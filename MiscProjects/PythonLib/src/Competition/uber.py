'''
Created on Aug 15, 2017

@author: aachy
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
graph = {}
for i in range(N):
    graph[i+1] = []

i = 1    
while i<=N:
    l = [int(x) for x in raw_input().split(' ')]
    l = l[1:]
    for j in l:
        graph[j].append(i)
        
    i += 1

def trav(k):
    reach = 0
    toTrav = [k]
    visited = {}
    while len(toTrav) > 0:
        curNode = toTrav.pop()
        if curNode not in visited:
            reach += 1
            visited[curNode] = 1
            for m in graph[curNode]:
                if m not in visited:
                    toTrav.append(m)
    return reach
            
        
count = 0
for i in graph:
    if trav(i)==len(graph):
        count += 1

print count