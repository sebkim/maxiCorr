# it pickles genePairIndnum1 and genePairIndnum2.
# zip(genePairIndnum1, genePairIndnum2) will be genePairIndnum.

import pickle
import numpy as np
import matplotlib.pyplot as plt

geneNames=pickle.load(open('./prePickles/gNames2.pickle','r'))
numGene=geneNames.shape[0]

genePairIndnum1=np.zeros((numGene*numGene-numGene)/2,dtype=np.int32)
genePairIndnum2=np.zeros((numGene*numGene-numGene)/2,dtype=np.int32)

itera=0
f=open('./logGnePairIndnum.log','w',0)
for rawI in range(numGene):
	for rawJ in range(rawI+1,numGene):
		genePairIndnum1[itera]=rawI
		genePairIndnum2[itera]=rawJ
		itera+=1
	f.write('rawI: {} complete!\n'.format(rawI))

pickle.dump(genePairIndnum1,open('./prePickles/genePairIndnum1.pickle','w'))
pickle.dump(genePairIndnum2,open('./prePickles/genePairIndnum2.pickle','w'))
