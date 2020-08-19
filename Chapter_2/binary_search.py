#2.3-5

#recursive
def binary_search_r(A,f,l,v):
    # Input: a sorted array A of size n, 2 values f,l representing the first and last indices of A
    #        to be searched in and a value v to be searched for
    mid = int((f+l)/2)
    if(A[mid]==v):
        return mid
    elif(f==l):
        return -1
    elif(A[mid]<v):
        return binary_search(A,mid+1,l,v)
    elif(A[mid]>v):
        return binary_search(A,f,mid-1,v)
    # Output: The index at which the element exists or -1 if it doesn't exist in the array. 


#iterative
def binary_search_i(A,v):
    f,l = 0,len(A)-1
    while(True):
        mid = int((f+l)/2)
        if(A[mid]==v):
            return mid
        elif(f==l):
            return -1
        elif(A[mid]>v):
            l=mid-1
        else:
            f=mid+1


# Since the binary search checks by extending outwards from the middle, 
# the worst case scenario is when the element is either not in the array or on either end of the array.
# So, the recurrence equation is T(n)   =   T(n/2)                  +                    c
#                                   The next search for (n/2) elements      Constant times (c1+c2+c3+c4)
#                               So, we can see that T = c*log(n)
# Therefore, the order of growth of such algorithm is  O(log(n))
