#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes

def str2et_c(spycore_obj, time_string):
    check_spyceObject(spycore_obj)

    et=ctypes.c_double()
    str2et=spycore_obj.CSPICE.str2et_c
    str2et(time_string.encode('utf-8'),ctypes.byref(et))
    

    return et.value


def spkez_c(spyce_core_obj, body_id, time, reference_frame, abcorr, observer):
    check_spyceObject(spycore_obj)

    if (reference_frame=="" or reference_frame==None):
        reference_frame=spyce_core_obj.REF_FRAME.encode('utf-8')
    else:
        reference_frame=reference_frame.encode('utf-8')
        
    
    if (abcorr=="" or abcorr==None) :
        abcorr=spyce_core_obj.ABCORR.encode('utf-8')
    else:
        abcorr=abcorr.encode('utf-8')
        
    
    
    
    temp_rJ0=[0] * 6
    RJ0 = (ctypes.c_double * len(temp_rJ0))(*temp_rJ0)
    #RJ0 = ctypes.c_double()
    LTIME=ctypes.c_double();
    spkez=spyce_core_obj.CSPICE.spkez_c(body_id, time, reference_frame,abcorr, observer, ctypes.byref(RJ0), ctypes.byref(LTIME))
    
    output_rj0=[0.0] * 7
    
    for x in range(6):
        output_rj0[x]=RJ0[x]
        
    output_rj0[6]=LTIME.value
        
    return output_rj0

def get_mu(spycore_obj, bodyid):

    check_spyceObject(spycore_obj)
    
    # Check if the loaded SPICE Kernels have the value of mu
    
    if(spycore_obj.CSPICE.bodfnd_c(bodyid,'GM'.encode('utf-8'))==1):
        values_t=[0] * 2
        values= (ctypes.c_double * len(values_t))(*values_t)
        dim=ctypes.c_int()
        bodvrd_c=spycore_obj.CSPICE.bodvrd_c
        
        bodvrd_c(str(bodyid).encode('utf-8'),'GM'.encode('utf-8'),ctypes.c_int(1),ctypes.byref(dim), ctypes.byref(values))
        return values[0] ##The values in the SPICE Kernel is in Km3s-2, we change it to m3s-2
        

    else:
        # If the value of the gravitational constant is not in the kernel, read it from the supplementary file.
        gm_file= spycore_obj.DATA_DIR + "/spice_supp/gm_remaining.csv"

        gm_toreturn=0.0
        with open(gm_file) as f:
            content = f.readlines()
        
        for line in content:
            line=line.rstrip();
            line_split=line.split(",")

            if int(line_split[0].strip())== bodyid:
                 gm_toreturn=float(line_split[1])

        return gm_toreturn
    
    
def get_mu_m3(spycore_obj, bodyid):
    return get_mu(spycore_obj, bodyid)*10**9