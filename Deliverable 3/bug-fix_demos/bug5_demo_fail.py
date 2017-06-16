# The following code is taken directly from the original bug report.
# https://github.com/matplotlib/matplotlib/issues/8059

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox, TransformedBbox, \
     blended_transform_factory
from mpl_toolkits.axes_grid1.inset_locator import BboxPatch, BboxConnector,\
     BboxConnectorPatch
fig, ax = plt.subplots(1, 2)
fig.set_size_inches(12, 6)
fig.set_tight_layout(True)
ax[0].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[1].set_xlim(0, 1)
ax[1].set_ylim(0.35, 0.65)
trans1 = blended_transform_factory(ax[0].transData, ax[0].transData)
trans2 = blended_transform_factory(ax[1].transData, ax[1].transData)
bbox = Bbox.from_extents(0, 0.4, 1, 0.6)
bbox1 = TransformedBbox(bbox, trans1)
bbox2 = TransformedBbox(bbox, trans2)
p = BboxConnectorPatch(bbox1, bbox2,
                       loc1a=1, loc2a=2, loc1b=4, loc2b=3, ec='b', fc='b')
p.set_clip_on(False)
ax[0].add_patch(p)
ax[1].yaxis.tick_right()
plt.show()
