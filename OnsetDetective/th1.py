#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: th1.py

"""
DESCRIPTION:
A threshold is applied to the TKEO signal, which retruns a logistic signal with
the value 'True' (i.e. 1)  if the threshold is exceeded, and 'False' (i.e. 0)
if the threshold is not exceeded.
"""

import numpy as np

def getTh1Val(aTkeo, k, iStartBaseline, iEndBaseline):
	
	"""
	Determines the threshold for the TKEO signal.
	
	Arguments:
	aTkeo			--- 1D numpy array containing tkeo per sample.
	k				--- Multiplier of the SD
	iStartBaseline	--- Start baseline period (as sample, integer)
	iEndBaseline	--- End baseline period (as sample, integer)
	
	Returns the threshold for the TKEO signal (float)
	"""
	
	# Determine a baseline slice:
	baselineSlice = aTkeo[iStartBaseline:iEndBaseline]

	# Get the mean and sd of the baseline:
	m = np.mean(baselineSlice)
	sd = np.std(baselineSlice)

	# Calculate first threshold:
	th1Val = m + sd*k
	
	return th1Val

def applyTh1(aTkeo, k, iStartBaseline, iEndBaseline):

	"""
	Returns the logistic signal after applying a threshold to the tkeo signal.

	Arguments:
	aTkeo			--- 1D numpy array containing tkeo per sample.
	k				--- Multiplier of the SD
	iStartBaseline	--- Start baseline period (as sample, integer)
	iEndBaseline	--- End baseline period (as sample, integer)

	Returns a 1D numpy array containing logistic signal
	"""

	# Determine the threshold:
	th1Val = getTh1Val(aTkeo, k, iStartBaseline, iEndBaseline)

	aLog = aTkeo > th1Val

	#from matplotlib import pyplot as plt
	#plt.plot(aLog, color = 'yellow', alpha = .5)
	#plt.plot(aTkeo)
	#plt.axhline(th1Val, color = 'red')
	##plt.show()

	return aLog

