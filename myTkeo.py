#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: myTkeo.py

"""
DESCRIPTION:
This module applies a Teager-Kaiser Energy operation to the raw emg signal and
returns a 1D numpy array containing tkeo's per sample.
"""

# Import built-in Python modules:

import numpy as np


# Define functions:

def getTkeo(a):

	"""
	Calculates the TKEO of a given recording.

	Arguments:
	a 			--- 1D numpy array.

	Returns:
	1D numpy array containing the tkeo per sample
	"""

	# Create two temporary arrays of equal length, shifted 1 sample to the right
	# and left and squared:
	i = a[1:-1]*a[1:-1]
	j = a[2:]*a[:-2]

	# Calculate the difference between the two temporary arrays:
	_a = i-j

	return _a
