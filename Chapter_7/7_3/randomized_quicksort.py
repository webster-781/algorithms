from random import randrange as rand
def partition(A,p,r):
    q=p-1
    x = A[r]
    for i in range(p,r):
        if(A[i]<=x):
            A[q+1],A[i]=A[i],A[q+1]
            q+=1
    A[q+1],A[r]=A[r],A[q+1]
    return q+1

def randomized_partition(A,p,r):
    for i in range(p,r+1):
        random = rand(p,r+1)
        A[random],A[i] = A[i],A[random]
    return partition(A,p,r)

def quicksort(A,p,r):
    if(p<r):
        q = randomized_partition(A,p,r)
        A = quicksort(A,p,q-1)
        A = quicksort(A,q+1,r)
    return A
