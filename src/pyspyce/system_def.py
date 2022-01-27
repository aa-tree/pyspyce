#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .error_codes import *

class system_def:
    
    __IBC=0 #IBC is the system's barycentre. Default value is 0, which is the solar system barycentre.
    
    __IPB=-999 # NAIF ID of primary body. -999 implies system has not been initialised.
    
    __ISB=-999 #  NAIF ID of Secondary body. -999 implies 2nd body has not been initialised.
    
    __IS_RTBP=False
    
    def __init__(self, *args):
        # Empty constuctor. Called on first initilisation of spyce_core object.
        
        if len(args)==0:
            return
        elif len(args)>=2:
            
            ## 2body system constructor.
            if (isinstance(args[0], int)) & (isinstance(args[1], int)):
                self.__IPB=args[0]
                self.__ISB=args[1]
                if(len(args)>=3):
                    self.__IS_RTBP=True
                
                return
            else:
                exit(error_codes.system_def_2body_error)
        
        else:
            exit(error_codes.system_def_constructor_error)

        
        return
    
    
    def set_barycentre(self, ibc):
        self.__IBC=ibc
        return
    
    def get_barycentre(self):
        return self.__IBC
    
