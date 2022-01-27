#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.spyce_core import *;
from spiceypy import *
from core.xpp.xpp_twobody_nopert import *

i_spyce_lib_location="/media/projectdrv/programming-workspace/python/pyspyce/"
model=[10, 399]

spyce=spyce_core(i_spyce_lib_location,model)

# print("Example: Convert a time string to Ephemeris time.")
# print("Input -> 2019-12-18T12:28:24")
# print(converttime_toet("2019-12-18T12:28:24"))
vstate =[0.00]*6
time=spyce.converttime_toet("2019-12-18T12:28:24")
# external = xpp_twobody_nopert(pyspyce, time, vstate)
# print(type(external))
# print(pyspyce.rk89(time, vstate, 0.0001, external, 6))

spyce.init_rtbp_system(399, 301)

