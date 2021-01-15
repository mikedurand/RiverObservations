#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:45:09 2021

@author: mtd
"""

from ReachObservations import ReachObservations
from RiverIO import RiverIO
from Domain import Domain

IO=RiverIO('MetroManTxt','SWOTobs.txt')
D=Domain(IO.data)

obs=ReachObservations(D,IO.data)
