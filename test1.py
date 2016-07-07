import pickle
import matplotlib.pyplot as plt
import gc
import numpy as np
from scipy.integrate import simps

a=pickle.load(open('./prePickles/reducedSick.pickle','r'))
b=pickle.load(open('./prePickles/reducedNormal.pickle','r'))

sickCorr=np.corrcoef(a)
normalCorr=np.corrcoef(b)
numGene = 2000
sickCorrFlattened = np.zeros((numGene*numGene-numGene)/2,dtype=np.float32)
normalCorrFlattened = np.zeros((numGene*numGene-numGene)/2,dtype=np.float32)
itera=0
for rawI in range(numGene):
	for rawJ in range(rawI+1,numGene):
		sickCorrFlattened[itera]=sickCorr[rawI][rawJ]
		normalCorrFlattened[itera]=normalCorr[rawI][rawJ]
		itera+=1

sickCorrFlattened.sort()
normalCorrFlattened.sort()
diffCorrFlattened = normalCorrFlattened - sickCorrFlattened

print simps(sickCorrFlattened, dx=1)
print simps(normalCorrFlattened, dx=1)
print simps(diffCorrFlattened, dx=1)
print

ab = np.concatenate((a,b),axis=1)
ab = ab.transpose()
np.random.shuffle(ab)
ab = ab.transpose()
a = ab[:,:60]
b = ab[:,60:]

sickCorr=np.corrcoef(a)
normalCorr=np.corrcoef(b)
numGene = 2000
sickCorrFlattened = np.zeros((numGene*numGene-numGene)/2,dtype=np.float32)
normalCorrFlattened = np.zeros((numGene*numGene-numGene)/2,dtype=np.float32)
itera=0
for rawI in range(numGene):
	for rawJ in range(rawI+1,numGene):
		sickCorrFlattened[itera]=sickCorr[rawI][rawJ]
		normalCorrFlattened[itera]=normalCorr[rawI][rawJ]
		itera+=1

sickCorrFlattened.sort()
normalCorrFlattened.sort()
diffCorrFlattened = normalCorrFlattened - sickCorrFlattened

print simps(sickCorrFlattened, dx=1)
print simps(normalCorrFlattened, dx=1)
print simps(diffCorrFlattened, dx=1)

print a.shape