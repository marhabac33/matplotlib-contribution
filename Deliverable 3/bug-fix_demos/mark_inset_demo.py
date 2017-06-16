# The following code was modified from
# http://stackoverflow.com/questions/32423187/how-can-i-make-matplotlib-mark-inset-display-line-on-top-of-the-graph

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

import numpy as np

fig, ax = plt.subplots()
data = np.random.random(1000) - .5
plt.plot(data)
plt.axhline(y=0, color='black')

axins = zoomed_inset_axes(ax, 8, loc=1)
axins.plot(data)
axins.axhline(y=0, color='black')
axins.axis([450, 550, -0.025, 0.025])

plt.yticks(visible=False)
plt.xticks(visible=False)

mark_inset(ax, axins, loc1=3, loc2=4, fc="r", ec="k", alpha=0.3, zorder=3)
plt.show()
