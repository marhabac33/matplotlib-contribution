import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pyplot

pyplot.plot([-100, 100])

#Bellow any of the 8 lines should cause an invalid type error.

#pyplot.xlim(np.nan)
#pyplot.xlim(np.inf)
#pyplot.xlim(np.NINF)
#pyplot.xlim("x is from 0 to 10")

#pyplot.ylim(np.nan)
#pyplot.ylim(np.inf)
#pyplot.ylim(np.NINF)
#pyplot.ylim("x is from 0 to 10")

#Bellow should work as expected, and show the chart with proper x and y limits.

#pyplot.xlim(-10,10)
#pyplot.xlim([3.3, 4.4])
#pyplot.xlim(np.array([1, 5]))
#pyplot.xlim(None)

#pyplot.ylim(-10,10)
#pyplot.ylim([3.3, 4.4])
#pyplot.ylim(np.array([1, 5]))
#pyplot.ylim(None)


pyplot.show()

