# find all pair correlations by two classes (sick and normal).
# x-axis is sick, and y-axis is normal.
# it outputs sickAndNormalCorrFlattened.pickle and genePairNames.pickle, genePairIndnum.pickle .

import pickle
import numpy as np
import matplotlib.pyplot as plt

genes=pickle.load(open('./prePickles/gExpressions2.pickle','r'))
geneNames=pickle.load(open('./prePickles/gNames2.pickle','r'))

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
genePairNames=[]
genePairIndnum=[]
for rawI in range(numGene):
	for rawJ in range(rawI+1,numGene):
		sickCorrFlattened.append(sickCorr[rawI][rawJ])
		normalCorrFlattened.append(normalCorr[rawI][rawJ])
		genePairNames.append((geneNames[rawI],geneNames[rawJ]))
		genePairIndnum.append((rawI,rawJ))

pickle.dump(zip(sickCorrFlattened,normalCorrFlattened),open('./prePickles/sickAndNormalCorrFlattened.pickle','w'))
pickle.dump(genePairNames,open('./prePickles/genePairNames.pickle','w'))
pickle.dump(genePairIndnum,open('./prePickles/genePairIndnum.pickle','w'))

# plt.scatter(sickCorrFlattened,normalCorrFlattened)
# plt.show()

# a=pickle.load(open('./prePickles/sickAndNormalCorrFlattened.pickle','r'))
# b=pickle.load(open('./prePickles/genePairNames.pickle','r'))
# c=pickle.load(open('./prePickles/genePairIndnum.pickle','r'))
