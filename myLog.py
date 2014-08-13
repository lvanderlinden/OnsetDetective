#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: myLog.py

"""
DESCRIPTION:
A threshold is applied to the TKEO signal, which retruns a logistic signal with
the value 'True' if the threshold is exceeded, and 'False' if the threshold is
not exceeded. A 1D numpy containing this logistic signal is returned.
Note that in Python the values 'True' and 'False' are interchangable with '1'
and '0'.
"""

# Define functions:

def getLog(a, th1):

	"""
	Returns the logistic signal after applying a threshold to the tkeo signal.

	Arguments:
	a	--- 1D numpy array containing tkeo per sample.
	th	--- Threshold for the tkeo.

	Returns:
	1D numpy array containing logistic signal instead of tkeo.
	"""

	_a = a > th1

	return _a

