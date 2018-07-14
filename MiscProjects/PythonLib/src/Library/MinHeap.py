'''
Created on Dec 28, 2016

@author: aachy
'''
class MinHeap(object):
    """docstring for BinHeap"""
    def __init__(self):
        super(MinHeap, self).__init__()
        self.self = self
        self.heap = [0]
        
    def insert(self,data):
        self.heap.append(data)
        self.percolateUp()

    def delete(self):
        retVal = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolateDown()
        return retVal

    def percolateUp(self):
        i = len(self.heap) - 1
        while i>1:
            if self.heap[i] < self.heap[i/2]:
                self.heap[i], self.heap[i/2] = self.heap[i/2], self.heap[i]
                i = i/2
            else:
                return

    def percolateDown(self):
        i = 1
        while 2*i<len(self.heap):
            if self.heap[i] > self.heap[2*i]:
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i
            elif self.heap[i] > self.heap[2*i + 1]:
                self.heap[i], self.heap[2*i + 1] = self.heap[2*i + 1], self.heap[i]
                i = 2*i + 1
            else:
                return
            
minHeap = MinHeap()
minHeap.insert(6)
minHeap.insert(13)
minHeap.insert(1)
minHeap.insert(65)
minHeap.insert(11)
minHeap.insert(45)
minHeap.insert(42)
minHeap.insert(33)
minHeap.insert(31)
minHeap.insert(26)
minHeap.insert(21)
minHeap.insert(25)
minHeap.insert(18)
print minHeap.delete()
print minHeap.heap