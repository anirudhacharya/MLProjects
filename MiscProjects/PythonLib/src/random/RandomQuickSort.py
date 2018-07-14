'''
Created on Sep 14, 2013

@author: Anirudh
'''
def quicksort(A,first,last):
    print A[first:last]
    if first<last:
        pivot = partition(A,first,last)
        quicksort(A, first, pivot-1)
        quicksort(A,pivot+1,last)
    return

def partition(A,first,last):
    randomElem = A[last]
    i = first-1
    for j in range(len(A))[first:last]:
        if A[j]<randomElem:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[last],A[i+1]=A[i+1],A[last]
    return i+1

if __name__ == "__main__":
    A = [48,26,33,56,81,4,9,10,56,65,3]
    #A = [2,2,2,2,2,2,2]
    quicksort(A,0,len(A)-1)
    print A
