# this file is for functions
from numpy.random import randint
import numpy as np


# average function
def average(lst):
    return sum(lst) / len(lst)


# Random generation of x numbers
def ran_gen_uni(lower_limit, upper_limit, size):
    x = np.random.uniform(int(lower_limit), int(upper_limit), int(size))
    return list(x)

print(ran_gen_uni(lower_limit=5, upper_limit=9, size=41))


def ran_gen_float(lower_limit, upper_limit, size):
    x = np.random.uniform(lower_limit, upper_limit, int(size))
    return list(x)

print(ran_gen_float(lower_limit=5, upper_limit=9, size=41))


def ran_int(lower_limit, upper_limit, size):
    return list(randint(lower_limit, upper_limit + 1, size))

print(np.linspace(start=5,
               stop=9,
               num = 41,
               endpoint = True,
               retstep = False,
               dtype = None))
