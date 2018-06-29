# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('axes', 0.5))
ax.spines['bottom'].set_position(('axes', 0.5))

x = np.linspace(-5, 5, 1000)

ax.plot(x, x)
ax.text(-4, 4, 'y=x', color='r')
ax.set_xlabel('x', horizontalalignment='right', x=1.0)
ax.set_ylabel('y', horizontalalignment='right', y=1.0, rotation=0)
plt.show()

