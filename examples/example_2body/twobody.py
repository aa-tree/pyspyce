#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyspyce import spyce_core as pyspyce;

import ctypes

i_spyce_lib_location="/media/projectdrv/programming-workspace/python/pyspyce/"
model=[10, 399]

spyce=pyspyce(i_spyce_lib_location,model)

#b_string1="01/01/2019"
b_string1="2019-12-18T12:28:24"

et=c_double()
str2et=spyce.CSPICE.str2et_c
str2et.restype=c_double

str2et(b_string1.encode('utf-8'),byref(et))

spyce.set_IBC(0)


print(spyce.get_mu_m3(612))






