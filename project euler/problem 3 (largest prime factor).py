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
	
factors=[]
n=600851475143
i=2
while i<=n:
	if n%i==0 and is_prime(i):
		factors.append(i)
		n=n/i
		i=2
	else:
		i+=1
print(max(factors))
