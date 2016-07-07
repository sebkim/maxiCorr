import pickle
import networkx as nx
import itertools
import numpy as np
import matplotlib.pyplot as plt

# numGene = 1000
# numGeneAfterFilter=100
numGene = 16452
numGeneAfterFilter=2000

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
		G.add_edge(i[0], i[1])

gDegree=G.degree().items()
gDegreeSorted=sorted(gDegree, key=lambda x: x[1], reverse=True)
gDegreeSorted = gDegreeSorted[:numGeneAfterFilter]
whichNodeSelected = [i[0] for i in gDegreeSorted]
whichNodeSelected.sort()


genes=pickle.load(open('./prePickles/gExpressions2.pickle','r'))
genes = genes[whichNodeSelected]
sickAndNormal=np.hsplit(genes,2)
sick=sickAndNormal[0]
normal=sickAndNormal[1]

sickCorr=np.corrcoef(sick)
normalCorr=np.corrcoef(normal)

numGene = len(whichNodeSelected)
sickCorrFlattened=np.zeros((numGene*numGene-numGene)/2,dtype=np.float32)
normalCorrFlattened=np.zeros((numGene*numGene-numGene)/2,dtype=np.float32)
itera=0
for rawI in range(numGene):
	for rawJ in range(rawI+1,numGene):
		sickCorrFlattened[itera]=sickCorr[rawI][rawJ]
		normalCorrFlattened[itera]=normalCorr[rawI][rawJ]
		itera+=1

sickCorrFlattened.sort()
normalCorrFlattened.sort()
plt.plot(sickCorrFlattened)
plt.plot(normalCorrFlattened)
plt.savefig('plotSortedSickandNormal(highCorrDiffGraph).pdf', transparent=True,format='pdf')
# plt.show()

