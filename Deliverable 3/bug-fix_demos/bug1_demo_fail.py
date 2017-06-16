# The following code is taken directly from the code provided in the original bug report.
# https://github.com/matplotlib/matplotlib/issues/8131

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pyplot
from math import *

x = np.arange(200000)
y = np.sin(x)
pyplot.plot(x, y)
pyplot.show()
