s=''
for n in range(10**6/5):
	s=s+str(n)

print(reduce(lambda x,y: x*y, map(int,[s[10**i] for i in range(7)]) ))
