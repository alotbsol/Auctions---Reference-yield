import numpy as np

ws = 6.68
constant = 1.12


a = 2
b = ws * constant
x = 1

e = np.exp(1)

print(e)
print(b)

print(a/b * (x/b)**(a-1) * e**(-(x/b)**a))

print(1-e**-(x/b)**a)

