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

def stimLockedOnset(a, k = 12, winWidth = 50, th2Val = .35,  iStartBaseline = 0, \
	iEndBaseline = 300, convertToTkeo=True, plot = False):
	
	"""
	Applies all steps of the stim-locked algorithm to determine onset (in samples)

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
	convertToTkeo	--- Set to False if the input array is already in the TKEO
						domain.
	plot			--- Boolean indicating whether or not to show some debug
						plots.

	Returns the stim-locked onset of the signal (as sample), int 
	(or None, if no onset was 
	detected because the thresold(s) was/were never exceeded).
	"""
	
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

	# Determines onset by applying a second threshold:
	onset = th2.onsetSample(aLog, aSmooth, th2Val, winWidth, plot = plot)
	
	return onset


def respLockedOnset(a, k = 12, winWidth = 100, th2Val = .35,  iStartBaseline = 0, \
	iEndBaseline = 300, convertToTkeo=True, plot = False):
	
	"""
	Applies all steps of the response-locked algorithm to determine onset (in samples)

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
	convertToTkeo	--- Set to False if the input array is already in the TKEO
						domain.
	plot			--- Boolean indicating whether or not to show some debug
						plots.


	Returns the onset of the signal (as sample), int (or None, if no onset was 
	detected because the thresold(s) was/were never exceeded).
	"""
	
	# Convert raw input signal to tkeo domain:
	if convertToTkeo:
		aTkeo = tkeo.tkeo2(a)
	else:
		aTkeo = a

	## Apply first th to obtain logistic signal:
	aLog = th1.applyTh1(aTkeo, k = k, iStartBaseline = iStartBaseline, \
		iEndBaseline = iEndBaseline, plot = plot)

	# Smooth logistic signal
	aSmooth = movWin.movWin(aLog,winWidth)
	maxVal = max(aSmooth)
	# Determine the sample that exceeded th2
	firstSampleAboveTh2= th2.aboveTh2(aSmooth, th2Val, plot = plot)
	plt.axhline(maxVal)
	plt.axhline(maxVal*.85)
	
	# Slice such that we look for a sample below the threshold only AFTER
	# a sample ABOVE th2 was detected:
	aSmoothSliced = aSmooth[firstSampleAboveTh2:]
	
	# Find first sample below th2:
	firstSampleBelowTh2 = th2.belowTh2(aSmoothSliced, th2Val)
	# Relative to unsliced smoothed signal:
	firstSampleBelowTh2 = firstSampleBelowTh2 + firstSampleAboveTh2
	
	return firstSampleBelowTh2

