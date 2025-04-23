import numpy
import random

winner = random.uniform(0,1000)

def lottery(user,machine):
    if user == machine:
        return True
    else:
        False
