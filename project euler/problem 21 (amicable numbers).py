def proper_divisors(n):
	l=[]
	if n<=1:
		return [0]*1
	i=1
	while i*i<n:
		if n%i==0:
			l.append(i)
			l.append(n/i)
		i+=1
	if n**0.5%1==0:
		l.append(int(n**0.5))
	l.remove(n)
	return l

def is_amicable(n):
	a=sum(proper_divisors(n))
	if sum(proper_divisors(a))==n and a!=n:
		return True
	else:
		return False

print [x for x in range(1,10**4) if is_amicable(x)]
print sum([x for x in range(1,10**4) if is_amicable(x)])
