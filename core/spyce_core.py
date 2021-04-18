from ctypes import *
from core.list_bodies import *
from core.error_codes import *

import sys
import os
import yaml
from core.state import *
from core.cspice_supp import *
from core.spiceypy_supp import *
from spiceypy import *

class spyce_core:
    
      
    SPYCE_LIB = "../../"
   
    list_bodies_array=[]
    list_kernels=[]
    
    
    # Core variables, do not alter, or assign directly
    
    IMAX=180 # The max number of bodies in JPL's ephemerides. 
    
    MU_LENGTH_2=113
    
    ISPC=False
      
    # This constructor initialises all of SPYCE global variables.
    #
    
    IBC=0 #IBC is the system's barycentre. Default value is 0, which is the solary system barycentre.
    
    
    

    REF_FRAME='J2000'
    ABCORR = 'NONE'
    
    VDIM=6 #Standard min state vector length.
    
    def __init__(self, spyce_core_location, model=[0]):

        self.SPYCE_LIB=spyce_core_location
        self.read_model_spyce(model)
        return
    
    # def read_config(self):
    #     configFile=self.SPYCE_LIB+"/config/config.yaml"
    #     with open(configFile) as f:
    #         config = yaml.load(f,Loader=yaml.FullLoader)
            
    #     self.CSPICE_LIB=config["cspice_location"]
    #     return 
            
    def read_model_spyce(self, model_file):
        
        # with open(model_file) as f:
        #     content = f.readlines()
        # # Now that we know the length of model.dat file, we can define the variable MMAX, and use it to initialise other important variables.
        
        # #MMAX = len(content)
       
        for line in model_file:
           new_body=spyce_list_bodies()
           if(self.check_list_array_forID(line)==False):
               
               new_body.set_ID(line)
               eph_temp=new_body.get_ibc_eph_ref_by_id(line,self)
               if eph_temp is not None:
                   new_body.set_ibc_eph(eph_temp[1])
                   self.add_kernelNametoList(eph_temp[0])
                   self.list_bodies_array.append(new_body)

        
        self.load_kernels_all()        
        return
    

    def check_list_array_forID(self, b_id):
        """
        

        Parameters
        ----------
        spyce_core_obj : obj
            spyce_core class Object.
        b_id : str
            ID of the body read from the model array.

        Returns
        -------
        True if bodyid is already in array. False if the bodyid is unique.

        """
        
        if(len(self.list_bodies_array)>0):
            found=False
            for body in self.list_bodies_array:
                if(body.get_ID()==b_id):
                    found=True
            
            return found
        else:
            return False
        
        
        
        return
    
    
    def add_kernelNametoList(self, kernel_name_toadd):
            
        found=False
            
        for kernel in self.list_kernels:
            if(kernel_name_toadd.strip()==kernel):
                found=True
                        
        if(found==False):
            self.list_kernels.append(kernel_name_toadd)
             
        return
        

        
    def load_kernels_all(self):
        #cDLL=self.return_SPICE_Object()
        for kernel in self.list_kernels:
            kernel_path=self.SPYCE_LIB+"eph/"+kernel
            #cDLL.furnsh_c(kernel_path.encode('utf-8'))
            spiceypy.furnsh(kernel_path)
        
        # Now that the required ephemerides have been loaded, we load the leapsecond kernel

        if(self.ISPC):
            kernel_path=self.SPYCE_LIB+"gkernels/naif0012.tls.pc"
        else:
            kernel_path=self.SPYCE_LIB+"gkernels/naif0012.tls"
        
        #cDLL.furnsh_c(kernel_path.encode('utf-8'))
        spiceypy.furnsh(kernel_path)

        
        kernel_path=self.SPYCE_LIB+"gkernels/gm_de431.tpc"
        #cDLL.furnsh_c(kernel_path.encode('utf-8'))
        spiceypy.furnsh(kernel_path)

        kernel_path=self.SPYCE_LIB+"gkernels/latest_leapseconds.tls"
        #cDLL.furnsh_c(kernel_path.encode('utf-8'))
        spiceypy.furnsh(kernel_path)

        return
    

    

    def set_barycentre(self, ibc):
        self.IBC=ibc
        return
    
    def get_barycentre(self):
        return self.IBC
    
    def get_referenceframe(self):
        return self.REF_FRAME
    
    def set_referenceframe(self, frame):
        self.REF_FRAME=frame
        return
    
    def converttime_toet(self, time):
        return converttime_toet(time)
    
    def get_state_wrt_barycentre(self, time, body_id):
        """
        

        Parameters
        ----------
        time : Float
            Ephemerides time at which the position is needed.
        body_id : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return get_state_wrt_barycentre(self, time, body_id)
    
    def get_mu(self, bodyid):
        return get_mu(self, bodyid)
    
    def get_mu_m3(self, bodyid):
        return get_mu_m3(self, bodyid)
    

    