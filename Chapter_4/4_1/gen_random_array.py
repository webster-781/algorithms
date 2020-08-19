import random 
def gen_random_array(n):
    A = []
    for i in range(n):
        A.append(random.randrange(-10000,10000))
    return A
