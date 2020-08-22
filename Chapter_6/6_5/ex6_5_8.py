from basic_ops_priority_queues import max_heapify 
def heap_delete(A,i):
    A[i-1],A[-1] = A[-1],A[i-1]
    del A[-1]
    if(len(A)>i):
        A = max_heapify(A,i)
    return A 
