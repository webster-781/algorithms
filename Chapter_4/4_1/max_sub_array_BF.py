#4.1-3
def max_sub_array(A):
    max_sum,max_i,max_j=0,-1,-1
    for i in range(len(A)):
        s=0
        for j in range(i,len(A)):
            s+=A[j]
            if(s>max_sum):
                max_sum=s
                max_i=i
                max_j=j

    return(max_sum,max_i,max_j)
