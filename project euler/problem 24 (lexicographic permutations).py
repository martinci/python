def factorial(n):
	if n==1 or n==0:
		return 1
	else:
		return n*factorial(n-1)

s=[0,1,2,3,4,5,6,7,8,9]
fac=[factorial(k) for k in range(10)]
result=[]
a=10**6
i=1
while 10**6%fac[-i]!=0:
	result.append(s[(a/fac[-i])])
	s.remove(s[(a/fac[-i])])
	a=a-(a/fac[-i])*fac[-i]
	i+=1

result.append(s[(a/fac[-i])])
s.remove(s[(a/fac[-i])])
print result
print s
