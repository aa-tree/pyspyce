#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:23:19 2021

@author: Anshuk Attri(contact@anshukattri.in)

"""
import spyce_core

class spyce_list_bodies:
    # This class serves as a temporary data store for body model information.
    
    def set_ID(self, body_id):
        self.id=body_id
        return
    
    def set_ibc_eph(self, ibc_eph):
        self.ref_ibc=ibc_eph
        return
    
    def set_ephName(self, name):
        self.eph=name
        return
    
    
    def get_ID(self):
        return self.id
    
    
    def get_ibc_eph_ref_by_id(self, bodyid):
        
        list_of_bodies_file=spyce_core.SPYCE_LIB+"spice_supp/list_of_bodies.csv"
        
        with open(list_of_bodies_file) as f:
            content = f.readlines()
            
        for line in content:
            line_split=line.split(",")
            
            if line_split[0]==bodyid:
                return [line_split[4],line_split[3]]
            
        
        return
    
        
        
            


    

    
    
    
