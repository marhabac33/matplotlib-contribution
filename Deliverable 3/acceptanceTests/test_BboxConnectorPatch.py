import matplotlib.pyplot as pyplot
from matplotlib.transforms import *
from mpl_toolkits.axes_grid1.inset_locator import BboxConnectorPatch

def test_face_colour_fill_between_plots():
    fig, ax = pyplot.subplots(1, 2)
    data = ax[0].transData
    data1 = ax[1].transData
    TransformedBbox1 = TransformedBbox(Bbox.from_extents(0, 0.1, 1, 0.2), \
                                       blended_transform_factory(data, data))
    TransformedBbox2 = TransformedBbox(Bbox.from_extents(0, 0.1, 1, 0.2), \
                                       blended_transform_factory(data1, data1))
    patch = BboxConnectorPatch(TransformedBbox1, TransformedBbox2, loc1a=1, \
                               loc2a=2, loc1b=4, loc2b=3, ec = "r", fc = "r")
    patch.set_clip_on(False)
    ax[0].add_patch(patch)
    pyplot.show()
    assert patch.get_fill()

def test_face_colour_fill_between_and_on_plots():
    fig, ax = pyplot.subplots(1, 2)
    data = ax[0].transData
    data1 = ax[1].transData
    TransformedBbox1 = TransformedBbox(Bbox.from_extents(0.5, 0.1, 0.5, 0.2), \
                                       blended_transform_factory(data, data))
    TransformedBbox2 = TransformedBbox(Bbox.from_extents(0.5, 0.1, 0.5, 0.2), \
                                       blended_transform_factory(data1, data1))
    patch = BboxConnectorPatch(TransformedBbox1, TransformedBbox2, loc1a=4, \
                               loc2a=3, loc1b=2, loc2b=1, ec = "r", fc = "r")
    patch.set_clip_on(False)
    ax[0].add_patch(patch)
    pyplot.show()
    assert patch.get_fill()


if __name__ == "__main__":
    test_face_colour_fill_between_plots()
    test_face_colour_fill_between_and_on_plots()
