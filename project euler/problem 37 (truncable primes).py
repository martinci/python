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
	
primes={}
trunc=[]
for n in range(2,10**6):
	if is_prime(n):
		primes[str(n)]=False
for p in primes.keys():
	br=0
	for l in range(1,len(p)):
		if not p[l:] in primes.keys():
			br=1
			break
		if not p[:l] in primes.keys():
			br=1
			break
	if br==0 and int(p)>7:
		primes[p]=True
		
print(sum([int(p) for p in primes.keys() if primes[p]]))
