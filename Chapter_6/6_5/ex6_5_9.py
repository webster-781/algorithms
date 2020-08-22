from min_priority_queues import heap_extract_min as e
from min_heap_sort import *
def k_way_merging1(A,n):
    #Assertion : A is a two dimensional list with each row a sorted list and total k rows and total number of elements =n
    k = len(A)
    B = []
    for i in range(n):                                  #Θ(sigma(k*lg(n-i)))
        minval,minindex = float('inf'),-1
        for j in range(k):                              #Θ(k)
            
            if(len(A[j])>0 and A[j][0]<minval):
                minval = A[j][0]
                minindex = j

        B.append(minval)
        A[minindex],_ = e(A[minindex])                  #O(lg(n-i))

    #Output: A sorted list of all n elements in A
    return B

#Now this comes out to be Θ(k*lg(n!)) = Θ(k*n*lg(n)), which is Ω(n*lg(k)).Thus this solution is not efficient enough.



#This is the second and more efficient approach.

def k_way_merging(A,n):
    k = len(A)
    A = [[[A[i][j],i] for j in range(len(A[i]))]for i in range(k)]              #--O(n)
        #Now every element in A also contains its key and the index of its array in A
    B = [A[j][0] for j in range(k)]
        #Same in B
    B = build_min_heap(B)                                                       #--O(k)
    C = []
    for i in range(n):                                                          #--O(n*lg(k))

        #Since B is a min-heap of the smallest elements in each list of A, the root of B is the current smallest element left in A, we remove this element from A[index] as well
        C.append(B[0][0])
        index = B[0][1]
        del A[index][0]

        #Case 1: B[0] was the last element left in A, thus A is now empty, so we decrease size of B
        if(len(A[index])==0):
            B[0],B[-1] = B[-1],B[0]
            del B[-1]

        #Case 2: Else, we put the new smallest element in A at the root of B
        else:
            B[0] = A[index][0]

        #Now, we rebuild the new heap B 
        min_heapify(B,1)                                                        #--O(lg(k))
    return C

#This algorithm takes O(n*lg(k)) which is faster than previous one.
