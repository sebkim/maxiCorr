import pickle
import networkx as nx
import itertools
import numpy as np
import matplotlib.pyplot as plt

# numGene = 1000
numGene = 16452

geneNames=pickle.load(open('./prePickles/gNames2.pickle','r'))
geneNames = geneNames[:numGene]

G = nx.Graph()

sickCorrFlattened=pickle.load(open('./prePickles/sickCorrFlattened.pickle','r'))
normalCorrFlattened=pickle.load(open('./prePickles/normalCorrFlattened.pickle','r'))

diffCorrFlattened = ( abs(i-j) for i,j in itertools.izip(sickCorrFlattened, normalCorrFlattened) )

def indexFlattenedGen(numGene):
	for rawI in range(numGene):
		for rawJ in range(rawI+1,numGene):
			yield (rawI, rawJ)

indexFlattened = indexFlattenedGen(numGene)
for d, i in itertools.izip(diffCorrFlattened, indexFlattened):
	if d>=0.5:
		# G.add_edge(i[0], i[1])
		G.add_edge(geneNames[i[0]], geneNames[i[1]])

gDegree=G.degree().items()
gDegreeSorted=sorted(gDegree, key=lambda x: x[1], reverse=True)

f=open('./degreeCount.txt','w')
for i in gDegreeSorted:
	f.write(str(i[0]) + ',' + str(i[1]) + '\n')
	# f.write(str(i[0]) + '\n')
f.close()
