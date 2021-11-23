import numpy as np

ws = 6.68
constant = 1.12


a = 2
b = ws * constant
x_min = 1
x_max = 30

e = np.exp(1)

val = 0
for i in range(x_min, x_max):
    cumulative = (1-e**-(i/b)**a)
    print(cumulative-val)
    val = cumulative

