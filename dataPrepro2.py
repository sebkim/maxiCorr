# preprocessing data second phase (gExpressions2.pickle, and gNames2.pickle)
# it eliminates genes if RMA values of more than 90% of them are less than 6.

import pickle
import numpy as np

def notSigExpressed(aList, numCell, prop, magicN):
	count=0
	for i in aList:
		if i<magicN:
			count+=1
	if count>numCell*prop:
		return True
	else:
		return False

gExpressions=pickle.load(open('./prePickles/gExpressions.pickle','r'))
gNames=pickle.load(open('./prePickles/gNames.pickle','r'))

numCell=gExpressions.shape[1]
whichRowFiltered=[]
for rawI, g in enumerate(gExpressions):
	if notSigExpressed(g,numCell,0.9,6):
		whichRowFiltered.append(rawI)

whichRowNotFiltered=set(range(gExpressions.shape[0]))
whichRowNotFiltered-=set(whichRowFiltered)
whichRowNotFiltered=list(whichRowNotFiltered)
whichRowNotFiltered.sort()

gExpressions2=gExpressions[whichRowNotFiltered]
gNames2=gNames[whichRowNotFiltered]

pickle.dump(gExpressions2,open('./prePickles/gExpressions2.pickle','w'))
pickle.dump(gNames2,open('./prePickles/gNames2.pickle','w'))
