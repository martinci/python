def is_prime(n):
	i=2	
	if n<=1:
		return False
	elif n<=3:
		return True
	while i**2<=n:
		if n%i==0:
			return False
		i+=1
	return True

count=0
n=2
l=[]
while count<=10000:
	if is_prime(n):
		l.append(n)
		count+=1
	n+=1
print l[-1]
	
