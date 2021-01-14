#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:49:40 2021

@author: mtd
"""

class ReachObservations:
    def __init__(self):
        self.D=Domain()
      
    
    
    def ReadObs(self,fname):
        # Read observation file in MetroMan text format
        
        from numpy import array,diff,ones,reshape,empty
    
        fid=open(fname,"r")
        infile=fid.readlines()
        
        # read domain
        self.D.nR=eval(infile[1])
        buf=infile[3]; buf=buf.split(); self.D.xkm=array(buf,float)
        buf=infile[5]; buf=buf.split(); self.D.L=array(buf,float)
        self.D.nt=eval(infile[7]);
        buf=infile[9]; buf=buf.split(); self.D.t=array([buf],float)
        
        self.D.dt=reshape(diff(self.D.t).T*86400 * ones((1,self.D.nR)),(self.D.nR*(self.D.nt-1),1))
        
        #specify variable sizes
        self.h=empty(  (self.D.nR,self.D.nt) ) #water surface elevation (wse), [m]
        self.h0=empty( (self.D.nR,1)  ) #initial wse, [m]
        self.S=empty(  (self.D.nR,self.D.nt) ) #water surface slope, [-]
        self.w=empty(  (self.D.nR,self.D.nt) ) #river top width, [m]
        self.hv=empty( (self.D.nR*self.D.nt,1) ) #reshaped version of h
        self.Sv=empty( (self.D.nR*self.D.nt,1) ) #reshaped version of S
        self.wv=empty( (self.D.nR*self.D.nt,1) ) #reshaped version of w
        self.sigh=[] #wse uncertainty standard deviation [m]
        self.sigS=[] #slope uncertainty standard deviation [-]
        self.sigW=[] #width uncertainty standard deviation [m]
        self.dA=empty( (self.D.nR,self.D.nt) ) #cross-sectional area anomaly [m^2]
        self.dAv=empty( (self.D.nR*(self.D.nt-1)) ) #reshaped version of dA
        self.hmin=empty( (self.D.nR,1)  ) #minimum wse, [m]
        self.A0Shift=empty( (self.D.nR,1)  ) #difference in A0 between inversion window and all of timeseries
        
        #%% read observations   
        for i in range(0,self.D.nR):
            buf=infile[i+11]; buf=buf.split(); self.h[i,:]=array(buf,float)
        buf=infile[12+self.D.nR]; buf=buf.split(); self.h0=array([buf],float)
        for i in range(0,self.D.nR):
            buf=infile[14+self.D.nR+i]; buf=buf.split(); self.S[i,:]=array(buf,float)/1e5; #convert cm/km -> m/m
        for i in range(0,self.D.nR):
            buf=infile[15+self.D.nR*2+i]; buf=buf.split(); self.w[i,:]=array(buf,float)
        self.sigS=eval(infile[16+self.D.nR*3])/1e5; #convert cm/km -> m/m
        self.sigh=eval(infile[18+self.D.nR*3])/1e2; #convert cm -> m
        self.sigw=eval(infile[20+self.D.nR*3] )
             
        
        #%%
        fid.close()   
    
    def GetVectorObs(self):
        
        from numpy import reshape
        
        #%% create resahepd versions of observations
        self.hv=reshape(self.h, (self.D.nR*self.D.nt,1) )
        self.Sv=reshape(self.S, (self.D.nR*self.D.nt,1) )
        self.wv=reshape(self.w, (self.D.nR*self.D.nt,1) )

class Domain:
    def __init__(self):
        self.nR=[] #number of reaches
        self.xkm=[] #reach midpoint distance downstream [m]
        self.L=[]  #reach lengths, [m]
        self.nt=[] #number of overpasses
        self.t=[] #time, [days]
        self.dt=[] #time delta between successive overpasses, [seconds]