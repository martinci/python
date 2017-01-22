fib=[1,1]
while fib[-1]<4*10**6:
	fib.append(sum(fib[:-3:-1]))
print( sum([f for f in fib if f%2==0]) )
