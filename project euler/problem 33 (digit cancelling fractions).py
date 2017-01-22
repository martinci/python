def is_cancelling(n,d):
	sn=str(n)
	sd=str(d)
	if sd[1]==sn[1] and n*int(sd[0]) == int(sn[0])*d and sn[1]!='0':
		return True
	if sd[1]==sn[0] and n*int(sd[0]) == int(sn[1])*d and sn[0]!=0:
		return True
	if sd[0]==sn[1] and n*int(sd[1]) == int(sn[0])*d and sn[1]!=0:
		return True
	if sd[0]==sn[0] and n*int(sd[1]) == int(sn[1])*d and sn[0]!=0:
		return True
	return False

num=1
den=1
for n in range(10,100):
	for d in range(n+1,100):
		if is_cancelling(n,d):
			num*=n
			den*=d
k=2			
while k<=num:		
	if num%k==0 and den%k==0:
		num=num/k
		den=den/k
		k=2	
	else:
		k+=1
print(den)
