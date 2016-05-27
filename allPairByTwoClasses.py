# find all pair correlations by two classes (sick and normal).
# x-axis is sick, and y-axis is normal.

import pickle
import numpy as np
import matplotlib.pyplot as plt

genes=pickle.load(open('./prePickles/gExpressions2.pickle','r'))

sickAndNormal=np.hsplit(genes,2)
sick=sickAndNormal[0]
normal=sickAndNormal[1]

#test purpose for fast execution
sick=sick[:1000]
normal=normal[:1000]
###

sickCorr=np.corrcoef(sick)
normalCorr=np.corrcoef(normal)

numGene=sickCorr.shape[0]
sickCorrFlattened=[]
normalCorrFlattened=[]
for rawI in range(numGene):
	for rawJ in range(rawI+1,numGene):
		sickCorrFlattened.append(sickCorr[rawI][rawJ])
		normalCorrFlattened.append(normalCorr[rawI][rawJ])

pickle.dump(zip(sickCorrFlattened,normalCorrFlattened),open('./prePickles/sickAndNormalCorrFlattened.pickle','w'))
# plt.scatter(sickCorrFlattened,normalCorrFlattened)
# plt.show()
