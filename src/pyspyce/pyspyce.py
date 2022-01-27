from pyspyce.spyce_core import spyce_core
from ctypes import *
from spiceypy import *
from .list_bodies import *
from .error_codes import *
from .state import * 
from .cspice_supp import *
from .spiceypy_supp import *
from .external.rk89 import *
from .system_def import *



class pyspyce:

    _spycecoreObject=None

    def __init__(self, data_directory, model=[0]):
        self._spycecoreObject=spyce_core(data_directory, model)
        return 
    
    def set_barycentre(self, ibc):
        self._spycecoreObject._system_def.set_barycentre(ibc)
        return
    
    def get_barycentre(self):
        return self._spycecoreObject._system_def.get_barycentre()
    
    def get_referenceframe(self):
        return self._spycecoreObject._REF_FRAME
    
    def set_referenceframe(self, frame):
        self._spycecoreObject._REF_FRAME=frame
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
        return get_state_wrt_ibc(self._spycecoreObject, time, body_id)
    
    def get_mu(self, bodyid):
        return get_mu(self._spycecoreObject, bodyid)
    
    def get_mu_m3(self, bodyid):
        return get_mu_m3(self._spycecoreObject, bodyid)
    

    def init_2body_system(self, primary_body, secondary_body=-999):
        self._spycecoreObject._system_def=system_def(primary_body, secondary_body)
        
    def init_rtbp_system(self, primary_body, secondary_body):
        self._spycecoreObject._system_def=system_def(primary_body, secondary_body, True)

        
    def rk89(self,time, vstate, dt, external_module, dim):
        return rk89_internal(time, vstate, dt, external_module, dim)