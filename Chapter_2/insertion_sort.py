#2.1-2
def insertion_sort(A):
    for j in range(1,len(A)):
        t, i=A[j],j-1
        while(i>=0 and A[i]<t):
            A[i+1]=A[i]
            i-=1
        A[i+1]=t
    return A
