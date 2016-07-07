import pickle
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps
import copy

def calcAUC(normal, sick):
	normalCorrFlattened, sickCorrFlattened = flatteningCorr(normal, sick)
	normalCorrFlattened.sort()
	sickCorrFlattened.sort()
	diffCorrFlattened = normalCorrFlattened - sickCorrFlattened
	return simps(diffCorrFlattened, dx=1)
def flatteningCorr(normal, sick):
	sickCorr=np.corrcoef(sick)
	normalCorr=np.corrcoef(normal)
	numGene = sick.shape[0]
	sickCorrFlattened = np.zeros((numGene*numGene-numGene)/2, dtype=np.float32)
	normalCorrFlattened = np.zeros((numGene*numGene-numGene)/2, dtype=np.float32)
	itera=0
	for rawI in range(numGene):
		for rawJ in range(rawI+1,numGene):
			sickCorrFlattened[itera]=sickCorr[rawI][rawJ]
			normalCorrFlattened[itera]=normalCorr[rawI][rawJ]
			itera+=1
	return normalCorrFlattened, sickCorrFlattened


reducedSick=pickle.load(open('./prePickles/reducedSick.pickle','r'))
reducedNormal=pickle.load(open('./prePickles/reducedNormal.pickle','r'))
firstAUC = calcAUC(reducedNormal, reducedSick)

# randomly shuffle samples
total = np.concatenate((reducedSick, reducedNormal),axis=1)
labels = np.array([0 if i<60 else 1 for i in range(120)]).reshape((1,120))
total = np.concatenate((total, labels))
total = total.transpose()
np.random.shuffle(total)
aWithLabel = total[:60,:]
bWithLabel = total[60:,:]
# a = aWithLabel[:,:-1]
# b = bWithLabel[:,:-1]

acopy = copy.copy(aWithLabel)
bcopy = copy.copy(bWithLabel)
prevAUC = calcAUC(acopy[:,:-1], bcopy[:,:-1])
while True:
	oldAUC = calcAUC(aWithLabel[:,:-1], bWithLabel[:,:-1])
	for i in range(60):
		for j in range(60):
			# try swapping
			tmp = copy.copy(acopy[i])
			acopy[i] = bcopy[j]
			bcopy[j] = tmp
			# print calcAUC(acopy, bcopy)
			if calcAUC(acopy[:,:-1], bcopy[:,:-1]) > prevAUC:
				tmp = copy.copy(aWithLabel[i])
				aWithLabel[i] = bWithLabel[j]
				bWithLabel[j] = tmp
				acopy = copy.copy(aWithLabel)
				bcopy = copy.copy(bWithLabel)
				prevAUC = calcAUC(acopy[:,:-1], bcopy[:,:-1])
				print prevAUC, i, j
	newAUC = calcAUC(aWithLabel[:,:-1], bWithLabel[:,:-1])
	print 'oldAUC : {}'.format(oldAUC)
	print 'newAUC : {}'.format(newAUC)
	print
	if oldAUC == newAUC:
		break

print
print 'complete!!!'
print 'firstAUC : {}'.format(firstAUC)
print 'newAUC : {}'.format(newAUC)

rateList = np.array(aWithLabel[:,-1])
rate = rateList.mean()
print "Accuray Rate : {}".format(rate)

print calcAUC(reducedNormal, reducedSick)
