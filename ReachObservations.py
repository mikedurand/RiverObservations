#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:49:40 2021

@author: mtd
"""

from numpy import reshape  

class ReachObservations:    
        
    def __init__(self,D,RiverData):
        # assign data from input dictionary
        self.h=RiverData["h"]        
        
        # et al.
        self.GetVectorObs(D)
    

    
    def GetVectorObs(self,D):    
        
        #%% create resahepd versions of observations
        self.hv=reshape(self.h, (D.nR*D.nt,1) )
        # self.Sv=reshape(self.S, (D.nR*D.nt,1) )
        # self.wv=reshape(self.w, (D.nR*D.nt,1) )

  