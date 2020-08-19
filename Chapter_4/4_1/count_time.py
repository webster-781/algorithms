import time
from gen_random_array import gen_random_array
from max_sub_array_DnC import max_sub_array as f1
from max_sub_array_BF import max_sub_array as f2
from max_sub_array_DnC_BF import max_sub_array as f3
from pandas import DataFrame
import matplotlib.pyplot as plt

index,t1,t2,t3 = [],[],[],[]
for i in range(1,1001,100):
    index.append(i)
    #print(i, end=': ')
    A = gen_random_array(i)
    start = time.time()
    f1(A,0,i-1)
    end = time.time()
    t1.append(int((end-start)*10000000))
    #print(f'{t1}', end=' ')
    start = time.time()
    f2(A)
    end = time.time()
    t2.append(int((end-start)*10000000))
    #print(f'{t2}', end='  ')
    start = time.time()
    f3(A,0,i-1)
    end = time.time()
    t3.append(int((end-start)*10000000))
    #print(f'{t3}')

Data = {'Size' : index, 'Recursive' : t1, 'Brute Force' : t2, 'Mixed' : t3}
df = DataFrame(Data, columns = ['Size', 'Recursive', 'Brute Force', 'Mixed'])
df.plot(x ='Size', y=['Mixed', 'Recursive', 'Brute Force'], kind = 'line')
plt.show()
