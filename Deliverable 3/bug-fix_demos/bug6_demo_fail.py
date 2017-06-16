# The following code is taken directly from the code provided in the original bug report.
# https://github.com/matplotlib/matplotlib/issues/7742

import matplotlib.pyplot as plt
from datetime import datetime

fig, axs = plt.subplots(2, 1)

axs[0].axhline(1.5)
axs[0].plot([datetime(2016, 1, 1, 0, 0, 0), datetime(2016, 1, 2, 0, 0, 0)], [1, 2])

axs[1].plot([datetime(2016, 1, 1, 0, 0, 0), datetime(2016, 1, 2, 0, 0, 0)], [1, 2])
axs[1].axhline(1.5)

plt.show()
