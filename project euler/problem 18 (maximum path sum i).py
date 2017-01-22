import itertools

with open('problem 18.txt', 'r') as f:
	triangle=f.read().splitlines()

for i in range(len(triangle)):
	triangle[i]=map(int,triangle[i].split(' '))

result=0
for s in itertools.product([0,1],repeat=14):
	suma=[]
	suma.append(triangle[0][0])
	for k in range(1,15):
		suma.append(triangle[k][sum(s[:k])])
	contender=sum(suma)
	if contender > result:
		result=contender
print result	
