#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.spyce_core import *;
from spiceypy import *


i_spyce_lib_location="/media/projectdrv/programming-workspace/python/spyce/"
model=[10, 399]

spyce=spyce_core(i_spyce_lib_location,model)

print("Example: Convert a time string to Ephemeris time.")
print("Input -> 2019-12-18T12:28:24")
print(converttime_toet("2019-12-18T12:28:24"))
