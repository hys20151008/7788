# -*- coding: utf-8 -*-

from sympy import *
from sympy.plotting import plot
from matplotlib import style

x = symbols('x')

p = plot(1/(exp(-x)+1),show=False, legend=True)
p1 = plot(1/(exp(-(x-1))+1),show=False)
p1[0].line_color = 'red'

p2 = plot(1/(exp(-(x-1)/3)+1),show=False)
p2[0].line_color = 'green'

p3 = plot(1/(exp(-(x-1)/5)+1),show=False)
p3[0].line_color = 'blue'

p4 = plot(exp(-x)/(1+exp(-x))**2,show=False)
p4[0].line_color = 'yellow'

p5 = plot(exp(-x/2)/(2*(1+exp(-x/2)))**2,show=False)
p5[0].line_color = 'black'

p.append(p1[0])
p.append(p2[0])
p.append(p3[0])
p.append(p4[0])
p.append(p5[0])

style.use('ggplot')
p.show()


