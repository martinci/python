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

length=[0,0,0]
for a in range(-10**3,10**3):
	for b in range(-10**3,10**3):
		n=0
		while is_prime(n**2+a*n+b):
			n+=1
		if n>length[0]:
			length=[n,a,b]
print length, length[1]*length[2]
