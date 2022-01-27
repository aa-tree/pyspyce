#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from spyce_core.error_codes import *

def check_spyceObject(spyce_obj):
    
    if(spyce_obj==None):
        exit(error_codes.spycore_var_null);
    else:
       if(spyce_obj.CSPICE==None):
           exit(error_codes.spycore_not_initialised);

    return