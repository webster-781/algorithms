def check_random(f):
    sum=0
    for i in range(10000):
        sum+=f()
    return (1-sum/10000)
