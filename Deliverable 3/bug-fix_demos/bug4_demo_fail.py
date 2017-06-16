# The following code is based on the code provided in the original bug report.
# https://github.com/matplotlib/matplotlib/issues/6921
# And taken directly from the matplotlib legened example taken from:
# http://matplotlib.org/users/legend_guide.html

import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

line1, = plt.plot([3,2,1], marker='o', label='Line 1')
line2, = plt.plot([1,2,3], marker='o', label='Line 2')

plt.legend(handler_map={line1: HandlerLine2D(numpoints=0.5)})
plt.show()
