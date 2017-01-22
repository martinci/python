def factorial(n):
	if n==1 or n==0:
		return 1
	else:
		return n*factorial(n-1)

fac=[factorial(n) for n in range(0,10)]		
def is_curious(n):
	suma=0
	for d in str(n):
		suma+=fac[int(d)]
	if suma==n:
		return True
	return False

print(sum([n for n in range(3,10**7) if is_curious(n)]))
