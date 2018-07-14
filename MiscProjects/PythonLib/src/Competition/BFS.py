'''
Created on Jan 3, 2017

@author: aachy
'''
import Queue as Q
def BFS(G,node):
    toTrav = Q.Queue()
    toTrav.put(node)
    parent = {}
    path = {}
    status = {}
    stamp = {}
    for i in range(len(G)):
        parent[i] = None
        path[i] = []
        status[i] = 'white'
    while not toTrav.empty():
        curNode = toTrav.get()
        if status[curNode] is 'white':
            status[curNode] = 'gray'
            parent[curNode] = None
            path[curNode] = [curNode]
            stamp[curNode] = 0
        nbrs = G[curNode]
        for i in nbrs:
            if status[i] is 'white':
                toTrav.put(i)
                status[i] = 'gray'
        status[curNode] = 'black'
        
        if toTrav.empty():
            for i in range(len(G)):
                if status[i] is 'white':
                    toTrav.put(i)
                    break
    
    return stamp,parent,path
def main():
    graph = [[2,3],[3],[1,5,8],[4],[],[6],[7],[8],[]]
    #graph = [[1,2],[3,4],[5,6],[7,8],[9,10],[],[],[],[],[],[]]
    graph = [[2,1],[3],[1],[2],[3,5],[5]]
    graph = [[1,2],[0,4],[0,3],[2],[1,5],[1,4,7],[4,7],[5,6]]
    stamp,parent,path = BFS(graph,0)
    for i in range(len(graph)):
        print str(i)+"\t"+ str(parent[i])+"\t"+str(stamp[i])
            
if __name__=='__main__':
    main()