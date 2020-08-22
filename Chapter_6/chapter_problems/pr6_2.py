# All functions are based on d-ary heaps with argument d as in d-a

from numpy import *

def logbase(d,x):                                               #returns log of x to base d
    return log(x)/log(d)

def level(i,d):                                                 #returns the level from the top: root is 0 and increasing downwards
    x = logbase(d,(d-1)*(i-1)+1)
    y = int(x)
    return y

def parent(i,d):                                                #returns the index of the parent of the node at index i
    return int((i+1)/d)

def child(i,j,d):                                               #returns the index of the jth child of node i
    return (i*d-1) +(j-1)

def children(i,d):                                              #returns all the children of the node i
    return [i*d-1+ j for j in range(d)]

def max_heapify(A,i,d):                                         #max_heapifies subtree at node i assuming that all its children subtrees are already max heaps
                                                                #--O(logbase(d,i))
    n= len(A)
    if(i>int(n/d)):
        return A
    else:
        largest = i
        j=0
        for j in children(i,d):
            if(j>n):
                break
            if(A[j-1]>=A[largest-1]):
                largest = j
        if(largest==i):
            return A
        A[largest-1],A[i-1]=A[i-1],A[largest-1]
        return max_heapify(A,largest,d)

def extract_max(A,d):                                           #extracts the max node(root element) and also returns a new Max Heap with one less element
                                                                #O(lg(n))
    maxval = A[0]
    A[0],A[-1] = A[-1],A[0]
    del A[-1]
    return maxval,max_heapify(A,1,d)

def build_max_heap(A,d):                                        #builds a max heap of an unordered array/heap
                                                                #O(n)
    for i in range(int(n/d),0,-1):
        A = max_heapify(A,i,d)
    return A

def increase_key(A,i,x,d):                                      #Increases the value of the key at node i to x
                                                                #O(lg(i))
    if(i==1):
        return A
    p = parent(i,d)
    if(A[p-1]<=x):
        A[i-1] = A[p-1]
        return increase_key(A,p,x,d)
    else:
        A[i-1] = x
        return A


def insert(A,x):                                                #Inserts a new element and returns the max heap
                                                                #O(lg(n))
    A.append(float('-inf'))
    return increase_key(A,len(A),x,d)
