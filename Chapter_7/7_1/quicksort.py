def quicksort(A,p,r):                           # sort a list A[p..r]
    if(p>=r):
        return A
    else:
        q,A = partition(A,p,r)
        A = quicksort(A,p,q-1)
        A = quicksort(A,q+1,r)
        return A

def partition(A,p,r):                           # partitions A[p..r] into A[p..q], A[q], A[q+1..r] such that A[p..q-1]<=A[q]<=A[q+1..r]
                                                # Θ(n)
    x = A[r]
    i = p-1
    for j in range(p,r):                        # Θ(n)
        if(A[j]<=x):
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1,A
