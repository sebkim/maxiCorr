f=open('./breastPath.txt','r')
data=f.readlines()

data2=[]
count=1
for rawI, i in enumerate(data):
	if i.startswith(str(count)+'. '):
		data2.append(i)
		count+=1
data2 = [i.strip() for i in data2]
data3=[]
for rawI, i in enumerate(data2):
	hereStr = str(rawI+1) + '. '
	data3.append(i.lstrip(hereStr))

f2 = open('./processedDegreeCount.txt')
ourData = f2.readlines()
ourData = [i.strip() for i in ourData]

for i in data3:
	if i in ourData:
		print i
