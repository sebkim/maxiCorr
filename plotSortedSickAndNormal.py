import pickle
import numpy as np
import matplotlib.pyplot as plt

sickCorrFlattened=pickle.load(open('./prePickles/sickCorrFlattened.pickle','r'))
normalCorrFlattened=pickle.load(open('./prePickles/normalCorrFlattened.pickle','r'))

sickCorrFlattened.sort()
normalCorrFlattened.sort()
plt.plot(sickCorrFlattened)
# plt.plot(normalCorrFlattened)
# plt.savefig('plotSortedSickandNormal.pdf', transparent=True,format='pdf')
plt.show()
