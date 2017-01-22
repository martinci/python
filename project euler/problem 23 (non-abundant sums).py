def d(n):
	l=0
	if n<=1:
		return 0
	i=1
	while i*i<n:
		if n%i==0:
			l+=i+n/i
		i+=1
	if n**0.5%1==0:
		l+=int(n**0.5)
	return l-n

def sum_of_abundants(n,lst):
	for k in range(12,n):
		if lst[k]>k and lst[n-k]>n-k:
			return True
	return False	

l=[]
l.append(0)
for n in range(1,28123+1):
	l.append(d(n))

print sum([n for n in range(28123+1) if not sum_of_abundants(n,l)])
