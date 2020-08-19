import random
def biased_random(p=0.8):
    t = random.randrange(0,1000)
    if(t<p*1000):
        return 0
    return 1
