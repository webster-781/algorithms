import random
def done(B):
    ans = True
    for i in B:
        if(ans==False):
            return ans
        ans = ans and i
    return ans

def random_search(A,v):
    n= len(A)
    B = [False for _ in range(n)]
    while(not done(B)):
        t = random.randrange(len(A))
        if(A[t]==v):
            return t
        else:
            B[t] = True
    return -1
