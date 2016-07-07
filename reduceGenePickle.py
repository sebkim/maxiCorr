import pickle
import numpy as np

f=open('./degreeCount.txt','r')
data=f.readlines()
data = [i.split(',') for i in data]
data = [[j.strip() for j in i] for i in data]
data = [[i[0], int(i[-1])] for i in data]
data = data[:2000]
data = [i[0] for i in data]

genes=pickle.load(open('./prePickles/gExpressions2.pickle','r'))
geneNames=pickle.load(open('./prePickles/gNames2.pickle','r'))
geneNames = geneNames.tolist()


selectedIndex=[geneNames.index(d) for d in data]

selectedIndex.sort()

sickAndNormal=np.hsplit(genes,2)
sick=sickAndNormal[0]
normal=sickAndNormal[1]

reducedSick = sick[selectedIndex]
reducedNormal = normal[selectedIndex]

pickle.dump(reducedSick,open('./prePickles/reducedSick.pickle','w'))
pickle.dump(reducedNormal,open('./prePickles/reducedNormal.pickle','w'))
pickle.dump(selectedIndex, open('./prePickles/reducedSelectedIndex.pickle','w'))