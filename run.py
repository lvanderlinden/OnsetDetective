#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Filename: run.py

import numpy as np
import os
from matplotlib import pyplot as plt
from exparser.TangoPalette import *

# Import onsetDetective modules:
import OnsetDetective.onsetDetective
import OnsetDetective.tkeo

# Walk through files
src = "/home/lotje/Documents/Research assistent Marseille/Raw data/data exp2"
for pp in os.listdir(src):
	ppPath = os.path.join(src, pp)
	for trial in os.listdir(ppPath):
		trialPath = os.path.join(ppPath, trial)
		for session in os.listdir(trialPath):
			sessionPath = os.path.join(trialPath, session)
			for f in os.listdir(sessionPath):
				fPath = os.path.join(sessionPath, f)
				
				if not "EMG1_" in f:
					continue

				a = np.fromfile(fPath, dtype = np.float32)
				aTkeo = OnsetDetective.tkeo.tkeo(a)
				aTkeo2 = OnsetDetective.tkeo.tkeo2(a)
				#plt.plot(a, color = blue[1], alpha = .5)
				plt.plot(aTkeo, color = blue[2])
				plt.plot(aTkeo2, color = red[2])
				onset = OnsetDetective.onsetDetective.onset(a)
				#print onset
				plt.axvline(onset, color = "red")
				plt.show()


