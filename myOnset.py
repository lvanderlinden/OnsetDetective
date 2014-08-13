#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: myOnset.py

"""
DESCRIPTION:
This module executes the final step of the algorithm: the moving window average
is thresholded. The first sample within this window that exceeded the tkeo
threshold (i.e. the first '1' in the log signal) is taken as the signal onset.
"""

# Import built-in Python modules:
import numpy as np

# Define functions:

def firstWindow(a, th):

	"""
	Returns the index of the first sample that exceeded the mov avg threshold.

	Arguments:
	a		--- 1D numpy array containing mov avg.
    th		--- threshold for the mov avg, float between 0 and 1.

	Returns:
	Index of the first sample that exceeded the mov-avg-signal threshold, int.
	"""

    # Check whether the threshold is indeed a float between 0 and 1:
	# TODO: exception -- moet helemaal niet meer doorgaan hier!
	if th > 1 or th < 0:
		raise ValueError, "th2 should be a float between 0 and 1."

	# Make sure the program doesn't crash if onset cannot be calculated:
	if len(np.where(a > th)[0]) == 0:
		firstWin = None
		print "The moving-window-average signal never exceeded the threshold. The onset is set to None.",
		return firstWin

	firstWin = int(np.where(a> th)[0][0])

	return firstWin


def getOnset(log, avg, th, window):

	"""
	Returns the onset of a given signal as detected by the algorithm.

	More specifically, this function determines the index of the first sample,
	within the first window exceeding t2, that exceeded t1.

	Arguments:
	log		--- 1D numpy array containing log signal.
	avg		--- 1D numpy array containing moving window average.
    th		--- threshold for the mov avg, float between 0 and 1
	window	--- width of the moving window, int.

	Returns:
	Onset of the signal (as sample), int.
	"""

	firstWin = firstWindow(avg.copy(), th)

	# If the mov avg signal never exceeded the threshold, absOnset is set to 0:
	if firstWin == None:
		onset = None
		return onset

	# Get the start and end of the window that first exceeded the threshold:
	minWin = firstWin - window/2 # first sample within the window
	maxWin = firstWin + window/2 # last sample within the window

	# Index within window:
	firstTrue = int(np.where(log[minWin:maxWin] == 1)[0][0])

	# Index in whole array:
	onset = firstTrue + minWin

	return onset



