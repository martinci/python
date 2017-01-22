l=range(1,21)
for i in range(20):
	for j in range(i+1,20):
		if l[j]%l[i]==0:
			l[j]=l[j]/l[i]
		print l
print reduce(lambda x,y: x*y,l)	
