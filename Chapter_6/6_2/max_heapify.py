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

def max_heapify_i(A,i):
    while(i<=int(len(A)/2)):
        left = 2*i
        right = left+1
        largest = i
        if(left<=len(A)):
            if(A[left-1]>A[largest-1]):
                largest = left
        if(right<=len(A)):
            if(A[right-1]>A[largest-1]):
                largest = right
        if(largest==i):
            break
        else:
            A[largest-1],A[i-1]= A[i-1],A[largest-1]
            i=largest
        #print(A)
    return A

