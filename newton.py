# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: (x-1)**2 - 2

x = np.linspace(0, 5, 100)
y = [f(elt) for elt in x]

plt.plot(x, y)
plt.axis([0, 6, 0, 36])
plt.show()

def newton(init_value):
    f_change, f_current = init_value, init_value
    ff = lambda x: 2*x + 2
    count = 0
    x = init_value
    while f_change > 0.00001:
        b = x - f(x)/ff(x)
        f_change = x - b
        x = b
        count += 1
    return b


if __name__ == '__main__':
    print(newton(3))
        
    
