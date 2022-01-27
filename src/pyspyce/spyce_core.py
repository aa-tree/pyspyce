from ctypes import *
from spiceypy import *
from .list_bodies import *
from .error_codes import *
from .state import * 
from .cspice_supp import *
from .spiceypy_supp import *
from .external.rk89 import *
from .system_def import *

class spyce_core:
    
      
    _DATA_DIR = ""
    _list_bodies_array=[]
    _list_kernels=[]
    
    
    # Core variables, do not alter, or assign directly
    
    _IMAX=180 # The max number of bodies in JPL's ephemerides. 
    
    _MU_LENGTH_2=113
    
    _ISPC=False
      
    
    
    _system_def=None #System Definition Object.
    

    _REF_FRAME='J2000'
    _ABCORR = 'NONE'
    
    _VDIM=6 #Standard min state vector length.
    
    # This constructor initialises all of SPYCE global variables.
    #

    def __init__(self, data_directory, model=[0]):
        
        self._DATA_DIR=data_directory
        self._read_model_spyce(model)
        self._system_def=system_def()
        return
    
    # def read_config(self):
    #     configFile=self.SPYCE_LIB+"/config/config.yaml"
    #     with open(configFile) as f:
    #         config = yaml.load(f,Loader=yaml.FullLoader)
            
    #     self.CSPICE_LIB=config["cspice_location"]
    #     return 
            
    def _read_model_spyce(self, model_file):
        
        # with open(model_file) as f:
        #     content = f.readlines()
        # # Now that we know the length of model.dat file, we can define the variable MMAX, and use it to initialise other important variables.
        
        # #MMAX = len(content)
       
        for line in model_file:
           new_body=spyce_list_bodies()
           if(self._check_list_array_forID(line)==False):
               
               new_body.set_ID(line)
               eph_temp=new_body.get_ibc_eph_ref_by_id(line,self)
               if eph_temp is not None:
                   new_body.set_ibc_eph(eph_temp[1])
                   self._add_kernelNametoList(eph_temp[0])
                   self._list_bodies_array.append(new_body)

        
        self._load_kernels_all()        
        return
    

    def _check_list_array_forID(self, b_id):
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
        
        if(len(self._list_bodies_array)>0):
            found=False
            for body in self._list_bodies_array:
                if(body.get_ID()==b_id):
                    found=True
            
            return found
        else:
            return False
        
        
        
        return
    
    
    def _add_kernelNametoList(self, kernel_name_toadd):
            
        found=False
            
        for kernel in self._list_kernels:
            if(kernel_name_toadd.strip()==kernel):
                found=True
                        
        if(found==False):
            self._list_kernels.append(kernel_name_toadd)
             
        return
        

        
    def _load_kernels_all(self):
        #cDLL=self.return_SPICE_Object()
        for kernel in self._list_kernels:
            kernel_path= self._DATA_DIR + kernel
            #cDLL.furnsh_c(kernel_path.encode('utf-8'))
            spiceypy.furnsh(kernel_path)
        
        # Now that the required ephemerides have been loaded, we load the leapsecond kernel

        if(self._ISPC):
            kernel_path= self._DATA_DIR + "/naif0012.tls.pc"
        else:
            kernel_path= self._DATA_DIR + "/naif0012.tls"
        
        #cDLL.furnsh_c(kernel_path.encode('utf-8'))
        spiceypy.furnsh(kernel_path)

        
        kernel_path= self._DATA_DIR + "/gm_de431.tpc"
        #cDLL.furnsh_c(kernel_path.encode('utf-8'))
        spiceypy.furnsh(kernel_path)

        kernel_path= self._DATA_DIR + "/latest_leapseconds.tls"
        #cDLL.furnsh_c(kernel_path.encode('utf-8'))
        spiceypy.furnsh(kernel_path)

        return
    
