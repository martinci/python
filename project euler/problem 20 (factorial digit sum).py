def factorial(n):
	if n==1 or n==0:
		return 1
	else:
		return n*factorial(n-1)

s=str(factorial(100))
sum=0
for c in s:
	sum+=int(c)
print sum
