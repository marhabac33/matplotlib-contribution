# The following code is based on the code provided in the original bug report.
# https://github.com/matplotlib/matplotlib/issues/7460

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pyplot

pyplot.plot([-100, 100])
xmin, xmax = pyplot.xlim()
pyplot.xlim(right=np.nan)
pyplot.show()

