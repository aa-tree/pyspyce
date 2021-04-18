#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes
from core.spyce_core import *;
 
    
def get_state_wrt_ibc(spyce_core_obj, time, body_id):
    
    temp_rJ0=[0] * 6
    RJ0 = (ctypes.c_double * len(temp_rJ0))(*temp_rJ0)
    #RJ0 = ctypes.c_double()
    LTIME=ctypes.c_double();
    spkez=spyce_core_obj.CSPICE.spkez_c(body_id, time, spyce_core_obj.REF_FRAME.encode('utf-8'), spyce_core_obj.ABCORR.encode('utf-8'), spyce_core_obj.IBC, ctypes.byref(RJ0), byref(LTIME))
    
    return RJ0;

