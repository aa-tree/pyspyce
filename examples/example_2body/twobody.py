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

spyce.set_IBC(0)


print(spyce.get_mu_m3(612))






