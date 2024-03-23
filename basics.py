from pylab import *

# MATLAB-like API
x = np.linspace(0, 5, 10)
y = x ** 2

""" figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show() """

# The matplotlib object-oriented API
fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')

plt.show()

# Subplots approach if not being explicit with axes
fig, axes = plt.subplots()

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')

plt.show()
