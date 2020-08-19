#2.1-4
def add_binary_integers(A,B):
    assert (len(A)==len(B))
    C,rem=[],0
    
    for i in range (len(A)+1):
        C.append(0)
    i=len(A)-1
    # Two n(=len(A)=len(B)) bit binary integers , C= n+1 bit binary integer which is 0 initially
    while (i>=0):
        # Invariant : rem::C[i...n] = A[i-1...n-1]+B[i-1...n-1]
        val = A[i]+B[i]+rem
        C[i+1] = val%2
        rem = int(val/2)
        i-=1
    C[0]=rem
    
    return C

# Initailization : For i=n, A[n-2...n-1] + B[n-2...n-1] = 0::C[n-1...n] => 0+0 =0 which is true

# Maintainence : Cases- 1+1+(rem=1) = 11, 1+1+(rem=0)=10, 1+0+(rem=1)=10, 1+0+(rem=0)=1, 0+0+(rem=0)=0, 0+0+(rem=1)=1
# So obviously, x1 + x2 + rem = (x1+x2+rem)/2::(x1+x2+rem)%2
# Now if, A' + B' = rem::C', then  x1::A' + x2::B' = (x1+x2+rem)/2::(x1+x2+rem)%2::C'.

# Termination : At the value i = -1 , rem::C[1...n] =  A[0...n-1] + B[0...n-1],
# but since C[0]=rem=> C[0...n] = A[0...n-1] + B[0...n-1]
# Simply put, C = A + B, which is what we need.
