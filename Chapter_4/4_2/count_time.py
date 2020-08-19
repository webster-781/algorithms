from matrix_mult_R import matrix_mult as m1
from matrix_mult_Strassen import matrix_mult as m2
from gen_matrix import gen_matrix as g
import time

for i in range(10):
    x= pow(2,i)
    print(x, end = ': ')
    A= g(x,x)
    B= g(x,x)
    start = time.time()
    m1(A,B)
    end = time.time()
    t1 = (end-start)*100000
    start = time.time()
    m2(A,B)
    end = time.time()
    t2 = (end-start)*100000
    print(t1,t2)
