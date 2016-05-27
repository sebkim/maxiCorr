# preprocessing data (gExpressions.pickle, and gNames.pickle)

import pickle
import numpy as np
# each keyVal of probes {{probe_name}}: ({{geneName}}, {{entrezID}})
f=open('./data/GPL570-13270.txt','r')
lines=f.readlines()
lines=lines[17:]
probes=[]
for line in lines:
	tmp=line.split('\t')
	probes.append((tmp[0],(tmp[10],tmp[11])))
f.close()
probes=dict(probes)

# genes[0] [{{probe_name}}, {{geneExpression 1}}, ..., {{geneExpression 120}}]
f=open('./data/LungCancerDataWithLabel.csv','r')
lines=f.readlines()
genes=[]
for line in lines:
	tmp=line.split('\t')
	tmp=[i.lstrip('"').rstrip('\n').rstrip('"') for i in tmp]
	tmp=[i if rawI==0 else float(i) for rawI,i in enumerate(tmp)]
	genes.append(tmp)
f.close()

onlyProbes=[i[0] for i in probes]
processedGenes={}


def maxiPickFromTwoLists(a, b):
	c=zip(a,b)
	c=[max(a,b) for a,b in c]
	return c

# each keyVal of processedGenes {{geneName}}: [{{geneExpression 1}}, ..., {{geneExpression 120}}]
for rawI, g in enumerate(genes):
	hereGeneName=probes[g[0]][0]
	if hereGeneName not in processedGenes:
		processedGenes[hereGeneName]=g[1:]
	else:
		print 'x!'*10
		prevGE=processedGenes[hereGeneName]
		newGE=maxiPickFromTwoLists(prevGE,g[1:])
		processedGenes[hereGeneName] = newGE

processedGenes=processedGenes.items()
gNames=[i[0] for i in processedGenes]
gExpressions=[i[1] for i in processedGenes]
gNames=np.array(gNames)
gExpressions=np.array(gExpressions)
pickle.dump(gNames,open('./prePickles/gNames.pickle','w'))
pickle.dump(gExpressions,open('./prePickles/gExpressions.pickle','w'))
