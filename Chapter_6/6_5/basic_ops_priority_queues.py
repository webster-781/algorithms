def max_heapify(A,i):
    n=len(A)
    if(i>int(n/2)):
        return A
    else:
        largest = i
        left=2*i
        right=left+1
        if(A[left-1]>=A[largest-1]):
            largest =left
        elif(right<=n and A[right]>=A[largest]):
            largest = right
        else:
            return A
        A[largest-1],A[i-1] = A[i-1],A[largest-1]
        return max_heapify(A,largest)

def maximum(A):
    return A[0]

def extract_maximum(A):
    maxval = A[0]
    A[-1],A[0] = A[0],A[-1]
    del A[-1]
    A = max_heapify(A,1)
    return maxval,A

def insert(A,x):
    minval = min(A)-1
    A.append(minval)
    n = len(A)
    return increase_key(A,n,x)

def increase_key(A,i,k):
    assert A[i-1] <= k
    A[i-1] = k
    while(i>1):
        parent = int(i/2)
        if(A[parent-1]<=A[i-1]):
            A[parent-1],A[i-1] = A[i-1],A[parent-1]
        else:
            break
        i = parent
    return A
