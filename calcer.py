import numpy
import random

x = random.randint(1,1000)

def lottery(man,machine):
    if man == machine:
        return True
    else:
        return False