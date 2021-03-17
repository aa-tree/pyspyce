import ctypes
from list_bodies import *

class spyce_core:
    
      
    # This constructor initialises all of SPYCE global variables.
    #
    SPYCE_LIB = "../../"
    CSPICE_LIB =" ../../cspice/"
    model_file_location="model.dat"

    # Core variables, do not alter, or assign directly
    
    
    
    MMAX=1 # The number of total bodies in the model. This variable is reassigned after the model.dat file is read.
    
        
    IMAX=180 # The max number of bodies in JPL's ephemerides. 
    
    MU_LENGTH_2=113
    
    ISPC=False


    LIST_I=[] #	Holds the class objects of list_bodies.
    
    LIST_EPH=[]
    LIST_EPH_IBC=[]

          
    
    
    def __init__(self, i_spyce_lib_location, i_cspice_lib_location, i_model_file_location): 
        
        SPYCE_LIB=i_spyce_lib_location
        CSPICE_LIB=i_cspice_lib_location
        model_file_location=i_model_file_location
        
        self.read_model_spyce(model_file_location)
        
        return
    
    def read_model_spyce(self, model_file):
        """
        
    
        Parameters
        ----------
        model_file : str
            DESCRIPTION.
    
        Returns
        -------
        None.
    
        """
        with open(model_file) as f:
            content = f.readlines()
        
        # Now that we know the length of model.dat file, we can define the variable MMAX, and use it to initialise other important variables.
        
        MMAX = len(content)
        
        i=0
        for line in content:
           new_body=spyce_list_bodies()
           new_body.set_ID(line)
        
        return
    
