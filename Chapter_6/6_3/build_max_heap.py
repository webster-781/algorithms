from numpy import *
def build_max_heap(A):
    n = len(A)
    for i in range(int(n/2)+1,0,-1):
        print(A)
        max_heapify(A,i)
    return A

def max_heapify(A,i):
    n=len(A)
    if(i>int(n/2)):
        return A
    l=2*i
    r=l+1
    largest =i
    #print(A,n,A[i-1],A[l-1],A[r-1],end= ' ')
    if(l<=n):
        if(A[largest-1]<A[l-1]):
            largest= l
            #print('l')
    if(r<=n):
        if(A[largest-1]<A[r-1]):
            largest= r
            #print('r')

    #print(f'largest = {A[largest-1]}')
    if(largest==i):
        #print('No Change')
        return A
    else:
        A[i-1],A[largest-1] = A[largest-1],A[i-1]
        #print(f'Max-Heapify(A[{largest}] = {A[largest]})')
    return max_heapify(A,largest)

