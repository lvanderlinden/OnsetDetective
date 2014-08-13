#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: run.py

"""
Note the free parameters!!
"""

import numpy as np

# Import OnsetDetective modules:
import tkeo, th1, movWin, th2

def onset(a, k = 12, winWidth = 100, th2Val = .35,  iStartBaseline = 0, \
	iEndBaseline = 300):
	
	"""
	Applies all steps of the algorithm to determine onset (in samples)

	Arguments: 
	a				--- 1D numpy array containing raw signal
	
	Keyword arguments:
	k 				--- Multiplier for the SD of the baseline, to determine 
						threhsold 1. (Default = 12)
	w 				---	Width of the moving window to smooth the logistic signal, 
						in samples (int). (Default = 100)
	th2Val 			--- Threshold for the smoothed signal (float between 0 and 1). 
						(Default = 0.35)
	iStartBaseline	--- Index of the first sample of the baseline period (int)
	iEndBaseline	--- Index pf the last sample of the baseline period (int)

	Returns the onset of the signal (as sample), int (or None, if no onset was 
	detected because the thresold(s) was/were never exceeded).
	"""
	
	# Convert raw input signal to tkeo domain:
	aTkeo = tkeo.tkeo(a)

	# Apply first th to obtain logistic signal:
	aLog = th1.applyTh1(aTkeo, k = k, iStartBaseline = iStartBaseline, \
		iEndBaseline = iEndBaseline)

	# Smooth logistic signal
	aSmooth = movWin.movWin(aLog,winWidth)

	# Determines onset by applying a second threshold:
	onset = th2.onsetSample(aLog, aSmooth, th2Val, winWidth)
	
	return onset

