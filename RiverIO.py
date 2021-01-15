#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 13:09:29 2021

@author: mtd
"""

from numpy import array,diff,ones,reshape,empty    

class RiverIO:
    def __init__(self,IOtype,fname):
        self.type=IOtype
        self.fname=fname
        
        if self.type == 'MetroManTxt':
            self.ReadMetroMan()
        else:
            print("RiverIO: Undefined observation data specified. Data not read.")
        
    
    
    def ReadMetroMan(self):
        # Read observation file in MetroMan text format        
        fid=open(self.fname,"r")
        infile=fid.readlines()
        
        # read domain
        nR=eval(infile[1])
        buf=infile[3]; buf=buf.split(); xkm=array(buf,float)
        buf=infile[5]; buf=buf.split(); L=array(buf,float)
        nt=eval(infile[7]);
        buf=infile[9]; buf=buf.split(); t=array([buf],float)
        
        dt=reshape(diff(t).T*86400 * ones((1,nR)),(nR*(nt-1),1))
        
        #specify variable sizes
        h=empty(  (nR,nt) ) #water surface elevation (wse), [m]
        # self.h0=empty( (self.D.nR,1)  ) #initial wse, [m]
        # self.S=empty(  (self.D.nR,self.D.nt) ) #water surface slope, [-]
        # self.w=empty(  (self.D.nR,self.D.nt) ) #river top width, [m]
        # self.hv=empty( (self.D.nR*self.D.nt,1) ) #reshaped version of h
        # self.Sv=empty( (self.D.nR*self.D.nt,1) ) #reshaped version of S
        # self.wv=empty( (self.D.nR*self.D.nt,1) ) #reshaped version of w
        # self.sigh=[] #wse uncertainty standard deviation [m]
        # self.sigS=[] #slope uncertainty standard deviation [-]
        # self.sigW=[] #width uncertainty standard deviation [m]
        # self.dA=empty( (self.D.nR,self.D.nt) ) #cross-sectional area anomaly [m^2]
        # self.dAv=empty( (self.D.nR*(self.D.nt-1)) ) #reshaped version of dA
        # self.hmin=empty( (self.D.nR,1)  ) #minimum wse, [m]
        # self.A0Shift=empty( (self.D.nR,1)  ) #difference in A0 between inversion window and all of timeseries
        
        #%% read observations   
        for i in range(0,nR):
            buf=infile[i+11]; buf=buf.split(); h[i,:]=array(buf,float)
        # buf=infile[12+self.D.nR]; buf=buf.split(); self.h0=array([buf],float)
        # for i in range(0,self.D.nR):
        #     buf=infile[14+self.D.nR+i]; buf=buf.split(); self.S[i,:]=array(buf,float)/1e5; #convert cm/km -> m/m
        # for i in range(0,self.D.nR):
        #     buf=infile[15+self.D.nR*2+i]; buf=buf.split(); self.w[i,:]=array(buf,float)
        # self.sigS=eval(infile[16+self.D.nR*3])/1e5; #convert cm/km -> m/m
        # self.sigh=eval(infile[18+self.D.nR*3])/1e2; #convert cm -> m
        # self.sigw=eval(infile[20+self.D.nR*3] )
             
        
        #%%
        fid.close()   
        
        # smush into a dictionary
        self.data={
            "nR": nR,
            "xkm": xkm,
            "L": L, 
            "nt": nt,
            "t":t,
            "dt": dt,
            "h": h}