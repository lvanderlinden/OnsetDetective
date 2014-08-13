#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: th2.py

"""
DESCRIPTION:
- Thresholds the smoothed signal.
- Determines the window belonging to the first sample that exceeded th2
- Determines the first sample within this window that exceeded th1
"""

import numpy as np

def th2(aSmooth, th2Val):

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
		print "The moving-window-average signal never exceeded the threshold. The onset is set to None.",
		return iTh2Exceeded

	iTh2Exceeded = int(np.where(aSmooth> th2Val)[0][0])
	
	#from matplotlib import pyplot as plt
	#plt.axhline(th2Val, color = 'green', linewidth = 3)

	return iTh2Exceeded


def onsetSample(aLog, aSmooth, th2Val, winWidth):

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
	
	iTh2Exceeded = th2(aSmooth.copy(), th2Val)

	#from matplotlib import pyplot as plt
	#plt.axvline(iTh2Exceeded,color = 'green', linewidth = 3)
	#plt.show()


	# If th2 was never exceeded, return None:
	if iTh2Exceeded == None:
		onset = None
		return onset

	# Determine the window around the first sample that exceeded th2:
	iStartWin = iTh2Exceeded - winWidth/2 # first sample of the window slice
	iEndWin = iTh2Exceeded + winWidth/2 # last sample of the window slice

	# Determine the first sample within the window-slice for which th1 was
	# exceeded:
	iTh2Exceeded = int(np.where(aLog[iStartWin:iEndWin] == 1)[0][0])

	# Determine the index of this sample relative to the whole array:
	onset = iTh2Exceeded + iStartWin

	return onset



