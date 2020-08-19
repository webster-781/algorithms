#2.3-2
def merge(A,p,q,r):
    assert p<=q<r
    L=A[p:q+1]
    R=A[q+1:r+1]
    #for i in range(p,q+1):
    #    L.append(A[i])
    #for i in range(q+1,r+1):
    #    R.append(A[i])
    i,j=0,0
    for k in range(p,r+1):
        if(i==len(L)):
            A[k] = R[j]
            j+=1
        elif(j==len(R)):
            A[k] = L[i]
            i+=1
        elif(R[j]<L[i]):
            A[k] = R[j]
            j+=1
        else:
            A[k] = L[i]
            i+=1
    return A

def merge_sort(A,f,l):
    print(A,f,l)
    if(f<l):
        A = merge_sort(A,f,int((f+l)/2))
        A = merge_sort(A,int((f+l)/2)+1,l)
        A = merge(A,f,int((f+l)/2),l)
    return A
