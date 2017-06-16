from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import six
from six.moves import xrange
from itertools import chain
from distutils.version import LooseVersion
import io

import datetime

import pytz

import numpy as np
from numpy import ma
from numpy import arange
from cycler import cycler
import pytest

import warnings

import matplotlib
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import matplotlib.markers as mmarkers
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
from numpy.testing import assert_allclose, assert_array_equal
from matplotlib.cbook import IgnoredKeywordWarning
import matplotlib.colors as mcolors


@image_comparison(baseline_images=['legend_lorder'], extensions=['png'])
def test_legend_lorder_using_pyplot():
    'Legend should have: tan, sin, cos, in that order.'
    x = np.linspace (0,50,400)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)

    plt.plot(x, y1, lorder=2, label="sin")
    plt.plot(x, y2, lorder=3, label="cos")
    plt.plot(x, y3, lorder=1, label="tan")
    plt.legend()


def test_legend_lorder_single_entry():
    'Test single legend entry is unchanged.'
    x = np.linspace (0,50,400)
    fig,ax = plt.subplots(1)
    ax.plot(x, x + 1, lorder=5, label="Test Singleton")

    handles = ['Line2D(Test Singleton)']
    labels = [u'Test Singleton']

    legend = plt.legend()

    handles_equal = [(str(handle1) == str(handle2)) for (handle1, handle2) in
                     zip(legend.legendHandles, handles)]
    handles_equal = reduce((lambda x, y: x and y), handles_equal)
    assert handles_equal

    texts = [x.get_text() for x in legend.texts]
    texts_equal = texts == labels
    assert texts_equal


def test_legend_lorder_default_order():
    'Test legend with 2 entries with their default order maintained.'
    x = np.linspace (0,50,400)
    fig,ax = plt.subplots(1)
    ax.plot(x, x + 1, lorder=1, label="Test 1")
    ax.plot(x, x - 1, lorder=2, label="Test 2")

    handles = ['Line2D(Test 1)', 'Line2D(Test 2)'] 
    labels = [u'Test 1', u'Test 2']

    legend = plt.legend()

    handles_equal = [(str(handle1) == str(handle2)) for (handle1, handle2) in
                     zip(legend.legendHandles, handles)]
    handles_equal = reduce((lambda x, y: x and y), handles_equal)
    assert handles_equal

    texts = [x.get_text() for x in legend.texts]
    texts_equal = texts == labels
    assert texts_equal
    

def test_legend_lorder_changed_order():
    'Test legend with 2 entries with their default order reversed.'
    x = np.linspace (0,50,400)
    fig,ax = plt.subplots(1)
    ax.plot(x, x + 1, lorder=2, label="Test 2")
    ax.plot(x, x - 1, lorder=1, label="Test 1")

    handles = ['Line2D(Test 1)', 'Line2D(Test 2)'] 
    labels = [u'Test 1', u'Test 2']

    legend = plt.legend()

    handles_equal = [(str(handle1) == str(handle2)) for (handle1, handle2) in
                     zip(legend.legendHandles, handles)]
    handles_equal = reduce((lambda x, y: x and y), handles_equal)
    assert handles_equal

    texts = [x.get_text() for x in legend.texts]
    texts_equal = texts == labels
    assert texts_equal


def test_legend_lorder_basic():
    'Test longer legend with set order.'
    x = np.linspace (0,50,400)
    fig,ax = plt.subplots(1)
    ax.plot(x, x + 1, lorder=1, label="Test 1")
    ax.plot(x, x - 1, lorder=4, label="Test 4")
    ax.plot(x, x - 1, lorder=5, label="Test 5")
    ax.plot(x, x - 1, lorder=2, label="Test 2")
    ax.plot(x, x - 1, lorder=3, label="Test 3")

    handles = ['Line2D(Test 1)', 'Line2D(Test 2)', 'Line2D(Test 3)',
               'Line2D(Test 4)', 'Line2D(Test 5)']
    labels = [u'Test 1', u'Test 2', u'Test 3', u'Test 4', u'Test 5']

    legend = plt.legend()

    handles_equal = [(str(handle1) == str(handle2)) for (handle1, handle2) in
                     zip(legend.legendHandles, handles)]
    handles_equal = reduce((lambda x, y: x and y), handles_equal)
    assert handles_equal

    texts = [x.get_text() for x in legend.texts]
    texts_equal = texts == labels
    assert texts_equal


