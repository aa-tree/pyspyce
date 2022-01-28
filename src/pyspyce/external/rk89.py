#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def rk89_internal(time, vstate, dt, external_module, dim=6):
    output=[0.0]*6
    fortran.rk89(time, dim, vstate, dt, external_module, output)
    return output
    
