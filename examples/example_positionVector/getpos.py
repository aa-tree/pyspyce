#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.spyce_core import *;
import ctypes

i_spyce_lib_location="/media/projectdrv/programming-workspace/python/spyce/"
model=[10, 399]

spyce=spyce_core(i_spyce_lib_location,model)

#b_string1="01/01/2019"
b_string1="2019-12-18T12:28:24"

et=c_double()
str2et=spyce.CSPICE.str2et_c
str2et.restype=c_double

str2et(b_string1.encode('utf-8'),byref(et))



#Using NAIF SPICE's spkez_c
print("Using NAIF SPICE's spkez_c:")
print()
pos_earth=spyce.spkez_c(399, et, "J2000", "NONE", 0)
for x in pos_earth:
    print(x)

print()

print("Using SPYCE's routine:")
print()
spyce.set_IBC(0) ##IBC is the reference frame. 0 denotes solar system barycentre
pos_earth=spyce.get_state_wrt_ibc(et,399)
for x in pos_earth:
    print(x)


