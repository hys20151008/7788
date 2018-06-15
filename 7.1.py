# -*- coding: utf-8 -*-
# 7.1 example in book Statistical learning method

import numpy as np
import matplotlib.pyplot as plt

x1, y1 = 3, 3
x2, y2 = 4, 3
x3, y3 = 1, 1

x,y = [2, 0], [0, 2]

xx, yy = [4, 0], [0, 4]

xxx, yyy = [6, 0], [0, 6]

plt.plot(xx, yy, 'g')
plt.plot(x,y, 'r--')
plt.plot(xxx, yyy, 'r--')

plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'b*')

plt.text(3, 3.2, r'$x_{1}$')
plt.text(4, 3.2, r'$x_{2}$')
plt.text(1.1, 1, r'$x_{3}$')

# horizontalalignment='right' make xlabel at the end of axis,
# rotation=0 make ylabel horizontally
plt.xlabel(r'$x^{(1)}$', horizontalalignment='right', x=1.0)
plt.ylabel(r'$x^{(2)}$', horizontalalignment='right', y=1.0, rotation=0)
plt.title('Interval Maximum Separation Hyperplane Example')
plt.axis([0, 6, 0, 6])
plt.grid(True)
plt.show()
