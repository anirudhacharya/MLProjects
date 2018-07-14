'''
Created on Jan 29, 2014

@author: Anirudh
'''
import abc
from collections import namedtuple

class Node:
    def __init__(self,info):
        self.info=info
        self.right=None
        self.left=None
    
    def getInfo(self):
        return self.info

class BSTree:
    __metaclass__= abc.ABCMeta
    #Node = namedtuple("info", "Node", "Node")
    
    def __init__(self, ):
        self.root = None
        
    def create(self,info):
        return Node(info)
    
    def addNode(self,node):
        if self.root==None:
            self.root=node
        else:
            current=self.root
            while True:
                if node.info <= current.info:
                    if current.left==None:
                        current.left=node
                        return
                    else:
                        current=current.left
                        continue
                else:
                    if current.right==None:
                        current.right=node
                        return
                    else:
                        current=current.right
                        continue
    
    def getNode(self,value):
        current=self.root
        while True:
            if current==None:
                return None
            elif value==current.info:
                return current
            elif value<current.info:
                current=current.left
                continue
            elif value>current.info:
                current=current.right
                continue 
    
    def depth(self,root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            return max(self.depth(root.left),self.depth(root.right))+1
    
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print node.info
            self.inorder(node.right)
 
    def preorder(self,node):
        if node is not None:
            print node.info
            self.preorder(node.left)
            self.preorder(node.right)
 
    def postorder(self,node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.info