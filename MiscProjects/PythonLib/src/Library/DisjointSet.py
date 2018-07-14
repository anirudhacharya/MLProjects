'''
Created on Dec 10, 2014

@author: Anirudh
'''
class Node:
    def __init__(self,data, rep, next):
        self.data = data
        self.parent = rep
        self.next = next
        
class List:
    def __init__(self,head, tail,length):
        self.head = head
        self.tail = tail
        self.size = length
        
def make_set(x):
    newNode = Node(x, None, None)
    newList = List(newNode, newNode,1)
    return newList

def union(x1,x2):
    node = x2.head
    (x1.tail).next = node
    x1.tail = x2.tail
    while node!= None:
        node.parent = x1.head
        node = node.next
    #x2 = None
    return x1

def find(x, disSet):
    for i in disSet:
        node = i.head
        while node!=None:
            if node.data==x:
                return node.parent
            node = node.next
    return None

def printSet(disSet):
    for i in disSet:
        node = i.head
        str1 = ""
        while node!=None:
            str1 = str1 + " " + str(node.data)
            node = node.next
        print str1
  
def main():
    disSet = []
    for i in range(10):
        disSet.append(make_set(i))
    
    disSet[0] = union(disSet[0],disSet[1])
    disSet = disSet[:1] + disSet[2:]
    #printSet(disSet)
    disSet[1] = union(disSet[1],disSet[2])
    disSet = disSet[:2] + disSet[3:]
    #printSet(disSet)
    disSet[0] = union(disSet[0],disSet[2])
    disSet = disSet[:2] + disSet[3:]
    disSet[3] = union(disSet[3],disSet[6])
    disSet = disSet[:6] + disSet[7:]
    printSet(disSet)
    print (find(4,disSet)).data
        
if __name__=='__main__':
    main()