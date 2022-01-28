#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes
from spiceypy import *
    
def get_state_wrt_ibc(spyce_core_obj, time, body_id):
    
    # temp_rJ0=[0] * 6
    # RJ0 = (ctypes.c_double * len(temp_rJ0))(*temp_rJ0)
    # #RJ0 = ctypes.c_double()
    # LTIME=ctypes.c_double();
    # spkez=spyce_core_obj.CSPICE.spkez_c(body_id, time, spyce_core_obj.REF_FRAME.encode('utf-8'), spyce_core_obj.ABCORR.encode('utf-8'), spyce_core_obj.IBC, ctypes.byref(RJ0), byref(LTIME))
    RJ0, ltime=spkez(body_id, time,spyce_core_obj._REF_FRAME,spyce_core_obj._ABCORR,spyce_core_obj._system_def.get_barycentre())
    return RJ0;

