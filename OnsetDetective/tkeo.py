#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: tkeo.py

"""
DESCRIPTION:
This module applies a Teager-Kaiser Energy operation to the raw signal and
returns a 1D numpy array containing tkeo's per sample.
"""

import numpy as np

def tkeo(a):

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
	aTkeo = i-j

	return aTkeo

def tkeo2(a):

	"""
	Calculates the TKEO of a given recording.

	Arguments:
	a 			--- 1D numpy array.

	Returns:
	1D numpy array containing the tkeo per sample
	"""

	# Create two temporary arrays of equal length, shifted 1 sample to the right
	# and left and squared:
	
	l = 1
	p = 2
	q = 0
	s = 3
	
	aTkeo = a[l:-p]*a[p:-l]-a[q:-s]*a[s:]

	return aTkeo


