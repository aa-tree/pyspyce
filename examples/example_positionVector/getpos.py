#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.spyce_core import *;
from spiceypy import *

i_spyce_lib_location="/media/projectdrv/programming-workspace/python/spyce/"
model=[10, 399]

spyce=spyce_core(i_spyce_lib_location,model)

#b_string1="01/01/2019"
time_string1="2019-12-18T12:28:24"

et=spiceypy.str2et(time_string1)

spyce.set_barycentre(0) ##IBC is the reference frame. 0 denotes solar system barycentre
pos_earth=spyce.get_state_wrt_barycentre(et,399)
for x in pos_earth:
    print(x)


