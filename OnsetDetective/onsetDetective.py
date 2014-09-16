#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: onsetDetective.py

"""
Note the free parameters!!
"""
from matplotlib import pyplot as plt
import numpy as np

# Import OnsetDetective modules:
import tkeo, th1, movWin, th2

def onset(a, method, k = 1500, winWidth = 100, th2Val = .35, th2PercStart = .1,\
	iStartBaseline = 0, \
	iEndBaseline = 300, convertToTkeo=True, plot = False):
	
	"""
	Applies all steps of the stim-locked algorithm to determine onset (in samples)

	Arguments: 
	a				--- 1D numpy array containing raw signal
	method			--- {"stim-locked", "resp-locked"}, onset-detection method
	
	Keyword arguments:
	k 				--- Multiplier for the SD of the baseline, to determine 
						threhsold 1. (Default = 12)
	w 				---	Width of the moving window to smooth the logistic signal, 
						in samples (int). (Default = 100)
	th2Val 			--- Threshold for the smoothed signal (float between 0 and 1). 
						(Default = 0.35)
	iStartBaseline	--- Index of the first sample of the baseline period (int)
	iEndBaseline	--- Index pf the last sample of the baseline period (int)
	convertToTkeo	--- Set to False if the input array is already in the TKEO
						domain.
	plot			--- Boolean indicating whether or not to show some debug
						plots.

	Returns the stim-locked onset of the signal (as sample), int 
	(or None, if no onset was 
	detected because the thresold(s) was/were never exceeded).
	"""
	
	if plot:
		fig = plt.figure()
		plt.subplots_adjust(hspace = 0)

	
	# Convert raw input signal to tkeo domain:
	if convertToTkeo:
		aTkeo = tkeo.tkeo2(a)
	else:
		aTkeo = a

	# Apply first th to obtain logistic signal:
	aLog = th1.applyTh1(aTkeo, k = k, iStartBaseline = iStartBaseline, \
		iEndBaseline = iEndBaseline, plot = plot)

	# Smooth logistic signal
	aSmooth = movWin.movWin(aLog,winWidth)

	if method == "stim-locked":
		onset = th2.stimLocked(aLog, aSmooth, th2Val, winWidth, plot = plot)

	elif method == "resp-locked":
		onset = th2.respLocked(aLog, aSmooth, th2Val, winWidth, \
			th2PercStart = th2PercStart, plot = plot)

	return onset
