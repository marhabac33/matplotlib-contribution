https://github.com/matplotlib/matplotlib/issues/8131
- Error message is not informative, specifically the error message should be changed from "OverflowError: In draw_path: - - 
Exceeded cell block limit" to  include a reference to 'agg.path.chunksize' rcparam. This is because increasing the 'agg.path.chunksize' can solve the error, i.e. setting: rcParams['agg.path.chunksize'] = 1000, as described in comments. 
- Reproduced by running bug1_demo_fail.py; Changing rcParams['agg.path.chunksize'] solves error is shown by bug1_demo_pass.py). 
- Based on bug report and related comments.

https://github.com/matplotlib/matplotlib/issues/7460
- An error should be raised if matplotlib.pyplot.xlim() is given a non-numeric value (except None), specifically numpy.nan or numpy.inf, currently it sets the alter limit to either -0.001 or 0.001 which is considered an unexpected/undesierable behaviour. Possible suggested fix involves using numpy.isfinite() to sanity check the values passed to matplotlib.pyplot.xlim(). 
- Can be reproduced by running bug2_demo_fail.py, which shows the program runs without error despit passing numpy.nan to matplotlib.pyplot.xlim(). 
- Based on bug report and related comments.

https://github.com/matplotlib/matplotlib/issues/8089
- Currently matplotlib.dates.MinuteLocator() contains an attribute MAXTICKS which throws an error if exceeded, this is undesired behaviour. A current work-around exists by manually changing the matplotlib.dates.MinuteLocator() attribute after it is initialized. Suggested solution involves removing MAXTICKS attribute and allowing the system to throw an out of memory error if the program exceeds system memory resources. 
- Reproduced by running bug3_demo_fail.py, current work-around shown by running bug3_demo_pass.py. 
- Based on bug report and related comments.

https://github.com/matplotlib/matplotlib/issues/6921
- A clearer error should be raised if matplotlib.pyplot.legend(numpoints = 0.5) is not passed an integer, currently the program raises the following error: "UnboundLocalError: local variable 'xdata' referenced before assignment", with an accompanying trace. The current error is very uninformative and instead a type check should be preformed to test if input is an integer, and an exception raised if not clearly stating valid input. Error located < https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/legend_handler.py#L151 >. 
- Can be reproduced by running bug4_demo_fail.py, which shows the program crashes and raises the unhelpful error. 
- Based on bug report, matplotlib Legend Guide (http://matplotlib.org/users/legend_guide.html) and related comments.

https://github.com/matplotlib/matplotlib/issues/8059
- The facecolour of a BboxConnectorPatch object is not rendered correctly. This is believed to be caused by the BboxConnectorPatch __init__ method setting fill=False. A current work around exists by manually changing fill and setting face colour after the BboxConnectorPatch is created (i.e. calling the BboxConnectorPatch's set_fill(True) and set_facecolor('b') methods). 
- Reproduced by running bug5_demo_fail.py, current work-around shown by running bug5_demo_pass.py. 
- Based on bug report and related comments.

https://github.com/matplotlib/matplotlib/issues/7742
- The behaviour of "(fig, ax) = matplotlib.pyplot.subplots(); ax[ ].axhline()" is different depending on what is plotted first, specifically the x-axis does not appear to be rescaled resulting in the same plot being displayed differently when ploted depending on if ax[ ].axhline() was called before or after ax[].plot() was called.
- Reproduced by running bug6_demo_fail.py.
- Based on bug report and related comments.
