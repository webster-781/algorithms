#7_2
def new_partition(A,p,r):
    # assert: A[p..r] is an array
    x= A[r]
    i,q,t=p,p,p-1
    while(i<=r):
        # INV: A[p..q-1]<x, A[q..t]=x, A[t+1..i-1]>x for p<=i<=r
        if(A[i]==x):
            A[i],A[t+1] = A[t+1],A[i]
            t+=1
        elif(A[i]<x):
            A[i],A[t+1] = A[t+1],A[i]
            A[q],A[t+1] = A[t+1],A[q]
            q+=1
            t+=1
        i+=1
    # assert: A[p..q-1]<x, A[q..t]=x, A[t+1..r]>x at termination
    return q,t

def quicksort(A,p,r):
    if(p>=r):
        return A
    else:
        q,t = new_partition(A,p,r)
        A = quicksort(A,p,q-1)
        A = quicksort(A,t+1,r)
        return A
