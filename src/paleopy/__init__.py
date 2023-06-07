#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

paleopy
------

Python backend for Past Interpretation of Cimate Tool (aka PICT)

"""

# after `import paleopy`, all the classes defined in `core` are
# available in the `paleopy` namespace, e.g. `paleopy.proxy`
from .core import *
# plotting functions and classes will be avaible in the `plotting`
# namespace, e.g. `paleopy.plotting.heatmap`
from . import plotting
# same thing for the `utils` functions
from . import utils
# same thing for the `markov` functions
from . import markov
# import the functions to calculat the climate mode indices 
from . import indices

__author__ = 'Nicolas Fauchereau'
__email__ = "Nicolas.Fauchereau@gmail.com"
__version__ = "0.1.0"
