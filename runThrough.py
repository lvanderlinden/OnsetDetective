#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: runAlgorithm.py

# Import built-in Python modules:
import numpy as np
from matplotlib import pyplot as plt

# Import our own modules:
import myTkeo, myOnset, myAvg, myLog
import os

# Define constant variables:

# Free parameters of the algorithm:
k = 12
th2 = .35
w = 100

# End of the baseline:
blEnd = 300

src = "/home/lotje/Documents/Research assistent Marseille/Raw data/EMG signals"

for muscle in os.listdir(src):
	mPath = os.path.join(src, muscle)
	
	for trial in os.listdir(mPath):
		filePath = os.path.join(mPath, trial)
		
		#if not 'mj_260310' in trial:
			#continue
		
		#if not '_S2_E28' in trial:
			#continue
		
		print 'trial = ', filePath


		# Apply all steps of the algorithm:

		# Convert input file to numpy array:
		raw = np.fromfile(filePath, dtype = np.float32)

		# Convert raw input signal to tkeo domain:
		tkeo = myTkeo.getTkeo(raw)

		# Get a baseline slice:
		bl = tkeo[0:blEnd]

		# Get the mean and sd of the baseline:
		m = np.mean(bl)
		sd = np.std(bl)

		# Calculate first threshold:
		th1 = m + sd*k

		# Get logistic signal:
		log = myLog.getLog(tkeo, th1)

		# Get mov avg:
		avg = myAvg.getAvg(log, w)

		# Determine the onset (in samples):
		onset = myOnset.getOnset(log, avg, th2, w)

		# Plot everything:

		# Set font
		plt.rc("font", family="arial")
		plt.rc("font", size=12)

		# Create figure:
		fig = plt.figure(figsize = (10,10))

		# Add main title:
		plt.suptitle("emg onset detection")

		# Make subplots:

		# Add subplot:
		plt.subplot(311)
		# Add title:
		plt.title("raw signal is converted to tkeo domain")
		# Plot raw data:
		plt.plot(raw, color = "#729fcf",linewidth = 1.5, alpha = .3)
		# Plot tkeo:
		plt.plot(tkeo, color = "#3465a4",linewidth = 1.5)
		# Plot baseline:
		plt.axvline(blEnd, color = "#555753", linewidth = 1.5, linestyle = "--")
		# Plot onset:
		plt.axvline(onset, color = "#8ae234", linewidth = 4)
		# Hide x axis (because it's identical for all subplots):
		plt.xticks([])
		# Add legend:
		plt.legend(["raw", "tkeo", "baseline", "emg onset"])

		# Add subplot:
		plt.subplot(312)

		# Set ylim such that the tkeo fits nicely:
		plt.ylim([min(tkeo), max(tkeo)])
		# Add title:
		plt.title("threshold1 is applied to tkeo signal")
		# Plot logistic signal:
		plt.plot(log, color = "#fce94f",linewidth = 1.5)
		# Plot tkeo:
		plt.plot(tkeo, color = "#3465a4",linewidth = 1.5)
		# Plot first threshold:
		plt.axhline(th1, color = "#ef2929",linewidth = 1.5)
		# Plot baseline:
		plt.axvline(blEnd, color = "#555753", linewidth = 1.5, linestyle = "--")
		# Plot onset:
		plt.axvline(onset, color = "#8ae234", linewidth = 4)
		# Hide x axis:
		plt.xticks([])
		# Add legend:
		plt.legend(["log", "tkeo", "threshold1", "baseline", "emg onset"])

		# Add subplot:
		plt.subplot(313)
		# Add title:
		plt.title("threshold2 is applied to moving-window average")
		# Plot logistic signal:
		plt.plot(log, color = "#fce94f",linewidth = 1.5)
		# Plot moving-window average:
		plt.plot(avg, color = "#f57900",linewidth = 1.5)
		# Plot second threshold:
		plt.axhline(th2, color = "#ef2929",linewidth = 1.5)
		# Plot baseline:
		plt.axvline(blEnd, color = "#555753", linewidth = 1.5, linestyle = "--")
		# Plot onset:
		plt.axvline(onset, color = "#8ae234", linewidth = 4)
		# Plot legend:
		plt.legend(["log", "moving avg", "threshold2", "baseline", "emg onset"])

		# Show the plot:
		plt.show()






