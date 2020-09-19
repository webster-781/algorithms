#7-6 Fuzzy Sorting of Intervals
from random import randrange as rand

def partition(A,p,r):
    q,t=p,p-1
    x = A[r]
    # assert: A[p..r] is an array of intervals in no particular order
    for i in range(p,r+1):
        # INV: A[p..q-1] < A[q..t] < A[t+1..i-1] where '<' sign represents that there exists no pair of values of c1,c2 s.t c1 >= c2 where c1 ∈  LHS and c2 ∈  RHS. Also A[q..t] intervals all overlap with x.
        
        if(A[i][1]<x[0]):
            # assert: the interval A[i] has no overlap with x and is A[i] < x
            A[i],A[t+1]=A[t+1],A[i]
            A[q],A[t+1]=A[t+1],A[q]
            t+=1
            q+=1

        elif(A[i][1]>=x[0] and x[1]>=A[i][0]):
            # assert: the interval A[i] overlaps with x
            A[i],A[t+1]=A[t+1],A[i]
            t+=1

    # assert: A[p..q-1] < A[q..t] < A[t+1..r]. A[q..t] intervals all ovelap.
    return q,t

def randomized_partition(A,p,r):
    for i in range(p,r+1):
        random = rand(p,r+1)
        A[random],A[i] = A[i],A[random]
    return partition(A,p,r)

def fuzzy_sort(A,p,r):
    # assert: A[p..r] is a list of intervals(as tuples)
    if(p<r):
            q,t = randomized_partition(A,p,r)
            # assert: A[p..q-1] < A[q..t] < A[t+1..r]. A[q..t] intervals all ovelap.
            A = fuzzy_sort(A,p,q-1)
            A = fuzzy_sort(A,t+1,r)
    # assert: A has been fuzzy-sorted.
    return A

def check(x,y): #auxillary function used while creating random interval arrays
    if(x>y):
        x,y=y,x
    return (x,y)
