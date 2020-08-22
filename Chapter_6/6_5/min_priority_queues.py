def min_heapify(A,i):
    n = len(A)
    if(i>int(n/2)):
        return A
    else:
        smallest = i
        left = 2*i
        right = 2*i+1
        if(A[left-1]<=A[smallest-1]):
            smallest = left
        elif(right<=n and A[right-1]<=A[smallest-1]):
            smallest = right
        else:
            return A
        A[smallest-1],A[i-1] = A[i-1],A[smallest-1]
        return min_heapify(A,smallest)

def heap_minimum(A):
    return A[0]

def heap_extract_min(A):
    minval = A[0]
    A[0],A[-1]=A[-1],A[0]
    del A[-1]
    A = min_heapify(A,1)
    return A, minval

def heap_decrease_key(A,i,k):
    assert A[i-1]>=k
    while(i>1 and A[int(i/2)-1]>k):
        A[i-1] = A[int(i/2)-1]
        i = int(i/2)
    A[i-1] = k
    return A

def min_heap_insert(A,x):
    A.append(max(A)+1)
    A = heap_decrease_key(A,len(A),x)
    return A


