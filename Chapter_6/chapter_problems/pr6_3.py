# A young tableau(m,n) is represented here as a 2D list. m is number of rows and n is number of columns


from numpy import *
def young_tableaufy(A,i,j):                     # Returns a young tableau while assuming that the input matrix is young tableau for both A[i+1....][j.....] and A[i....][j+1....]
                                                # T(m,n) = T(m-1,n) + c or T(m,n-1) + c   --> O(m+n)
    (li,lj) = (i,j)
    m = len(A)
    n = len(A[0])
    if(i>=m and j>=n):
        return A
    elif(i>=m):
        if(A[i-1][j]<=A[li-1][lj-1]):
            (li,lj) = (i,j+1)
    elif(j>=n):
        if(A[i][j-1]<=A[li-1][lj-1]):
            (li,lj) = (i+1,j)
    else:
        if(A[i-1][j]<=A[li-1][lj-1]):
            (li,lj) = (i,j+1)
        if(A[i][j-1]<=A[li-1][lj-1]):
            (li,lj) = (i+1,j)
    #print(A,li,lj)
    if((li,lj)==(i,j)):
        return A
    A[i-1][j-1],A[li-1][lj-1] = A[li-1][lj-1],A[i-1][j-1]
    return young_tableaufy(A,li,lj)


def build_young_tableau(A):                     # Creates a young tableau of a matrix
                                                # O(m*n*(m+n))
    n= len(A)
    m = len(A[0])
    for i in range(n,0,-1):
        for j in range(m,0,-1):
            A = young_tableaufy(A,i,j)
    return A

def extract_min(A):                             # Returns the minimum element i.e. first element of matrix and returns a new young tableau of same size
                                                # O(m+n)
    minval = A[0][0]
    A[0][0]= A[-1][-1]
    A[-1][-1] = float('inf')
    young_tableaufy(A,1,1)
    return A, minval


def decrease_key(A,i,j,x):                      # Takes a node and decreases its value to a smaller number and returns the resulting young tableau
                                                # O(m+n)
    A[i-1][j-1] = x
    while(i>1 or j>1):
        #print(A,i,j)
        if(j>1 and A[i-1][j-2]>=x):
                A[i-1][j-2],A[i-1][j-1] = A[i-1][j-1],A[i-1][j-2]
                j-=1
        elif(i>1 and A[i-2][j-1]>=x):
                A[i-2][j-1],A[i-1][j-1] = A[i-1][j-1],A[i-2][j-1]
                i-=1
        else:
           break
    return A


def insert(A,x):                                # Inserts a new value to an incomplete young tableau and returns a new young tableau
                                                # O(m+n)
    return decrease_key(A,len(A),len(A[0]),x)

def tableau_sort(A):                            # Takes a list of perfect square n. of elements and sorts it 
                                                # O(n*n*n) + (1->n^2)Sigma(2*n) --> O(n^3)
    B = []
    t = len(A)
    n = int(sqrt(t))
    A = [[A[i] for i in range(j*n,n*(j+1))] for j in range(n)]
    A = build_young_tableau(A)                  # O(n*n*(n+n))
    for i in range(n,0,-1):                     # O(n*n*n)
        for j in range(n,0,-1):                 # O(n*n)
            A,minval = extract_min(A)           # O(2*n)
            #print(A, minval)
            B.append(minval)
    return B

def stored(A,x):                                # Takes a young tableau and a number as input and determines whether or not the number exists in the tableau
                                                # T(p) = T(p-1) + O(1) where p = m+n --> O(m+n)
    m=len(A)
    n=len(A[0])
    i,j=m,1
    while(i>0 and j<=n):                        # O(m+n)
        current = A[i-1][j-1]
        if(current==x):
            return i,j
        elif(current<x):
            j+=1
        else:
            i-=1

    return False

def stored1(A,x):                               # Takes a young tableau and a number as input and determines whether or not the number exists in the tableau
                                                # O(m+n)
    m=len(A)
    n=len(A[0])
    flag,dist = False,100
    i,j= 1,1
    ni,nj=1,1
    newdist = float('inf')
    while(i<=m and j<=n):                       # O(m+n)
        if(newdist == 0 ):
            return True
        if(newdist == dist):
            return False
        dist = newdist
        i,j=ni,nj
        print(dist,i,j)
        ni,nj=i,j
        if(i<m):
            val = abs(x-A[i][j-1])
            if(val<=newdist):
                newdist = val
                ni=i+1

        if(i>1):
            val = abs(x-A[i-2][j-1])
            if(val<=newdist):
                newdist = val
                ni=i-1

        if(j>1):
            val = abs(x-A[i-1][j-2])
            if(val<=newdist):
                newdist = val
                ni=i
                nj=j-1

        if(j<n):
            val = abs(x-A[i-1][j])
            if(val<=newdist):
                newdist = val
                ni=i
                nj=j+1

    return False
