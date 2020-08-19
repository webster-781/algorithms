import random
def gen_matrix(m,n):
    A=[[0 for k in range(n)] for k in range(m)]
    for i in range(m):
        for j in range(n):
            A[i][j] = random.randrange(10)
    return A

