file=open('frequencies.txt','r')

cTime=[0 for i in range(0,128)]

for i in range(127,-1,-1):
	f=float(file.readline())
	cTime[i]=int(1e6/f/2)
	print(f)
print(cTime)
outFile=open('cycletime.txt','w')

outFile.write('ct[128]={')
for i in range(0,128):
	outFile.write(str(cTime[i])+',')
outFile.write('}')
