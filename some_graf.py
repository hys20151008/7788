# -*- coding: utf-8 -*-


from sympy import symbols
from sympy.plotting import plot, plot_implicit
import matplotlib.pyplot as plt

def move_sympyplot_to_axes(p, ax):
    backend = p.backend(p)
    backend.ax = ax
    backend.process_series()
    backend.ax.spines['right'].set_color('none')
    backend.ax.spines['bottom'].set_position('zero')
    backend.ax.spines['top'].set_color('none')
    plt.close(backend.fig)

x = symbols('x')
p1 = plot((x**2,(x,-2,2)),(x,(x,-4,4)),legend=True, show=False)
p1[1].line_color = 'r'
p2 = plot((1/x,(x,-4,4)),ylim=(-2,2),legend=True, show=False)


fig,(ax,ax2) = plt.subplots(ncols=2)
move_sympyplot_to_axes(p1,ax)
move_sympyplot_to_axes(p2, ax2)
plt.show()

