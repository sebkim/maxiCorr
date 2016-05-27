import numpy as np

numGene=16000
genePairIndnum=np.zeros((numGene*numGene-numGene)/2,dtype=object)
itera=0
for i in range(numGene):
	for j in range(i+1, numGene):
		genePairIndnum[itera]=(i,j)
	print i

# import pickle
# genePairIndnum=pickle.load(open('./prePickles/genePairIndnum.pickle','r'))

# import pickle
# sickCorrFlattened=pickle.load(open('./prePickles/sickCorrFlattened.pickle','r'))
