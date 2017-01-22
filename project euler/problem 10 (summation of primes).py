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

s=0
for n in range(2*10**6):
	if is_prime(n):
		s+=n
print s
