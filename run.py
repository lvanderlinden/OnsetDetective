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
				plt.plot(aTkeo, color = blue[2])
				onset1 = OnsetDetective.onsetDetective.stimLockedOnset(a, plot = False)
				onset2 = OnsetDetective.onsetDetective.respLockedOnset(a, plot = False)
				#print onset
				
				plt.axvline(onset1, color = "red")
				plt.axvline(onset2, color = "red")
				plt.show()


