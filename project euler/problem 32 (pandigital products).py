def is_pandigital(s):
	if s.count('0')>0:
		return False
	for i in range(1,10):
		if s.count(str(i))!=1:
			return False
	return True

pandigital={}
for n in range(1,10):
	for m in range (10*3,10**4):
			if is_pandigital(str(n)+str(m)+str(n*m)):
				pandigital[n*m]=str(n)+'x'+str(m)+'='+str(n*m)
				
for n in range(10,10**2):
	for m in range (10*2,10**3):
			if is_pandigital(str(n)+str(m)+str(n*m)):
				pandigital[n*m]=True

print(sum([k for k in pandigital.keys()]))
