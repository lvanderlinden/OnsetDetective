#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: movWin.py

"""
DESCRIPTION:
Smooths logistic signal by applying a moving-window average. A 1D numpy array
containing the smoothed signal is returned.
"""

import numpy as np
from matplotlib import pyplot as plt


def movWin(aLog, winWidth):

	"""
	Returns a 1D array containing mov avg of the log signal.

	Arguments:
	aLog		--- 1D numpy array containing logistic signal.
	winWidth	--- width of the moving window in samples, int.

	Returns a 1D numpy containing moving-window average of the log signal.
	"""

	# Check whether window width is an int. Otherwise the program crashes.
	if type(winWidth) != int:
		raise ValueError, "The window width should be an int."

	# Create an empty array of the same size as the input array:
	aSmooth = np.zeros(aLog.size)

	# Loop through the input array:
	for i in range(winWidth/2, aLog.size-winWidth/2):
		t = aLog[i-winWidth/2:i+winWidth/2].mean()
		aSmooth[i] = t


	return aSmooth

