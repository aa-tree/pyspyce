#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:33:06 2021

@author: Anshuk Attri(contact@anshukattri.in)
"""

from spyce_core import *
import ctypes

i_spyce_lib_location="/media/projectdrv/programming-workspace/python/spyce/"
model=[10, 399]

spyce=spyce_core(i_spyce_lib_location,model)

b_string1="2019-12-18T12:28:24"

et=c_double()
str2et=spyce.CSPICE.str2et_c
str2et.restype=c_double

str2et(b_string1.encode('utf-8'),byref(et))
print(et.value)




