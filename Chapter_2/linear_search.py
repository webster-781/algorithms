#2.1-3
def linear_search(A,v):
    #An array A[0....n-1]
    x=-1
    for i in range(len(A)):
        #Invariant : If v exists in A[0...i-1] at latest index r then x=r otherwise x=-1
        if(A[i]==v):
            x=i
    return x
    #A value x such that A[x] = v or -1 if no such x exists.


# Initialization : For case i=0, there is no element in A[0..-1], so x=-1

# Maintainence : Suppose the invariant is satisfied for i-1 then for i, if A[i]=v then x=i
# otherwise the latest index containing v is the previously saved value of x

# Termination: Now at the final value of i=n, loop terminates and thus the value of x is 
# the latest index at which v is found in A[0...n-1] which is the whole array!
