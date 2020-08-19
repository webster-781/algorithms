#5.1-3
from biased_random import biased_random as b
def unbiased_random():
    while(True):
        x=b()
        y=b()
        if(x!=y):
            return x
