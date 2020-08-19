#4.1
def max_cross_sub_array(A,low,mid,high):
    max_left,min_i=mid,mid
    s=0
    for i in range(mid,low-1,-1):
        s+=A[i]
        if(max_left<=s):
            max_left=s
            min_i=i
    max_right=0
    max_j=mid+1
    s=0
    for j in range(mid+1,high+1):
        s+=A[j]
        if(max_right<=s):
            max_right=s
            max_j=j
    return(max_left+max_right, min_i, max_j)


def max_sub_array(A,low,high):
    if(low==high):
        return(A[low],low,high)
    else:
        mid = int((low+high)/2)
        left_sum,left_low,left_high = max_sub_array(A,low,mid)
        right_sum,right_low,right_high = max_sub_array(A,mid+1,high)
        cross_sum,cross_low,cross_high = max_cross_sub_array(A,low,mid,high)
        if(cross_sum>=left_sum and cross_sum>=right_sum):
            return(cross_sum,cross_low,cross_high)
        elif(left_sum>=right_sum):
            return(left_sum,left_low,left_high)
        return(right_sum,right_low,right_high)
