# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


x = np.array([ 6,  8, 10, 14, 18])
y = np.array([ 7. ,  9. , 13. , 17.5, 18. ])

plt.plot(x, y, 'k.')
plt.axis([0, 25, 0, 25])


model = LinearRegression()
model.fit(x.reshape(-1,1),y.reshape(-1,1))

e = [item[0] for item in model.predict(x.reshape(-1,1))]


X = list(zip(x,x))
Y = list(zip(y,e))
for i in range(len(X)):
    plt.plot(X[i],Y[i],'r')

plt.title("Linear regression use least square method")
plt.xlabel(r'$x$', horizontalalignment='right', x=1.0)
plt.ylabel(r'$y$', horizontalalignment='right', y=1.0, rotation=0)

plt.plot(x, e)
plt.grid(True)
plt.show()
