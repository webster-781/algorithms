#7_1
def hoare_partition(A,p,r):
    x=A[p]
    i=p
    j=r
    # assert: A[p..r] is an array
    while(True):

    # INV: A[p..i-1]<= x <= A[j+1...r]
        while(A[j]>x):
            j=j-1
        while(A[i]<x):
            i=i+1
        if(i<j):
            A[i],A[j] = A[j],A[i]
        else:
            return j
    # assert: i=j implies A[p..j-1]<=x<=A[j+1..r] => A[j] = x. A[p..r] has been partitioned about index j
     
def quicksort(A,p,r):
    if(r<=p):
        return A
    q = hoare_partition(A,p,r)
    A = quicksort(A,p,q)
    A = quicksort(A,q+1,r)
    return A
