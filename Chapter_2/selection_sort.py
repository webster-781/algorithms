#2.2-2

def selection_sort(A):
    # An array A[0...n-1]
    n= len(A)                                                                               # 1

    for i in range(n-1):                                                                    # n-1

        #Invariant : A[0...i-1] is sorted such that all A[0...i-1]<=A[i...n-1]              # 0
        
        for j in range(i+1,n):                                                              # (n-2)(Sigma(tj))
            
            if(A[j]<A[i]):                                                                  # (n-2)(Sigma(tj-1))
                A[j],A[i] = A[i],A[j]                                                       # (n-2)(Sigma(tj-1))
    
    return A                                                                                # 1


# We only need to iterate over n-1  steps becuase at i =n-1, the invariant says
# A[0...n-2] is sorted A[0...n-2] <= A[n-1...n-1] = A[n-1], thus All A is already sorted. 

# Best Case :  O(n^2)
# Worst Case : O(n^2)

# Case doesn't matter because it tests all possible values for the smallest number.
