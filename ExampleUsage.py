#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:45:09 2021

@author: mtd
"""

from ReachObservations import ReachObservations

obs=ReachObservations()
obs.ReadObs('SWOTobs.txt')
obs.GetVectorObs()