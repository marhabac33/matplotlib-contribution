#to run any of the following acceptance tests,
#run the following imports:

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pyplot

#and then copy and paste your desired acceptance test.


# Test 1 (Legend should have: tan, sin, cos, in that order.)
x = np.linspace (0,50,400)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

pyplot.plot(x, y1, lorder=2, label="sin")
pyplot.plot(x, y2, lorder=3, label="cos")
pyplot.plot(x, y3, lorder=1, label="tan")
pyplot.legend()
pyplot.ylim(-1.5, 1.5)
pyplot.show()


#Test 2 (Legend should have: y = 4x, y = 2x+1, y = 3x, y = x+2, y = 5x, in that order.)
#x = np.arange(10)

#pyplot.plot(x, x + 1, lorder=4, label="y = x+2")
#pyplot.plot(x, x*2 + 4, lorder=2, label="y = 2x+1")
#pyplot.plot(x, x*3, lorder=3, label="y = 3x")
#pyplot.plot(x, x*4, lorder=1, label="y = 4x")
#pyplot.plot (x, x*5, lorder=5, label="y = 5x")
#pyplot.legend()
#pyplot.ylim(0,50)
#pyplot.show()

#Test 3 (Verify that no problems arise when lorder is missing (in this case order does not matter))
#x = np.linspace (0,50,400)
#y1 = np.sin(x)
#y2 = np.cos(x)
#y3 = np.tan(x)

#pyplot.plot(x, y1, label="sin")
#pyplot.plot(x, y2, label="cos")
#pyplot.plot(x, y3, label="tan")
#pyplot.legend()
#pyplot.ylim(-1.5, 1.5)
#pyplot.show()

#Test 4 (Verify functionality of lorder works with more obscure values. 
#No error should be produced and legend should have: y = 4x, y = 2x+1, y = 3x, y = x+2, y = 5x, in that order.)
#x = np.arange(10);

#pyplot.plot(x, x + 1, lorder=452, label="y = x+2")
#pyplot.plot(x, x*2 + 4, lorder=2, label="y = 2x+1")
#pyplot.plot(x, x*3, lorder=30, label="y = 3x")
#pyplot.plot(x, x*4, lorder=0, label="y = 4x")
#pyplot.plot (x, x*5, lorder=99999, label="y = 5x")
#pyplot.legend()
#pyplot.ylim(0,50)
#pyplot.show()


#Test 5 (Verify non ordered labels appear last. Legend should have : sin, cos, tan, in that order.)
#x = np.linspace (0,50,400)
#y1 = np.sin(x)
#y2 = np.cos(x)
#y3 = np.tan(x)

#pyplot.plot(x, y1, lorder=2, label="sin")
#pyplot.plot(x, y2, lorder=3, label="cos")
#pyplot.plot(x, y3, label="tan")
#pyplot.legend()
#pyplot.ylim(-1.5, 1.5)
#pyplot.show()

