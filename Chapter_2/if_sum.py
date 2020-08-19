#2.3-7
from merge_sort import merge_sort, merge
from binary_search import binary_search_i

def if_sum(A,v):                                                    
    n = len(A)                                                              # c                                
    flag = False                                                            # c
    A = merge_sort(A,0,n-1)                                                 # O(n*lg(n))
    for i in range(n):                                                      # (0->(n)Sigma{c}) = O(n)
        x = v-A[i]                                                          # (0->(n-1)Sigma{c}) = O(n)
        if(binary_search_i(A[:i]+(A[i+1:]), x)!=-1):                        # (0->(n-1)Sigma{O(lg(n-1))}) = O(n*lg(n))
            flag=True                                                       # c
            return flag                                                     # c
    return flag                                                             # c

# Thus, the total worst-case running time comes out to be of O(n*lg(n)+(n*lg(n))) = O(n*lg(n))
