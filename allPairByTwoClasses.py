# find all pair correlations by two classes (sick and normal).
# x-axis is sick, and y-axis is normal.
# it outputs sickCorrFlattened.pickle normalCorrFalttened.pickle, genePairNames.pickle, genePairIndnum.pickle .

import pickle
import numpy as np
import matplotlib.pyplot as plt

genes=pickle.load(open('./prePickles/gExpressions2.pickle','r'))
geneNames=pickle.load(open('./prePickles/gNames2.pickle','r'))

sickAndNormal=np.hsplit(genes,2)
sick=sickAndNormal[0]
normal=sickAndNormal[1]

# #test purpose for fast execution
# sick=sick[:1000]
# normal=normal[:1000]
# ###

# sickCorr=np.corrcoef(sick)
# normalCorr=np.corrcoef(normal)

numGene=sickCorr.shape[0]
sickCorrFlattened=np.zeros((numGene*numGene-numGene)/2,dtype=np.float32)
normalCorrFlattened=np.zeros((numGene*numGene-numGene)/2,dtype=np.float32)
genePairNames=np.zeros((numGene*numGene-numGene)/2,dtype=object)
genePairIndnum=np.zeros((numGene*numGene-numGene)/2,dtype=object)

# itera=0
# f=open('./logAllPairByTwoClasses.log','w',0)
# for rawI in range(numGene):
# 	for rawJ in range(rawI+1,numGene):
# 		sickCorrFlattened[itera]=sickCorr[rawI][rawJ]
# 		# normalCorrFlattened[itera]=normalCorr[rawI][rawJ]
# 		# genePairNames[itera]=(geneNames[rawI],geneNames[rawJ])
# 		# genePairIndnum[itera]=(rawI,rawJ)
# 		itera+=1
# 	f.write('rawI: {} complete!\n'.format(rawI))

pickle.dump(sickCorrFlattened,open('./prePickles/sickCorrFlattened.pickle','w'))
pickle.dump(normalCorrFlattened,open('./prePickles/normalCorrFlattened.pickle','w'))
# pickle.dump(genePairNames,open('./prePickles/genePairNames.pickle','w'))
# pickle.dump(genePairIndnum,open('./prePickles/genePairIndnum.pickle','w'))


# plt.scatter(sickCorrFlattened,normalCorrFlattened)
# plt.show()

# a=pickle.load(open('./prePickles/sickAndNormalCorrFlattened.pickle','r'))
# b=pickle.load(open('./prePickles/genePairNames.pickle','r'))
# c=pickle.load(open('./prePickles/genePairIndnum.pickle','r'))
