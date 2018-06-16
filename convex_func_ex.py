import matplotlib.pyplot as plt
import numpy as np

fig = plt.subplots()

x = np.linspace(-8,8,1000)
y = [elt**2 for elt in x]

x1, y1 = [-3, 5], [9, 25]

f = lambda x: 2*x + 15

y2 = (9 + 15)/2
x2 = -1.5


plt.plot(x, y)
plt.plot(x1, y1, 'r')
plt.plot(-3, 9,'ro')
plt.plot(5, 25,'ro')
plt.plot(-1.5, 12, 'g*')
plt.plot(1,1,'r*')
plt.text(-5,9,'(x,f(x))')
plt.text(5.2,25,'(y,f(y))')
plt.text(-2,15,r'$\frac{f(x)+f(y)}{2}$')
plt.text(1.5, 0.2, r'$f(\frac{x+y}{2})$')
plt.title('凸函数示意图,图上任意两点之间的弦(即线段)都在函数图像之上')

plt.show()
