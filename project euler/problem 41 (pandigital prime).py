def is_pan(d,n):
	s=str(d)
	for i in range(1,n+1):
		if s.count(str(i))!=1:
			return False
	return True
def is_prime(n):
	if n<=1:
		return False
	if n<=3:
		return True
	i=2
	while i*i<=n:
		if n%i==0:
			return False
		i+=1
	return True

dig=[]
for d in range(1,10)
	dig.append(str(d))
size=9
while size>0:
	p=''
	for i in range(size)
		
	size-=1