def test_legend_lorder_duplicate_values():
    'Test longer legends behaviour when two lorder kwargs have the same value.'
    x = np.linspace (0,50,400)
    fig,ax = plt.subplots(1)
    ax.plot(x, x + 1, lorder=1, label="Test 1")
    ax.plot(x, x - 1, lorder=4, label="Test 5")
    ax.plot(x, x - 1, lorder=2, label="Test 2")
    ax.plot(x, x - 1, lorder=2, label="Test 3")
    ax.plot(x, x - 1, lorder=3, label="Test 4")

    handles = ['Line2D(Test 1)', 'Line2D(Test 2)', 'Line2D(Test 3)',
               'Line2D(Test 4)', 'Line2D(Test 5)'] 
    labels = [u'Test 1', u'Test 2', u'Test 3', u'Test 4', u'Test 5']

    legend = plt.legend()

    handles_equal = [(str(handle1) == str(handle2)) for (handle1, handle2) in
                     zip(legend.legendHandles, handles)]
    handles_equal = reduce((lambda x, y: x and y), handles_equal)
    assert handles_equal

    texts = [x.get_text() for x in legend.texts]
    texts_equal = texts == labels
    assert texts_equal


def test_legend_lorder_random_values():
    'Test longer legends maintains relative order with random values.'
    x = np.linspace (0,50,400)
    fig,ax = plt.subplots(1)
    ax.plot(x, x + 1, lorder=102, label="Test 3")
    ax.plot(x, x - 1, lorder=42, label="Test 2")
    ax.plot(x, x - 1, lorder=2569, label="Test 5")
    ax.plot(x, x - 1, lorder=0, label="Test 1")
    ax.plot(x, x - 1, lorder=300, label="Test 4")

    handles = ['Line2D(Test 1)', 'Line2D(Test 2)', 'Line2D(Test 3)',
               'Line2D(Test 4)', 'Line2D(Test 5)'] 
    labels = [u'Test 1', u'Test 2', u'Test 3', u'Test 4', u'Test 5']

    legend = plt.legend()

    handles_equal = [(str(handle1) == str(handle2)) for (handle1, handle2) in
                     zip(legend.legendHandles, handles)]
    handles_equal = reduce((lambda x, y: x and y), handles_equal)
    assert handles_equal

    texts = [x.get_text() for x in legend.texts]
    texts_equal = texts == labels
    assert texts_equal


def test_legend_lorder_some_unordered():
    '''Test longer legends maintains relative order when some handlers do not
    have lorder.'''
    x = np.linspace (0,50,400)
    fig,ax = plt.subplots(1)
    ax.plot(x, x + 1, label="Test 4")
    ax.plot(x, x - 1, label="Test 5")
    ax.plot(x, x - 1, lorder=1, label="Test 1")
    ax.plot(x, x - 1, lorder=2, label="Test 2")
    ax.plot(x, x - 1, lorder=3, label="Test 3")

    handles = ['Line2D(Test 1)', 'Line2D(Test 2)', 'Line2D(Test 3)',
               'Line2D(Test 4)', 'Line2D(Test 5)'] 
    labels = [u'Test 1', u'Test 2', u'Test 3', u'Test 4', u'Test 5']

    legend = plt.legend()

    handles_equal = [(str(handle1) == str(handle2)) for (handle1, handle2) in
                     zip(legend.legendHandles, handles)]
    handles_equal = reduce((lambda x, y: x and y), handles_equal)
    assert handles_equal

    texts = [x.get_text() for x in legend.texts]
    texts_equal = texts == labels
    assert texts_equal
