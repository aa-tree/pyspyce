#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.spyce_core import *


def xpp_twobody_nopert(spycore_obj, t, vstate):
    
    if(len(vstate)<spycore_obj.VDIM):
        exit('State array was less than the min length '+spycore_obj.VDIM)
    
    spycore_obj.get_state_wrt_ibc(time, b_id)
    
    output=[0.00]*6
    output[0]=vstate[3];
    output[1]=vstate[4];
    output[2]=vstate[5]; #XP is taken from the input array.
    
    
    
    
    return 

