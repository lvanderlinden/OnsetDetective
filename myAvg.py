#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: myAvg.py

"""
DESCRIPTION:
This module calculates a moving window average for every sample of the logistic
signal. A 1D array with the smoothed signal is returned.
"""

# Import built-in Python modules:
import numpy as np

# Define functions:

def getAvg(a, window):

	"""
	Returns a 1D array containing mov avg of the log signal.

	Arguments:
	a		--- 1D numpy array containing logistic signal.
	window	--- width of the moving window, int.

	Returns:
	1D numpy containing moving-window average of the log signal.
	"""

	# Check whether window width is an int. Otherwise the program crashes.
	if type(window) != int:
		raise ValueError, "The window width should be an int."

	# Create an empty array of the same size as the input array:
	_a = np.zeros(a.size)

	# Loop through the input array:
	for i in range(window/2, a.size-window/2):
		t = a[i-window/2:i+window/2].mean()
		_a[i] = t

	return _a

