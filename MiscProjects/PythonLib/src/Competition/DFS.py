'''
Created on Dec 31, 2016

@author: aachy
'''
def dfs(node, graph):
    V = len(graph)
    d = [-1]*V
    f = [-1]*V
    pred = [None]*V
    path = {}
    stack = []
    color = ['white']*V
    time=0
    
    stack.append(node)
        
    while len(stack) > 0:
        curNode = stack.pop()
        if color[curNode]=='white':
            color[curNode] = 'gray'
            time += 1
            d[curNode] = time
            path[curNode] = [curNode]
            stack.append(curNode)
            continue
        elif color[curNode]=='gray':
            nbrs = graph[curNode]
            stack.append(curNode)
            flag = True
            for i in nbrs:
                if color[i] is 'white':
                    stack.append(i)
                    pred[i]=curNode
                    path[i] = path[curNode] + [i]
                    flag = False
            if flag:
                stack.pop()
                color[curNode]='black'
                time += 1
                f[curNode]=time

        if len(stack)==0:
            for i in range(V):
                if color[i] == 'white':
                    stack.append(i)
                    break
        
    return d,f,pred,path
    
def main():
    graph = [[2,3],[3],[1,5,8],[4],[],[6],[7],[8],[]]
    #graph = [[1,2],[3,4],[5,6],[7,8],[9,10],[],[],[],[],[],[]]
    graph = [[2,1],[3],[1],[2],[3,5],[5]]
    d,f,pred,path = dfs(0,graph)
    for i in range(len(graph)):
        print str(i)+"\t"+ str(pred[i])+"\t"+str(d[i])+"\t"+str(f[i])
            
if __name__=='__main__':
    main()