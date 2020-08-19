#4.1-3
def diff_array(A):
    B= []
    for i in range(1,len(A)):
        B.append(A[i]-A[i-1])
    return B

def max_sub_array(A):
    D = diff_array(A)
    front,last = 0,0
    s=0
    max_sum=s
    max_f,max_l=0,0
    for i in range(len(D)):
        s+=D[i]
        if(s<=0):
            s=0
            front=i+1
            last=i
        else:
            last+=1
        if(max_sum<s):
            max_f=front
            max_l=last
            max_sum=s

    return(max_f,max_l+1,(max_sum))

