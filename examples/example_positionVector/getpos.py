#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyspyce import *
from spiceypy import *
from pyspyce.pyspyce import pyspyce

from pyspyce.system_def import system_def
i_data_directory="/media/projectdrv/programming-workspace/python/pyspyce/data/"
model=[10, 399]

spyce=pyspyce(i_data_directory, model)

#b_string1="01/01/2019"
time_string1="2019-12-18T12:28:24"

et=spiceypy.str2et(time_string1)
spyce.set_barycentre(0)  # IBC is the reference frame. 0 denotes solar system barycentre
pos_earth=spyce.get_state_wrt_barycentre(et,399)
for x in pos_earth:
    print(x)




