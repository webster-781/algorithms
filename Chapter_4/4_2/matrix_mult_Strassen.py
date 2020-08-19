def matrix_add(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrix_sub(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
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
    else:
        A11,A12,A21,A22 = div_matrix(A)
        B11,B12,B21,B22 = div_matrix(B)

        S1 = matrix_sub(B12,B22)
        S2 = matrix_add(A11,A12)
        S3 = matrix_add(A21,A22)
        S4 = matrix_sub(B21,B11)
        S5 = matrix_add(A11,A22)
        S6 = matrix_add(B11,B22)
        S7 = matrix_sub(A12,A22)
        S8 = matrix_add(B21,B22)
        S9 = matrix_sub(A11,A21)
        S10 = matrix_add(B11,B12)

        P1 = matrix_mult(A11,S1)
        P2 = matrix_mult(S2,B22)
        P3 = matrix_mult(S3,B11)
        P4 = matrix_mult(A22,S4)
        P5 = matrix_mult(S5,S6)
        P6 = matrix_mult(S7,S8)
        P7 = matrix_mult(S9,S10)

        C11 = matrix_add(matrix_add(P5,P4),matrix_sub(P6,P2))
        C12 = matrix_add(P1,P2)
        C21 = matrix_add(P3,P4)
        C22 = matrix_sub(matrix_add(P5,P1),matrix_add(P3,P7))

        return(comb_matrix(C11,C12,C21,C22))
