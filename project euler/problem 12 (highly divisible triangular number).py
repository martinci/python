def divisors(n):
	l=0
	i=1
	while i*i<n:
		if n%i==0:
			l+=2
		i+=1
	if n**0.5%1==0:
		l+=1
	return l

n=1
while True:
	if divisors(int((n+1)*n*0.5))>500:
		print ((n+1)*n)/2
		break	
	n+=1
