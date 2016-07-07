f=open('./degreeCount.txt','r')
data=f.readlines()
data = [i.split(',') for i in data]
data = [[j.strip() for j in i] for i in data]
data = [[i[0], int(i[-1])] for i in data]
data = data[:2000]
f2=open('./processedDegreeCount.txt','w')
for i in data:
	f2.write(str(i[0]) + '\n')
