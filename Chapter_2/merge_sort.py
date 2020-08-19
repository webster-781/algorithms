#Section - 2.3.1

def merge(A,p,q,r):
    assert (p<=q<r)
    
    #A[p...q] and A[q+1...r] are sorted
    L,R=[],[]
    for i in range(p,q+1):
        L.append(A[i])
    L.append(max(A)+1)
    for i in range(q+1,r+1):
        R.append(A[i])
    R.append(max(A)+1)
    j,k=0,0
    for i in range(p,r+1):
        #Invariant : A[p...i-1] has been sorted with A[p...i-1] <= A[i...r]
        
        if(L[j]<R[k]):
            A[i] = L[j]
            j+=1
            
        else:
            A[i]=R[k]
            k+=1
    return 

def count_inversions(A,f,l):
    if(f==l):
        return (A)
    else:
        x =int((f+l)/2)
        A = merge_sort(A,f,x)
        A = merge_sort(A,x+1,l)
        return merge(A,f,x,l)
