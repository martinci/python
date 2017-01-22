def Collatz_seq(n):
	l=[]
	l.append(n)
	
	if l[-1]==1:
		return l
	else:
		if l[-1]%2==0:
			return l+Collatz_seq(n/2)
		else:
			return l+Collatz_seq(3*n+1)

def LengthCollatz(n):
	count=1
	a=n
	while a!=1:
		if a%2==0: 
			a=a/2
		else:
			a=3*a+1
		count+=1
	return count

MaxLength=1
index=0
for i in range(1,10**6):
	lc=LengthCollatz(i)
	if lc>MaxLength:
		MaxLength=lc
		index=i

print index, MaxLength
