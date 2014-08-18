#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: th2.py

"""
DESCRIPTION:
- Thresholds the smoothed signal.
- Determines the window belonging to the first sample that exceeded th2
- Determines the first sample within this window that exceeded th1

TODO:
merge aboveTh2 and belowTh2
"""

import numpy as np
from matplotlib import pyplot as plt

def aboveTh2(aSmooth, th2Val):

	"""
	Returns the index of the first sample that exceeded the mov avg threshold.

	Arguments:
	aSmooth	--- 1D numpy array containing mov avg.
    th2Val	--- threshold for the mov avg, float between 0 and 1.

	Returns:
	Index of the first sample that exceeded the mov-avg-signal threshold, int.
	"""

    # Check whether the threshold is indeed a float between 0 and 1:
	# TODO: exception -- moet helemaal niet meer doorgaan hier!
	if th2Val > 1 or th2Val < 0:
		raise ValueError, "th2 should be a float between 0 and 1."

	# Make sure the program doesn't crash if onset cannot be calculated:
	if len(np.where(aSmooth > th2Val)[0]) == 0:
		iTh2Exceeded = None
		print "Th2 was never exceeded. The onset is set to None.",
		return iTh2Exceeded

	iTh2Exceeded = int(np.where(aSmooth> th2Val)[0][0])
	
	return iTh2Exceeded

def belowTh2(aSmooth, th2Val):
	
	"""
	"""
	
	# Make sure the program doesn't crash if onset cannot be calculated:
	if len(np.where(aSmooth < th2Val)[0]) == 0:
		iBelow = None
		print "There are no samples smaller than th2. The onset is set to None.",
		return iBelow

	iBelow = int(np.where(aSmooth< th2Val)[0][0])
	
	return iBelow
	
def stimLocked(aLog, aSmooth, th2Val, winWidth, plot = False):

	"""
	Returns the onset of a given signal as detected by the algorithm.

	Arguments:
	aLog		--- 1D numpy array containing log signal.
	aSmooth 	--- 1D numpy array containing moving window average of the log 
					signal
    th2Val			--- threshold for the mov avg, float between 0 and 1
	winWidth	--- width of the moving window, int.

	Returns the onset of the signal (as sample), int (or None, if no onset was
	detected because the thresold(s) was/were never exceeded).
	"""

	# Determine the first sample where the smoothed signal exceeded th2
	

	iTh2Exceeded = aboveTh2(aSmooth.copy(), th2Val)

	# If th2 was never exceeded, return None:
	if iTh2Exceeded == None:
		onset = None
		return onset

	# Determine the window around the first sample that exceeded th2:
	iStartWin = iTh2Exceeded - winWidth/2 # first sample of the window slice
	iEndWin = iTh2Exceeded + winWidth/2 # last sample of the window slice

	# Determine the first sample within the window-slice for which th1 was
	# exceeded:
	iTh1Exceeded = int(np.where(aLog[iStartWin:iEndWin] == 1)[0][0])
	
	# Determine the index of this sample relative to the whole array:
	onset = iTh1Exceeded + iStartWin

	if plot:
		plt.subplot(212)
		plt.plot(aSmooth, color = 'orange')
		plt.axhline(th2Val, color = "orange")
		plt.axvline(iTh1Exceeded, color = "blue", label = "th1 exceeded")
		plt.axvline(iTh1Exceeded, color = "green", label = "th2 exceeded")
		plt.axvline(onset, color = "orange", label = "onset", linewidth = 2)
		plt.axvline(iStartWin, color = 'gray', linestyle = "--")
		plt.axvline(iEndWin, color = 'gray', linestyle = "--")
		plt.legend(loc='best', frameon=False)
		
	return onset


def respLocked(aLog, aSmooth, th2Val, winWidth, plot = False):

	"""
	Returns the onset of a given signal as detected by the algorithm.

	Arguments:
	aLog		--- 1D numpy array containing log signal.
	aSmooth 	--- 1D numpy array containing moving window average of the log 
					signal
    th2Val		--- threshold for the mov avg, float between 0 and 1
	winWidth	--- width of the moving window, int.

	Returns the onset of the signal (as sample), int (or None, if no onset was
	detected because the thresold(s) was/were never exceeded).
	"""

	# Determine the first sample where the smoothed signal exceeded th2
	# TODO: only th2 or also th1?
	firstSampleAboveTh2= aboveTh2(aSmooth, th2Val)
	if firstSampleAboveTh2 in ("None", None):
		onset = None
		return onset

	# Slice such that we look for a sample below the threshold only AFTER
	# a sample ABOVE th2 was detected:
	aSmoothSliced = aSmooth[firstSampleAboveTh2:]
	aLogSliced = aLog[firstSampleAboveTh2:]
	
	startVal = aSmoothSliced[0]
	th2Val = startVal - (startVal*.1)
	

	# Find first sample below th2:
	firstSampleBelowTh2= belowTh2(aSmoothSliced, th2Val)
	print "first sample below = ", firstSampleBelowTh2
	
	
	# If there was no sample below th2, return None:
	if firstSampleBelowTh2 == None:
		onset = None
		return onset

	# Determine the window around the first sample that exceeded th2:
	#iStartWin = firstSampleBelowTh2 - winWidth/2 # first sample of the window slice
	#iEndWin = firstSampleBelowTh2 + winWidth/2 # last sample of the window slice
	

	# Determine the first sample within the window-slice for which th1 was
	# exceeded:
	#firstSampleBelowTh1 = int(np.where(aLogSliced[iStartWin:iEndWin] == 0)[0][0])
	# Determine the index of this sample relative to the whole array:
	#onset = firstSampleAboveTh2 + iStartWin + firstSampleBelowTh1
	onset = firstSampleBelowTh2+firstSampleAboveTh2

	if plot:
		plt.subplot(312)
		plt.plot(aLogSliced, color = "yellow")
		plt.plot(aSmoothSliced, color = 'orange')
		plt.axhline(th2Val, color = "blue")
		plt.axhline(startVal, color = "red", linewidth = 2)
		plt.axvline(firstSampleBelowTh2, color = "green", label = "below th2")
		#plt.axvline(firstSampleBelowTh1 + iStartWin, color = "red", label = "below th1")
		#plt.axvline(iStartWin, color = "gray")
		#plt.axvline(iEndWin, color = "gray")
		#plt.axvline(onset, color = "orange", label = "onset", linewidth = 2)
		plt.legend()
		plt.xticks([])

	return onset

