# import numpy as np

# numGene=16000
# genePairIndnum=np.zeros((numGene*numGene-numGene)/2,dtype=object)
# itera=0
# for i in range(numGene):
# 	for j in range(i+1, numGene):
# 		genePairIndnum[itera]=(i,j)
# 	print i

import pickle
genePairIndnum1=pickle.load(open('./prePickles/genePairIndnum1.pickle','r'))
genePairIndnum2=pickle.load(open('./prePickles/genePairIndnum2.pickle','r'))
genePairIndnum=zip(genePairIndnum1, genePairIndnum2)

# import pickle
# sickCorrFlattened=pickle.load(open('./prePickles/sickCorrFlattened.pickle','r'))
