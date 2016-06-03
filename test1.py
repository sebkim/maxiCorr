import pickle
import matplotlib.pyplot as plt

a=pickle.load(open('./prePickles/sickCorrFlattened.pickle','r'))
b=pickle.load(open('./prePickles/normalCorrFlattened.pickle','r'))

diff=[abs(i-j) for i,j in zip(a,b)]
overall=zip(diff,a,b)

overall=sorted(overall,key=lambda i:i[0])
