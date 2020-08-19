def matrix_add(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def comb_matrix(C11,C12,C21,C22):
    n = len(C11)
    C = [[0 for i in range(n*2)] for i in range(n*2)]
    for i in range(n):
        for j in range(n):
            C[i][j] =C11[i][j]
    for i in range(n):
        for j in range(n,2*n):
            C[i][j] =C12[i][j-n]
    for i in range(n,2*n):
        for j in range(n):
            C[i][j] =C21[i-n][j]
    for i in range(n,2*n):
        for j in range(n,2*n):
            C[i][j] =C22[i-n][j-n]
    return C

def div_matrix(A):
    n = int(len(A)/2)
    A11 = [[0 for i in range(n)]for i in range(n)]
    A12 = [[0 for i in range(n)]for i in range(n)]
    A21 = [[0 for i in range(n)]for i in range(n)]
    A22 = [[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            A11[i][j] = A[i][j]
    for i in range(n):
        for j in range(n):
            A12[i][j] = A[i][j+n]
    for i in range(n):
        for j in range(n):
            A21[i][j] = A[i+n][j]
    for i in range(n):
        for j in range(n):
            A22[i][j] = A[i+n][j+n]
    return A11,A12,A21,A22


def matrix_mult(A,B):
    n = len(A)
    if(n==1):
        return [[A[0][0]*B[0][0]]]

    A11,A12,A21,A22 = div_matrix(A)
    B11,B12,B21,B22 = div_matrix(B)

    C11  =  matrix_add(matrix_mult(A11,B11), matrix_mult(A12,B21))
    C12  =  matrix_add(matrix_mult(A11,B12), matrix_mult(A12,B22))
    C21  =  matrix_add(matrix_mult(A21,B11), matrix_mult(A22,B21))
    C22  =  matrix_add(matrix_mult(A21,B12), matrix_mult(A22,B22))
    C = comb_matrix(C11,C12,C21,C22)
    return C
