# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()

f = lambda x: (x-1)**2 - 2
x = np.linspace(-2, 5, 100)
y = [f(elt) for elt in x]


# 移动坐标轴(中心位置)
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


xdata, ydata = [], []
ax.plot(x, y)

ln, = ax.plot([], [], 'r', animated=True)

def init():
    ax.set_xlim(0, 6)
    ax.set_ylim(-3, 36)
    return ln,


def newton(init_value):
    f_change, f_current = init_value, init_value
    ff = lambda x: 2*x - 2
    count = 0
    x = init_value
    ret = []
    while f_change > 0.001:
        ret_x =[]
        b = x - f(x)/ff(x)
        k = ff(x)
        func = lambda xx: k*(xx-x)+f(x)
        lx = np.linspace(0, 5, 100)
        ly = [func(elt) for elt in lx]

        ret_x.append(lx)
        ret_x.append(ly)
        ret.append(ret_x)

        f_change = x - b
        x = b
        count += 1
    return ret


def update(frame):
    xdata = frame[0]
    ydata = frame[1]
    ln.set_data(xdata, ydata)
    return ln,
    
    
ani = FuncAnimation(fig, update,frames= newton(4),init_func=init, blit=True, interval=2000)
# 将动画保存为gif文件
ani.save('newton_ani.gif', writer='imagemagick', fps=1)
plt.show()

