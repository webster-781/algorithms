#7_4
def partition(A,p,r):
    x=A[r]
    i,q=p,p-1
    while(i<r):
        if(A[i]<=x):
            A[q+1],A[i]= A[i],A[q+1]
            q+=1
        i+=1
    A[r],A[q+1] = A[q+1],A[r]
    return q+1

def tail_recursive_quicksort(A,p,r):
    # assert: array A[p..r].
    i=p
    while(i<r):
        # INV: A[p..i] has been sorted
        q = partition(A,i,r)
        # assert: A[i..q-1]<=A[q]<=A[i+1..r].
        tail_recursive_quicksort(A,i,q-1)
        # assert: A[i..q] has been sorted.
        i=q+1
    return A
