#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:33:06 2021

@author: Anshuk Attri(contact@anshukattri.in)
"""

from core.spyce_core import *
import ctypes


#To Convert this string into ephemerides time

b_string1="2019-12-18T12:28:24"


i_spyce_lib_location="/media/projectdrv/programming-workspace/python/spyce/"
model=[10, 399]

spyce=spyce_core(i_spyce_lib_location,model)


et=c_double()
str2et=spyce.CSPICE.str2et_c

str2et(b_string1.encode('utf-8'),byref(et))
print('Result from CSPICE Native Routine:')
print(et.value)

## Alternatively:
    
print('Result from SPYCE Routine:')
print(spyce.str2et_c(b_string1))




