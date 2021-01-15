#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:11:07 2021

@author: mtd
"""

class Domain:
    def __init__(self):
        self.nR=[] #number of reaches
        self.xkm=[] #reach midpoint distance downstream [m]
        self.L=[]  #reach lengths, [m]
        self.nt=[] #number of overpasses
        self.t=[] #time, [days]
        self.dt=[] #time delta between successive overpasses, [seconds]