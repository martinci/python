lst=set([(a,b) for a in range(1000) for b in range(1000)])
for (a,b) in lst:
	c=1000-a-b
	if a**2+b**2==c**2:
		print a*b*c
