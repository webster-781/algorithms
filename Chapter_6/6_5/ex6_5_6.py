def heap_increase_key(A,i,k):
    assert A[i-1]<=k
    while(i>1 and A[int(i/2)-1]<k):
        A[i-1] = A[int(i/2)-1]
        i = int(i/2)
    A[i-1] = k
    return A
