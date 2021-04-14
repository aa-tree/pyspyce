#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:33:06 2021

@author: Anshuk Attri(contact@anshukattri.in)
"""

from spyce_core import *;
from pos import *;
import ctypes

i_spyce_lib_location="/media/projectdrv/programming-workspace/python/spyce/"
i_cspice_lib_location="/media/projectdrv/programming-workspace/python/spyce/cspice/lib/cspice.so"
i_model_file_location="/media/projectdrv/programming-workspace/python/spyce/examples/example_positionVector/model.dat"

spyce=spyce_core(i_spyce_lib_location, i_cspice_lib_location, i_model_file_location)

#b_string1="01/01/2019"
b_string1="2019-12-18T12:28:24"

et=c_double()
str2et=spyce.CSPICE.str2et_c
str2et.restype=c_double

str2et(b_string1.encode('utf-8'),byref(et))

spyce.set_IBC(0)
pos_earth=pos.get_state_wrt_ibc(spyce, et,0)
distance=(pos_earth[0]**2+pos_earth[1]**2+pos_earth[2]**2)**0.5
print(distance)



